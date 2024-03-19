from datetime import datetime
from typing import Annotated, List, Literal, Optional, Union

from pydantic import Field

from validio_sdk.scalars import CredentialId

from .base_model import BaseModel
from .fragments import CredentialBase


class GetCredentialByResourceName(BaseModel):
    credential_by_resource_name: Optional[
        Annotated[
            Union[
                "GetCredentialByResourceNameCredentialByResourceNameCredential",
                "GetCredentialByResourceNameCredentialByResourceNameAwsAthenaCredential",
                "GetCredentialByResourceNameCredentialByResourceNameAwsCredential",
                "GetCredentialByResourceNameCredentialByResourceNameAwsRedshiftCredential",
                "GetCredentialByResourceNameCredentialByResourceNameAzureSynapseEntraIdCredential",
                "GetCredentialByResourceNameCredentialByResourceNameAzureSynapseSqlCredential",
                "GetCredentialByResourceNameCredentialByResourceNameDatabricksCredential",
                "GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredential",
                "GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredential",
                "GetCredentialByResourceNameCredentialByResourceNameKafkaSaslSslPlainCredential",
                "GetCredentialByResourceNameCredentialByResourceNameKafkaSslCredential",
                "GetCredentialByResourceNameCredentialByResourceNameLookerCredential",
                "GetCredentialByResourceNameCredentialByResourceNamePostgreSqlCredential",
                "GetCredentialByResourceNameCredentialByResourceNameSnowflakeCredential",
                "GetCredentialByResourceNameCredentialByResourceNameTableauConnectedAppCredential",
                "GetCredentialByResourceNameCredentialByResourceNameTableauPersonalAccessTokenCredential",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="credentialByResourceName")


class GetCredentialByResourceNameCredentialByResourceNameCredential(BaseModel):
    typename__: Literal["Credential", "DemoCredential", "GcpCredential"] = Field(
        alias="__typename"
    )
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameCredentialStats"


class GetCredentialByResourceNameCredentialByResourceNameCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameAwsAthenaCredential(BaseModel):
    typename__: Literal["AwsAthenaCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameAwsAthenaCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameAwsAthenaCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameAwsAthenaCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameAwsAthenaCredentialConfig(
    BaseModel
):
    access_key: str = Field(alias="accessKey")
    region: str
    query_result_location: str = Field(alias="queryResultLocation")


class GetCredentialByResourceNameCredentialByResourceNameAwsCredential(BaseModel):
    typename__: Literal["AwsCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameAwsCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameAwsCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameAwsCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameAwsCredentialConfig(BaseModel):
    access_key: str = Field(alias="accessKey")


class GetCredentialByResourceNameCredentialByResourceNameAwsRedshiftCredential(
    BaseModel
):
    typename__: Literal["AwsRedshiftCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameAwsRedshiftCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameAwsRedshiftCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameAwsRedshiftCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameAwsRedshiftCredentialConfig(
    BaseModel
):
    host: str
    port: int
    user: str
    default_database: str = Field(alias="defaultDatabase")


class GetCredentialByResourceNameCredentialByResourceNameAzureSynapseEntraIdCredential(
    BaseModel
):
    typename__: Literal["AzureSynapseEntraIdCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameAzureSynapseEntraIdCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameAzureSynapseEntraIdCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameAzureSynapseEntraIdCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameAzureSynapseEntraIdCredentialConfig(
    BaseModel
):
    client_id: str = Field(alias="clientId")
    host: str
    port: int
    database: Optional[str]


class GetCredentialByResourceNameCredentialByResourceNameAzureSynapseSqlCredential(
    BaseModel
):
    typename__: Literal["AzureSynapseSqlCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameAzureSynapseSqlCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameAzureSynapseSqlCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameAzureSynapseSqlCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameAzureSynapseSqlCredentialConfig(
    BaseModel
):
    username: str
    host: str
    port: int
    database: Optional[str]


class GetCredentialByResourceNameCredentialByResourceNameDatabricksCredential(
    BaseModel
):
    typename__: Literal["DatabricksCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameDatabricksCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameDatabricksCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameDatabricksCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameDatabricksCredentialConfig(
    BaseModel
):
    host: str
    port: int
    http_path: str = Field(alias="httpPath")


class GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredential(BaseModel):
    typename__: Literal["DbtCloudCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredentialConfig(
    BaseModel
):
    warehouse_credential: "GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredentialConfigWarehouseCredential" = Field(
        alias="warehouseCredential"
    )
    account_id: str = Field(alias="accountId")
    api_base_url: Optional[str] = Field(alias="apiBaseUrl")


class GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredentialConfigWarehouseCredential(
    CredentialBase
):
    pass


class GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredential(BaseModel):
    typename__: Literal["DbtCoreCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredentialConfig(
    BaseModel
):
    warehouse_credential: "GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredentialConfigWarehouseCredential" = Field(
        alias="warehouseCredential"
    )


class GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredentialConfigWarehouseCredential(
    CredentialBase
):
    pass


class GetCredentialByResourceNameCredentialByResourceNameKafkaSaslSslPlainCredential(
    BaseModel
):
    typename__: Literal["KafkaSaslSslPlainCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameKafkaSaslSslPlainCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameKafkaSaslSslPlainCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameKafkaSaslSslPlainCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameKafkaSaslSslPlainCredentialConfig(
    BaseModel
):
    bootstrap_servers: List[str] = Field(alias="bootstrapServers")
    username: str


class GetCredentialByResourceNameCredentialByResourceNameKafkaSslCredential(BaseModel):
    typename__: Literal["KafkaSslCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameKafkaSslCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameKafkaSslCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameKafkaSslCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameKafkaSslCredentialConfig(
    BaseModel
):
    bootstrap_servers: List[str] = Field(alias="bootstrapServers")
    ca_certificate: str = Field(alias="caCertificate")


class GetCredentialByResourceNameCredentialByResourceNameLookerCredential(BaseModel):
    typename__: Literal["LookerCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameLookerCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameLookerCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameLookerCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameLookerCredentialConfig(
    BaseModel
):
    base_url: str = Field(alias="baseUrl")
    client_id: str = Field(alias="clientId")


class GetCredentialByResourceNameCredentialByResourceNamePostgreSqlCredential(
    BaseModel
):
    typename__: Literal["PostgreSqlCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNamePostgreSqlCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNamePostgreSqlCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNamePostgreSqlCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNamePostgreSqlCredentialConfig(
    BaseModel
):
    host: str
    port: int
    user: str
    default_database: str = Field(alias="defaultDatabase")


class GetCredentialByResourceNameCredentialByResourceNameSnowflakeCredential(BaseModel):
    typename__: Literal["SnowflakeCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameSnowflakeCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameSnowflakeCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameSnowflakeCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameSnowflakeCredentialConfig(
    BaseModel
):
    account: str
    user: str
    role: Optional[str]
    warehouse: Optional[str]


class GetCredentialByResourceNameCredentialByResourceNameTableauConnectedAppCredential(
    BaseModel
):
    typename__: Literal["TableauConnectedAppCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameTableauConnectedAppCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameTableauConnectedAppCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameTableauConnectedAppCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameTableauConnectedAppCredentialConfig(
    BaseModel
):
    host: str
    site: str
    user: str
    client_id: str = Field(alias="clientId")
    secret_id: str = Field(alias="secretId")


class GetCredentialByResourceNameCredentialByResourceNameTableauPersonalAccessTokenCredential(
    BaseModel
):
    typename__: Literal["TableauPersonalAccessTokenCredential"] = Field(
        alias="__typename"
    )
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "GetCredentialByResourceNameCredentialByResourceNameTableauPersonalAccessTokenCredentialStats"
    config: "GetCredentialByResourceNameCredentialByResourceNameTableauPersonalAccessTokenCredentialConfig"


class GetCredentialByResourceNameCredentialByResourceNameTableauPersonalAccessTokenCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class GetCredentialByResourceNameCredentialByResourceNameTableauPersonalAccessTokenCredentialConfig(
    BaseModel
):
    host: str
    site: str
    token_name: str = Field(alias="tokenName")


GetCredentialByResourceName.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAwsAthenaCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAwsAthenaCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAwsAthenaCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAwsCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAwsCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAwsCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAwsRedshiftCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAwsRedshiftCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAwsRedshiftCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAzureSynapseEntraIdCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAzureSynapseEntraIdCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAzureSynapseEntraIdCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAzureSynapseSqlCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAzureSynapseSqlCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameAzureSynapseSqlCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDatabricksCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDatabricksCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDatabricksCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDbtCloudCredentialConfigWarehouseCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameDbtCoreCredentialConfigWarehouseCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameKafkaSaslSslPlainCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameKafkaSaslSslPlainCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameKafkaSaslSslPlainCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameKafkaSslCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameKafkaSslCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameKafkaSslCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameLookerCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameLookerCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameLookerCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNamePostgreSqlCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNamePostgreSqlCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNamePostgreSqlCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameSnowflakeCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameSnowflakeCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameSnowflakeCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameTableauConnectedAppCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameTableauConnectedAppCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameTableauConnectedAppCredentialConfig.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameTableauPersonalAccessTokenCredential.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameTableauPersonalAccessTokenCredentialStats.model_rebuild()
GetCredentialByResourceNameCredentialByResourceNameTableauPersonalAccessTokenCredentialConfig.model_rebuild()
