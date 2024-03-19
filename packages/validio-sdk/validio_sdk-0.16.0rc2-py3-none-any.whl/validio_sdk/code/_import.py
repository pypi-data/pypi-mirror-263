import dataclasses
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, cast

from validio_sdk.resource._resource import DiffContext, Resource
from validio_sdk.resource._server_resources import CREDENTIALS_WITH_DEPENDENCIES
from validio_sdk.resource.channels import Channel
from validio_sdk.resource.credentials import Credential
from validio_sdk.resource.notification_rules import NotificationRule
from validio_sdk.resource.segmentations import Segmentation
from validio_sdk.resource.sources import Source
from validio_sdk.resource.validators import Validator
from validio_sdk.resource.windows import Window


@dataclasses.dataclass
class VariableName:
    """Remove quotes when we go to write out the variable name inside a list."""

    value: str

    def __repr__(self) -> str:
        return self.value


@dataclass
class VariableNameMapping:
    next_var_id: int = 0
    name_to_var: dict[str, str] = dataclasses.field(default_factory=dict)

    def get_or_create_var(self, cls: type, name: str) -> str:
        if name not in self.name_to_var:
            var_name = f"{cls.__name__.lower()}_{self.next_var_id}"
            self.next_var_id += 1
            self.name_to_var[name] = var_name
        return self.name_to_var[name]


@dataclass
class ImportContext:
    variable_names: dict[type, VariableNameMapping] = dataclasses.field(
        default_factory=dict
    )
    # Variable name => Declaration
    resource_decls: dict[str, str] = dataclasses.field(default_factory=dict)

    def get_variable(self, cls: type, name: str) -> str:
        if cls not in self.variable_names:
            self.variable_names[cls] = VariableNameMapping()

        return self.variable_names[cls].get_or_create_var(cls, name)

    def add_resource_decl(self, cls: type, name: str, decl: str) -> None:
        var_name = self.get_variable(cls, name)
        if var_name in self.resource_decls:
            raise RuntimeError(f"var {var_name} has already been declared")

        self.resource_decls[var_name] = decl

    def output(self) -> str:
        resource_types = DiffContext.fields()
        resource_types.sort()

        imports = (
            [
                "from validio_sdk import *",
                "from validio_sdk.graphql_client.enums import *",
                "from validio_sdk.resource.thresholds import *",
            ]
            + [
                f"from validio_sdk.resource.{_type} import *"
                for _type in resource_types
            ]
            + ["\n"]
        )

        decls = []
        for resource_type, var_mapping in self.variable_names.items():
            for resource_name, var_name in var_mapping.name_to_var.items():
                if var_name not in self.resource_decls:
                    decls.append(
                        f"{var_name} = {resource_name!r}  # FIXME: manually change"
                        " to actual resource reference"
                    )
        if len(decls) > 0:
            # Add a (cosmetic) new line before the var declarations and the imports.
            decls.append("\n")
        for var_name, decl in self.resource_decls.items():
            decls.append(f"{var_name} = {decl}")

        return "\n".join(imports + decls)


async def _import(
    ctx: DiffContext,
) -> str:
    import_ctx = ImportContext()

    def import_credential(cls: type, name: str, r: Resource) -> None:
        inits: list[tuple[str, Any, str | None]] | None = None
        credential_object = cast(Any, r)
        if hasattr(credential_object, "warehouse_credential_name"):
            credential = import_ctx.get_variable(
                Credential, credential_object.warehouse_credential_name
            )
            inits = [("warehouse_credential", credential, None)]

        import_ctx.add_resource_decl(
            cls,
            name,
            r._import_str(
                indent_level=0,
                import_ctx=import_ctx,
                inits=inits,
            ),
        )

    add_resource_decls(
        ctx=ctx,
        resource_types=[("credentials", Credential), ("channels", Channel)],
        importer=import_credential,
    )

    # These depend on credentials.
    def import_src_dst(cls: type, name: str, r: Resource) -> None:
        credential = import_ctx.get_variable(Credential, cast(Any, r).credential_name)
        import_ctx.add_resource_decl(
            cls,
            name,
            r._import_str(
                indent_level=0,
                import_ctx=import_ctx,
                inits=[("credential", credential, None)],
            ),
        )

    add_resource_decls(
        ctx=ctx,
        resource_types=[("sources", Source)],
        importer=import_src_dst,
    )

    # These depend on sources
    def import_source_deps(cls: type, name: str, r: Resource) -> None:
        source = import_ctx.get_variable(Source, cast(Any, r).source_name)
        import_ctx.add_resource_decl(
            cls,
            name,
            r._import_str(
                indent_level=0, import_ctx=import_ctx, inits=[("source", source, None)]
            ),
        )

    add_resource_decls(
        ctx=ctx,
        resource_types=[("windows", Window), ("segmentations", Segmentation)],
        importer=import_source_deps,
    )

    # Notification rules
    def import_notification_rules(cls: type, name: str, r: Resource) -> None:
        rule = cast(NotificationRule, r)
        channel = import_ctx.get_variable(Channel, rule.channel_name)

        # This works a bit different from `channel` because `channel` is a
        # parent resource and we skip all `<resource>_name` params whereas if we
        # would set `conditions` in `inits` we would get it twice which is not
        # what we want.
        # Also we ignore the type of sources because it's supposed to hold
        # strings and not `VariableName` but we re-use the same type to get a
        # proper config file.
        if rule.conditions.source_condition:
            rule.conditions.source_condition.sources = [  # type: ignore
                VariableName(
                    import_ctx.get_variable(Source, source_name),
                )  # type: ignore
                for source_name in rule.conditions.source_condition.sources
            ]

        import_ctx.add_resource_decl(
            cls,
            name,
            rule._import_str(
                indent_level=0,
                import_ctx=import_ctx,
                inits=[("channel", channel, None)],
            ),
        )

    add_resource_decls(
        ctx=ctx,
        resource_types=[("notification_rules", NotificationRule)],
        importer=import_notification_rules,
    )

    def import_validators(cls: type, name: str, r: Resource) -> None:
        v = cast(Validator, r)
        window = import_ctx.get_variable(Window, v.window_name)
        segmentation = import_ctx.get_variable(Segmentation, v.segmentation_name)
        inits: list[tuple[str, Any, str | None]] = [
            ("window", window, None),
            ("segmentation", segmentation, None),
        ]

        import_ctx.add_resource_decl(
            cls,
            name,
            r._import_str(
                indent_level=0,
                import_ctx=import_ctx,
                inits=inits,
            ),
        )

    add_resource_decls(
        ctx=ctx,
        resource_types=[("validators", Validator)],
        importer=import_validators,
    )

    return import_ctx.output()


def add_resource_decls(
    ctx: DiffContext,
    resource_types: list[tuple[str, type]],
    importer: Callable[[type, str, Resource], None],
) -> None:
    for resource_type, cls in resource_types:
        resources = list(getattr(ctx, resource_type).items())
        # Sort the resources by name so that the generated file has a stable order.
        # We must however ensure that we sort resources that has dependencies on
        # others last.
        resources.sort(
            key=lambda p: (
                p[1].__class__.__name__ in CREDENTIALS_WITH_DEPENDENCIES,
                p[0],
            )
        )

        for name, r in resources:
            importer(cls, name, r)
