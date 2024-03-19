"""Sources."""

import inspect
import json
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, cast

from camel_converter import to_snake

# We need validio_sdk in scope due to eval.
# ruff: noqa: F401
import validio_sdk
from validio_sdk.graphql_client import CsvParserInput, FileFormat
from validio_sdk.graphql_client.enums import StreamingSourceMessageFormat
from validio_sdk.graphql_client.input_types import (
    StreamingSourceMessageFormatConfigInput,
)
from validio_sdk.resource._diffable import Diffable
from validio_sdk.resource._resource import Resource
from validio_sdk.resource._serde import (
    CONFIG_FIELD_NAME,
    NODE_TYPE_FIELD_NAME,
    ImportValue,
    _api_create_input_params,
    _api_update_input_params,
    _encode_resource,
    _import_resource_params,
    get_children_node,
)
from validio_sdk.resource.credentials import (
    AwsAthenaCredential,
    AwsCredential,
    AwsRedshiftCredential,
    AzureSynapseCredential,
    Credential,
    DatabricksCredential,
    DemoCredential,
    GcpCredential,
    KafkaCredential,
    PostgreSqlCredential,
    SnowflakeCredential,
)
from validio_sdk.scalars import JsonTypeDefinition
from validio_sdk.validio_client import ValidioAPIClient

if TYPE_CHECKING:
    from validio_sdk.resource._diff import DiffContext

"""Max lookback time period for warehouse sources"""
MAX_LOOKBACK_DAYS = 365

"""We allow only 5-digit cron expressions"""
CRON_DIGITS = 5


class Source(Resource):
    """A source configuration.

    https://docs.validio.io/docs/sources
    """

    def __init__(
        self,
        name: str,
        credential: Credential,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :param name: Unique resource name assigned to the source
        :param credential: The credential to attach the source to
        :param jtd_schema: The schema to associate the source with. If None is
            provided (default), then the schema will be automatically inferred.
            https://docs.validio.io/docs/source-configuration#4-schema
        """
        super().__init__(name, credential._resource_graph)
        self.credential_name: str = credential.name
        self.jtd_schema = jtd_schema
        _sanitize_jtd_schema(self.jtd_schema)

        credential.add(name, self)

    def _immutable_fields(self) -> set[str]:
        return {"credential_name"}

    def _mutable_fields(self) -> set[str]:
        # Note: jtd_schema is a mutable field but is handled specially in the diff
        # process - since schemas can be managed automatically. So it's not listed
        # here
        return set({})

    def resource_class_name(self) -> str:
        """Returns the base class name."""
        return "Source"

    def _api_create_input(self, namespace: str, ctx: "DiffContext") -> Any:
        return _api_create_input_params(
            self,
            namespace=namespace,
            overrides={
                **self._api_input_overrides(),
                "credential_id": ctx.credentials[self.credential_name]._must_id(),
            },
        )

    def _api_update_input(self, _namespace: str, _: "DiffContext") -> Any:
        return _api_update_input_params(self, overrides=self._api_input_overrides())

    def _api_input_overrides(self) -> dict[str, Any]:
        return {}

    def _encode(self) -> dict[str, object]:
        # Drop a couple fields here since they are not part of the constructor
        # for when we deserialize back.
        return _encode_resource(self, skip_fields={"credential_name"})

    @staticmethod
    def _decode(
        ctx: "DiffContext",
        cls: type,
        obj: dict[str, dict[str, object]],
        credential: Credential,
    ) -> "Source":
        source = cls(
            **cast(
                dict[str, object], {**obj[CONFIG_FIELD_NAME], "credential": credential}
            )
        )

        children_obj = cast(dict[str, dict[str, object]], get_children_node(obj))
        Source._decode_segmentations(ctx, source, children_obj)
        Source._decode_windows(ctx, source, children_obj)
        Source._register_validators_to_decode(ctx, children_obj)

        return source

    @staticmethod
    def _decode_segmentations(
        ctx: "DiffContext", source: "Source", children_obj: dict[str, dict[str, object]]
    ) -> None:
        from validio_sdk.resource.segmentations import Segmentation

        segmentations_obj = cast(
            dict[str, dict[str, object]],
            (
                children_obj[Segmentation.__name__]
                if Segmentation.__name__ in children_obj
                else {}
            ),
        )
        segmentations = {}
        for segmentation_name, value in segmentations_obj.items():
            segmentation = Segmentation._decode(value, source)
            segmentations[segmentation_name] = segmentation
            ctx.segmentations[segmentation_name] = segmentation

        if len(segmentations) > 0:
            source._children[Segmentation.__name__] = cast(
                dict[str, Resource], segmentations
            )

    @staticmethod
    def _decode_windows(
        ctx: "DiffContext", source: "Source", children_obj: dict[str, dict[str, object]]
    ) -> None:
        from validio_sdk.resource.windows import Window

        windows_obj = cast(
            dict[str, dict[str, object]],
            children_obj[Window.__name__] if Window.__name__ in children_obj else {},
        )

        windows = {}
        for window_name, value in windows_obj.items():
            window = Window._decode(value, source)
            windows[window_name] = window
            ctx.windows[window_name] = window

        if len(windows) > 0:
            source._children[Window.__name__] = cast(dict[str, Resource], windows)

    @staticmethod
    def _register_validators_to_decode(
        ctx: "DiffContext", children_obj: dict[str, dict[str, Any]]
    ) -> None:
        """
        While we decode the graph, we can't resolve validators until all its
        dependencies have been resolved - potential dependencies of a validator
        are (reference sources). So the idea is that, we keep track of
        validators here. After we've done the pass through all other resources,
        we resolve validators separately.
        """
        from validio_sdk.resource.validators import Validator

        validators_obj = (
            children_obj[Validator.__name__]
            if Validator.__name__ in children_obj
            else {}
        )
        for name, value in validators_obj.items():
            ctx.pending_validators_raw[name] = (
                eval(f"validio_sdk.resource.validators.{value[NODE_TYPE_FIELD_NAME]}"),
                value,
            )

    def _import_params(self) -> dict[str, ImportValue]:
        return _import_resource_params(
            resource=self,
            skip_fields={"jtd_schema"},
        )

    async def _api_infer_schema(
        self, credential: Credential, client: ValidioAPIClient
    ) -> None:
        # e.g GcpBigQuerySource
        class_name = self.__class__.__name__
        # => GcpBigQuery
        source_type_name = class_name[: -len("Source")]
        # => gcp_big_query
        resource_snake_case = to_snake(source_type_name)
        # => infer_gcp_big_query_schema
        infer_method = f"infer_{resource_snake_case}_schema"
        infer_fn = client.__getattribute__(infer_method)

        infer_args = self._api_infer_schema_input()
        if infer_args is None:
            response = await infer_fn()
        else:
            cls = eval(
                f"validio_sdk.graphql_client.input_types.{source_type_name}InferSchemaInput"
            )
            response = await infer_fn(
                cls(**{**cast(Any, infer_args), "credential_id": credential._must_id()})
            )

        self.jtd_schema = response
        _sanitize_jtd_schema(self.jtd_schema)

    @abstractmethod
    def _api_infer_schema_input(self) -> dict[str, object] | None:
        """
        Return the fields (as defined in the graphql ...InferSchemaInput as well
        as their values. The credential id is provided by the caller so that's
        ignored here. If None is returned (Demo), then the inference method is
        assumed to take no parameters (not even a credential id).
        """


def _sanitize_jtd_schema(jtd_schema: JsonTypeDefinition | None) -> None:
    # TODO VR-2073:
    # The jtd python lib for some reason wants this property to be a string
    # even though the spec and all other language libraries say it's a bool.
    if jtd_schema and "additionalProperties" in jtd_schema:
        del jtd_schema["additionalProperties"]


class DemoSource(Source):
    """A Demo source configuration."""

    def __init__(
        self,
        name: str,
        credential: DemoCredential,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """Constructor."""
        super().__init__(name, credential, jtd_schema)

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return None


class DbtSource(Source):
    """A base class source."""

    def __init__(
        self,
        name: str,
        credential: GcpCredential,
        project_name: str,
        job_name: str,
        schedule: str = "0/15 * * * *",
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :project_name: The name of the dbt project.
        :job_name: The name of the dbt job.
        :param schedule: A 5-digit cron expression specifying how when the source
            polls for new data. Example: '0 0 * * *' to poll daily at midnight.
        """
        super().__init__(name, credential, jtd_schema)

        self.project_name = project_name
        self.job_name = job_name
        self.schedule = schedule

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "project_name",
                "job_name",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return None


class DbtModelRunSource(DbtSource):
    """A source for dbt model run results."""


class DbtTestResultSource(DbtSource):
    """A source for dbt test results."""


class GcpBigQuerySource(Source):
    """A BigQuery source configuration.

    https://docs.validio.io/docs/bigquery
    """

    def __init__(
        self,
        name: str,
        credential: GcpCredential,
        project: str,
        dataset: str,
        table: str,
        cursor_field: str,
        lookback_days: int,
        schedule: str,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :param project: GCP project where the BigQuery instance resides.
        :param dataset: Dataset containing the configured table.
        :param table: Name of table to monitor.
        :param cursor_field: Timestamp column specifying when each row in the table
            was added/updated.
            https://docs.validio.io/docs/data-warehouse#general-considerations
        :param lookback_days: How far back in time to start data monitoring
            from. (max 365)
        :param schedule: A 5-digit cron expression specifying how when the source
            polls for new data. Example: '0 0 * * *' to poll daily at midnight.
        """
        super().__init__(name, credential, jtd_schema)

        self.project = project
        self.dataset = dataset
        self.table = table
        self.cursor_field = cursor_field
        self.lookback_days = lookback_days
        self.schedule = schedule

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "project",
                "dataset",
                "table",
                "cursor_field",
            },
        }

    def _mutable_fields(self) -> set[str]:
        return {
            *super()._mutable_fields(),
            *{
                "lookback_days",
                "schedule",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            "dataset": self.dataset,
            "project": self.project,
            "table": self.table,
        }


class SnowflakeSource(Source):
    """
    A Snowflake source configuration.

    https://docs.validio.io/docs/snowflake
    """

    def __init__(
        self,
        name: str,
        credential: SnowflakeCredential,
        database: str,
        db_schema: str,
        table: str,
        cursor_field: str,
        lookback_days: int,
        schedule: str,
        warehouse: str | None = None,
        role: str | None = None,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :param database: Name of the snowflake database to connect to (immutable).
        :param db_schema: Name of the schema in the database that contains the
            table to monitor (immutable).
        :param table: Name of table to monitor (immutable).
        :param warehouse: Snowflake virtual warehouse to use to run queries (immutable).
        :param role: Snowflake role to assume when running queries (immutable).
        :param cursor_field: Timestamp column specifying when each row in the table
            was added/updated (immutable).
            https://docs.validio.io/docs/data-warehouse#general-considerations
        :param lookback_days: How far back in time to start data ingestion
            from. (max 365)
        :param schedule: A 5-digit cron expression specifying how when the source
            polls for new data. Example: '0 0 * * *' to poll daily at midnight.
        """
        super().__init__(name, credential, jtd_schema)

        self.database = database
        self.db_schema = db_schema
        self.table = table
        self.warehouse = warehouse
        self.role = role
        self.cursor_field = cursor_field
        self.lookback_days = lookback_days
        self.schedule = schedule

    def __getattr__(self, name: str) -> str:
        """Getter for field aliases."""
        # schema is called db_schema
        if name == "schema":
            return self.db_schema
        raise AttributeError

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "db_schema",
                "database",
                "table",
                "cursor_field",
                "warehouse",
                "role",
            },
        }

    def _mutable_fields(self) -> set[str]:
        return {
            *super()._mutable_fields(),
            *{
                "lookback_days",
                "schedule",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            "database": self.database,
            "db_schema": self.db_schema,
            "table": self.table,
            "role": self.role,
            "warehouse": self.warehouse,
        }


class PostgresLikeSource(Source):
    """A Postgres compatible source configuration."""

    def __init__(
        self,
        name: str,
        credential: PostgreSqlCredential | AwsRedshiftCredential,
        database: str | None,
        db_schema: str,
        table: str,
        cursor_field: str,
        lookback_days: int,
        schedule: str,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :param db_schema: Name of the schema in the database that contains the table.
        :param table: Name of table to monitor.
        :param database: Name of the database containing the specified schema. If none
            is provided, the `default_database` of the provided credential is used.
        :param cursor_field: Timestamp column specifying when each row in the table
            was added/updated.
            https://docs.validio.io/docs/data-warehouse#general-considerations
        :param lookback_days: How far back in time to start data ingestion
            from. (max 365)
        :param schedule: A 5-digit cron expression specifying how when the source
            polls for new data. Example: '0 0 * * *' to poll daily at midnight.
        """
        super().__init__(name, credential, jtd_schema)

        self.db_schema = db_schema
        self.table = table
        self.database = database
        self.cursor_field = cursor_field
        self.lookback_days = lookback_days
        self.schedule = schedule

    def __getattr__(self, name: str) -> str:
        """Getter for field aliases."""
        # schema is called db_schema
        if name == "schema":
            return self.db_schema
        raise AttributeError

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "db_schema",
                "database",
                "table",
                "cursor_field",
            },
        }

    def _mutable_fields(self) -> set[str]:
        return {
            *super()._mutable_fields(),
            *{
                "lookback_days",
                "schedule",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            "database": self.database,
            "db_schema": self.db_schema,
            "table": self.table,
        }


class PostgreSqlSource(PostgresLikeSource):
    """A PostgreSql source configuration.

    https://docs.validio.io/docs/postgresql
    """


class AwsRedshiftSource(PostgresLikeSource):
    """A Redshift source configuration.

    https://docs.validio.io/docs/redshift
    """


class AwsAthenaSource(Source):
    """
    An AWS Athena source configuration.

    https://docs.validio.io/docs/athena
    """

    def __init__(
        self,
        name: str,
        credential: AwsAthenaCredential,
        catalog: str,
        database: str,
        table: str,
        cursor_field: str,
        lookback_days: int,
        schedule: str,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :param catalog: Name of the Athena catalog to connect to (immutable).
        :param database: Name of the database in the catalog (immutable).
        :param table: Name of table to monitor (immutable).
        :param cursor_field: Timestamp column specifying when each row in the table
            was added/updated (immutable).
            https://docs.validio.io/docs/data-warehouse#general-considerations
        :param lookback_days: How far back in time to start data ingestion
            from. (max 365)
        :param schedule: A 5-digit cron expression specifying how when the source
            polls for new data. Example: '0 0 * * *' to poll daily at midnight.
        """
        super().__init__(name, credential, jtd_schema)

        self.catalog = catalog
        self.database = database
        self.table = table
        self.cursor_field = cursor_field
        self.lookback_days = lookback_days
        self.schedule = schedule

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "catalog",
                "database",
                "table",
                "cursor_field",
            },
        }

    def _mutable_fields(self) -> set[str]:
        return {
            *super()._mutable_fields(),
            *{
                "lookback_days",
                "schedule",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            "catalog": self.catalog,
            "database": self.database,
            "table": self.table,
        }


class DatabricksSource(Source):
    """
    A Databricks source configuration.

    https://docs.validio.io/docs/databricks
    """

    def __init__(
        self,
        name: str,
        credential: DatabricksCredential,
        catalog: str,
        db_schema: str,
        table: str,
        cursor_field: str,
        lookback_days: int,
        schedule: str,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :param catalog: Name of the Databricks catalog to connect to (immutable).
        :param db_schema: Name of the schema in the catalog (immutable).
        :param table: Name of table to monitor (immutable).
        :param cursor_field: Timestamp column specifying when each row in the table
            was added/updated (immutable).
            https://docs.validio.io/docs/data-warehouse#general-considerations
        :param lookback_days: How far back in time to start data ingestion
            from. (max 365)
        :param schedule: A 5-digit cron expression specifying how when the source
            polls for new data. Example: '0 0 * * *' to poll daily at midnight.
        """
        super().__init__(name, credential, jtd_schema)

        self.catalog = catalog
        self.db_schema = db_schema
        self.table = table
        self.cursor_field = cursor_field
        self.lookback_days = lookback_days
        self.schedule = schedule

    def __getattr__(self, name: str) -> str:
        """Getter for field aliases."""
        # schema is called db_schema
        if name == "schema":
            return self.db_schema
        raise AttributeError

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "catalog",
                "db_schema",
                "table",
                "cursor_field",
            },
        }

    def _mutable_fields(self) -> set[str]:
        return {
            *super()._mutable_fields(),
            *{
                "lookback_days",
                "schedule",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            "catalog": self.catalog,
            "db_schema": self.db_schema,
            "table": self.table,
        }


class AzureSynapseSource(Source):
    """
    A Azure Synapse source configuration.

    https://docs.validio.io/docs/azure-synapse
    """

    def __init__(
        self,
        name: str,
        credential: AzureSynapseCredential,
        database: str,
        db_schema: str,
        table: str,
        cursor_field: str,
        lookback_days: int,
        schedule: str,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :param database: Name of the Azure Synapse database to connect to (immutable).
        :param db_schema: Name of the schema in the database (immutable).
        :param table: Name of table to monitor (immutable).
        :param cursor_field: Timestamp column specifying when each row in the table
            was added/updated (immutable).
            https://docs.validio.io/docs/data-warehouse#general-considerations
        :param lookback_days: How far back in time to start data ingestion
            from. (max 365)
        :param schedule: A 5-digit cron expression specifying how when the source
            polls for new data. Example: '0 0 * * *' to poll daily at midnight.
        """
        super().__init__(name, credential, jtd_schema)

        self.database = database
        self.db_schema = db_schema
        self.table = table
        self.cursor_field = cursor_field
        self.lookback_days = lookback_days
        self.schedule = schedule

    def __getattr__(self, name: str) -> str:
        """Getter for field aliases."""
        # schema is called db_schema
        if name == "schema":
            return self.db_schema
        raise AttributeError

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "database",
                "db_schema",
                "table",
                "cursor_field",
            },
        }

    def _mutable_fields(self) -> set[str]:
        return {
            *super()._mutable_fields(),
            *{
                "lookback_days",
                "schedule",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            "database": self.catalog,
            "db_schema": self.db_schema,
            "table": self.table,
        }


# Streaming


class StreamingMessageFormat(Diffable):
    """Message format configuration for a streaming source."""

    def __init__(
        self,
        format: StreamingSourceMessageFormat | None = StreamingSourceMessageFormat.JSON,
        db_schema: str | None = None,
    ):
        """
        Constructor.

        :param format: Specifies the format of messages in the stream
        :param schema: Schema of messages in the stream. Default is JSON.
        """
        self.format = format
        self.db_schema = db_schema

    def __getattr__(self, name: str) -> str | None:
        """Getter for field aliases."""
        # schema is called db_schema
        if name == "schema":
            return self.db_schema
        raise AttributeError

    @staticmethod
    def _from_any(other: Any) -> "StreamingMessageFormat":
        if isinstance(other, StreamingMessageFormat):
            return other
        if isinstance(other, dict):
            return StreamingMessageFormat(**other)

        params = {
            f: getattr(other, f)
            for f in list(inspect.signature(StreamingMessageFormat).parameters)
        }
        return StreamingMessageFormat(**params)

    def _immutable_fields(self) -> set[str]:
        return set({})

    def _mutable_fields(self) -> set[str]:
        return {
            "format",
            "db_schema",
        }

    def _nested_objects(self) -> dict[str, Diffable | list[Diffable] | None]:
        return {}

    def _encode(self) -> dict[str, object]:
        return self.__dict__


class StreamSource(Source):
    """Base class for streaming sources."""

    def __init__(
        self,
        name: str,
        credential: Credential,
        jtd_schema: JsonTypeDefinition | None = None,
        message_format: StreamingMessageFormat | None = None,
    ):
        """Constructor."""
        super().__init__(name, credential, jtd_schema)

        self.message_format = (
            StreamingMessageFormat()
            if message_format is None
            else StreamingMessageFormat._from_any(message_format)
        )

    def _nested_objects(self) -> dict[str, Diffable | list[Diffable] | None]:
        return {
            "message_format": self.message_format,
        }

    def _message_format_input(
        self,
    ) -> StreamingSourceMessageFormatConfigInput | None:
        return StreamingSourceMessageFormatConfigInput(
            format=self.message_format.format,
            db_schema=self.message_format.db_schema,
        )

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            **(super()._api_infer_schema_input() or {}),
            "message_format": self._message_format_input(),
        }

    def _api_input_overrides(self) -> dict[str, Any]:
        return {
            "message_format": self._message_format_input(),
        }


class AwsKinesisSource(StreamSource):
    """
    A Kinesis source configuration.

    https://docs.validio.io/docs/kinesis
    """

    def __init__(
        self,
        name: str,
        credential: AwsCredential,
        region: str,
        stream_name: str,
        jtd_schema: JsonTypeDefinition | None = None,
        message_format: StreamingMessageFormat | None = None,
    ):
        """
        Constructor.

        :param region: AWS region where the Kinesis stream resides.
        :param stream_name: The Kinesis stream to monitor.
        :param message_format: The format of messages in the stream.
        """
        super().__init__(name, credential, jtd_schema, message_format)

        self.region = region
        self.stream_name = stream_name

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "region",
                "stream_name",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            **(super()._api_infer_schema_input() or {}),
            "region": self.region,
            "stream_name": self.stream_name,
        }


class GcpPubSubBaseSource(StreamSource, ABC):
    """Base definition for PubSub source configuration."""

    def __init__(
        self,
        name: str,
        credential: GcpCredential,
        project: str,
        subscription_id: str,
        jtd_schema: JsonTypeDefinition | None = None,
        message_format: StreamingMessageFormat | None = None,
    ):
        """
        Constructor.

        :param project: The GCP project where the pubsub topic resides.
        :param subscription_id: The subscription ID of the subscription
            to use to consumer messages from the topic.
            https://cloud.google.com/pubsub/docs/create-subscription
        :param message_format: The format of messages in the stream.
        """
        super().__init__(name, credential, jtd_schema, message_format)

        self.project = project
        self.subscription_id = subscription_id

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "project",
                "subscription_id",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            **(super()._api_infer_schema_input() or {}),
            "project": self.project,
            "subscription_id": self.subscription_id,
        }


class GcpPubSubSource(GcpPubSubBaseSource):
    """A PubSub source configuration. See GcpPubSubBase for properties."""


class GcpPubSubLiteSource(GcpPubSubBaseSource):
    """A PubSubLite source configuration."""

    def __init__(
        self,
        name: str,
        credential: GcpCredential,
        project: str,
        location: str,
        subscription_id: str,
        jtd_schema: JsonTypeDefinition | None = None,
        message_format: StreamingMessageFormat | None = None,
    ):
        """
        Constructor.

        :param project: The GCP project where the pubsub topic resides.
        :param location: The region where the pubsub topic resides: e.g
            e.g. europe-west3-a
            https://cloud.google.com/pubsub/lite/docs/locations
        :param subscription_id: The subscription ID of the subscription
            to use to consumer messages from the stream.
            https://cloud.google.com/pubsub/docs/create-subscription
        :param message_format: The format of messages in the stream.
        """
        super().__init__(
            name=name,
            credential=credential,
            jtd_schema=jtd_schema,
            project=project,
            subscription_id=subscription_id,
            message_format=message_format,
        )

        self.location = location

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{"location"},
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            **(super()._api_infer_schema_input() or {}),
            "location": self.location,
        }


class KafkaSource(StreamSource):
    """
    A Kafka source configuration.

    https://docs.validio.io/docs/kafka
    """

    def __init__(
        self,
        name: str,
        credential: KafkaCredential,
        topic: str,
        jtd_schema: JsonTypeDefinition | None = None,
        message_format: StreamingMessageFormat | None = None,
    ):
        """
        Constructor.

        :param topic: Topic to read data from.
        :param message_format: The format of messages in the stream.
        """
        super().__init__(name, credential, jtd_schema, message_format)

        self.topic = topic

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{"topic"},
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            **(super()._api_infer_schema_input() or {}),
            "topic": self.topic,
        }


# Object storages


class CsvParserConfig(Diffable):
    """CSV configuration for a source."""

    def __init__(
        self,
        null_marker: str | None = None,
        delimiter: str = ",",
    ):
        """
        Constructor.

        :param null_marker: Specifies what character sequence represents
            NULL (defaults to empty string)
        :param delimiter: Delimiter used in the csv file
        """
        self.null_marker = null_marker
        self.delimiter = delimiter

    @staticmethod
    def _from_any(other: Any) -> "CsvParserConfig":
        if isinstance(other, CsvParserConfig):
            return other
        if isinstance(other, dict):
            return CsvParserConfig(**other)

        params = {
            f: getattr(other, f)
            for f in list(inspect.signature(CsvParserConfig).parameters)
        }
        return CsvParserConfig(**params)

    def _immutable_fields(self) -> set[str]:
        return set({})

    def _mutable_fields(self) -> set[str]:
        return {
            "null_marker",
            "delimiter",
        }

    def _nested_objects(self) -> dict[str, Diffable | list[Diffable] | None]:
        return {}

    def _encode(self) -> dict[str, object]:
        return json.loads(
            json.dumps(
                self.__dict__,
                default=lambda o: o._encode(),
            )
        )


class ObjectStorageSource(Source, ABC):
    """
    Base class for object storage source configuration.

    https://docs.validio.io/docs/s3
    """

    def __init__(
        self,
        name: str,
        credential: Credential,
        bucket: str,
        file_pattern: str | None,
        schedule: str,
        csv: CsvParserConfig | None = None,
        file_format: FileFormat | None = None,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :param bucket: Name of the bucket to ingest files from.
        :param file_pattern: Glob pattern against file names, used to filter in
            what files are eligible for ingestion.
        :param schedule: A 5-digit cron expression specifying how when the source
            polls for new data. Example: '0 0 * * *' to poll daily at midnight.
        """
        super().__init__(name, credential, jtd_schema)

        self.bucket = bucket
        self.file_pattern = file_pattern
        self.schedule = schedule
        self.csv = (
            CsvParserConfig(null_marker=None, delimiter=",")
            if csv is None
            else CsvParserConfig._from_any(csv)
        )
        self.file_format = (
            None
            if file_format is None
            # When we decode, enums are passed in a strings
            else (
                file_format
                if isinstance(file_format, FileFormat)
                else FileFormat(file_format)
            )
        )

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{"bucket", "file_format"},
        }

    def _mutable_fields(self) -> set[str]:
        return {
            *super()._mutable_fields(),
            *{
                "schedule",
                "file_pattern",
            },
        }

    def _nested_objects(self) -> dict[str, Diffable | list[Diffable] | None]:
        return {
            "csv": self.csv,
        }

    def _csv_parser_input(self) -> CsvParserInput:
        return CsvParserInput(
            delimiter=self.csv.delimiter,
            # type: ignore[call-arg]
            null_marker=self.csv.null_marker,
        )

    def _api_input_overrides(self) -> dict[str, Any]:
        return {
            "csv": self._csv_parser_input(),
        }


class AwsS3Source(ObjectStorageSource):
    """
    An AWS S3 source configuration.

    https://docs.validio.io/docs/s3
    """

    def __init__(
        self,
        name: str,
        credential: AwsCredential,
        bucket: str,
        prefix: str,
        file_pattern: str | None,
        schedule: str,
        csv: CsvParserConfig | None = None,
        file_format: FileFormat | None = None,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :param bucket: Name of the bucket to read files from.
        :param prefix: Folder prefix. e.g. if '/a/b' is specified as a prefix,
            then only files located in the '/a/b' folder will be ingested
        """
        super().__init__(
            name=name,
            credential=credential,
            bucket=bucket,
            csv=csv,
            file_format=file_format,
            file_pattern=file_pattern,
            schedule=schedule,
            jtd_schema=jtd_schema,
        )

        self.prefix = prefix

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "prefix",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            "bucket": self.bucket,
            "prefix": self.prefix,
            "file_pattern": self.file_pattern,
            "file_format": self.file_format,
            "csv": self._csv_parser_input(),
        }


class GcpStorageSource(ObjectStorageSource):
    """
    An GCS source configuration.

    https://docs.validio.io/docs/gcs
    """

    def __init__(
        self,
        name: str,
        credential: GcpCredential,
        project: str,
        bucket: str,
        folder: str,
        file_pattern: str | None,
        schedule: str,
        csv: CsvParserConfig | None = None,
        file_format: FileFormat | None = None,
        jtd_schema: JsonTypeDefinition | None = None,
    ):
        """
        Constructor.

        :param project: Name of GCP project where the bucket resides.
        :param bucket: Name of the bucket to ingest files from.
        :param folder: Name of a folder within the bucket, to ingest files from.
        """
        super().__init__(
            name=name,
            credential=credential,
            bucket=bucket,
            csv=csv,
            file_format=file_format,
            file_pattern=file_pattern,
            schedule=schedule,
            jtd_schema=jtd_schema,
        )

        self.project = project
        self.folder = folder

    def _immutable_fields(self) -> set[str]:
        return {
            *super()._immutable_fields(),
            *{
                "project",
                "folder",
            },
        }

    def _api_infer_schema_input(self) -> dict[str, object] | None:
        return {
            "project": self.project,
            "bucket": self.bucket,
            "folder": self.folder,
            "file_pattern": self.file_pattern,
            "file_format": self.file_format,
            "csv": self._csv_parser_input(),
        }
