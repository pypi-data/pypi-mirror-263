from datetime import datetime
from typing import Annotated, List, Literal, Optional, Union

from pydantic import Field

from validio_sdk.scalars import CredentialId

from .base_model import BaseModel
from .fragments import CredentialBase


class ListCredentials(BaseModel):
    credentials_list: List[
        Annotated[
            Union[
                "ListCredentialsCredentialsListCredential",
                "ListCredentialsCredentialsListAwsAthenaCredential",
                "ListCredentialsCredentialsListAwsCredential",
                "ListCredentialsCredentialsListAwsRedshiftCredential",
                "ListCredentialsCredentialsListAzureSynapseEntraIdCredential",
                "ListCredentialsCredentialsListAzureSynapseSqlCredential",
                "ListCredentialsCredentialsListDatabricksCredential",
                "ListCredentialsCredentialsListDbtCloudCredential",
                "ListCredentialsCredentialsListDbtCoreCredential",
                "ListCredentialsCredentialsListKafkaSaslSslPlainCredential",
                "ListCredentialsCredentialsListKafkaSslCredential",
                "ListCredentialsCredentialsListLookerCredential",
                "ListCredentialsCredentialsListPostgreSqlCredential",
                "ListCredentialsCredentialsListSnowflakeCredential",
                "ListCredentialsCredentialsListTableauConnectedAppCredential",
                "ListCredentialsCredentialsListTableauPersonalAccessTokenCredential",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="credentialsList")


class ListCredentialsCredentialsListCredential(BaseModel):
    typename__: Literal["Credential", "DemoCredential", "GcpCredential"] = Field(
        alias="__typename"
    )
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListCredentialStats"


class ListCredentialsCredentialsListCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListAwsAthenaCredential(BaseModel):
    typename__: Literal["AwsAthenaCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListAwsAthenaCredentialStats"
    config: "ListCredentialsCredentialsListAwsAthenaCredentialConfig"


class ListCredentialsCredentialsListAwsAthenaCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListAwsAthenaCredentialConfig(BaseModel):
    access_key: str = Field(alias="accessKey")
    region: str
    query_result_location: str = Field(alias="queryResultLocation")


class ListCredentialsCredentialsListAwsCredential(BaseModel):
    typename__: Literal["AwsCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListAwsCredentialStats"
    config: "ListCredentialsCredentialsListAwsCredentialConfig"


class ListCredentialsCredentialsListAwsCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListAwsCredentialConfig(BaseModel):
    access_key: str = Field(alias="accessKey")


class ListCredentialsCredentialsListAwsRedshiftCredential(BaseModel):
    typename__: Literal["AwsRedshiftCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListAwsRedshiftCredentialStats"
    config: "ListCredentialsCredentialsListAwsRedshiftCredentialConfig"


class ListCredentialsCredentialsListAwsRedshiftCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListAwsRedshiftCredentialConfig(BaseModel):
    host: str
    port: int
    user: str
    default_database: str = Field(alias="defaultDatabase")


class ListCredentialsCredentialsListAzureSynapseEntraIdCredential(BaseModel):
    typename__: Literal["AzureSynapseEntraIdCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListAzureSynapseEntraIdCredentialStats"
    config: "ListCredentialsCredentialsListAzureSynapseEntraIdCredentialConfig"


class ListCredentialsCredentialsListAzureSynapseEntraIdCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListAzureSynapseEntraIdCredentialConfig(BaseModel):
    client_id: str = Field(alias="clientId")
    host: str
    port: int
    database: Optional[str]


class ListCredentialsCredentialsListAzureSynapseSqlCredential(BaseModel):
    typename__: Literal["AzureSynapseSqlCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListAzureSynapseSqlCredentialStats"
    config: "ListCredentialsCredentialsListAzureSynapseSqlCredentialConfig"


class ListCredentialsCredentialsListAzureSynapseSqlCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListAzureSynapseSqlCredentialConfig(BaseModel):
    username: str
    host: str
    port: int
    database: Optional[str]


class ListCredentialsCredentialsListDatabricksCredential(BaseModel):
    typename__: Literal["DatabricksCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListDatabricksCredentialStats"
    config: "ListCredentialsCredentialsListDatabricksCredentialConfig"


class ListCredentialsCredentialsListDatabricksCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListDatabricksCredentialConfig(BaseModel):
    host: str
    port: int
    http_path: str = Field(alias="httpPath")


class ListCredentialsCredentialsListDbtCloudCredential(BaseModel):
    typename__: Literal["DbtCloudCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListDbtCloudCredentialStats"
    config: "ListCredentialsCredentialsListDbtCloudCredentialConfig"


class ListCredentialsCredentialsListDbtCloudCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListDbtCloudCredentialConfig(BaseModel):
    warehouse_credential: "ListCredentialsCredentialsListDbtCloudCredentialConfigWarehouseCredential" = Field(
        alias="warehouseCredential"
    )
    account_id: str = Field(alias="accountId")
    api_base_url: Optional[str] = Field(alias="apiBaseUrl")


class ListCredentialsCredentialsListDbtCloudCredentialConfigWarehouseCredential(
    CredentialBase
):
    pass


class ListCredentialsCredentialsListDbtCoreCredential(BaseModel):
    typename__: Literal["DbtCoreCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListDbtCoreCredentialStats"
    config: "ListCredentialsCredentialsListDbtCoreCredentialConfig"


class ListCredentialsCredentialsListDbtCoreCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListDbtCoreCredentialConfig(BaseModel):
    warehouse_credential: "ListCredentialsCredentialsListDbtCoreCredentialConfigWarehouseCredential" = Field(
        alias="warehouseCredential"
    )


class ListCredentialsCredentialsListDbtCoreCredentialConfigWarehouseCredential(
    CredentialBase
):
    pass


class ListCredentialsCredentialsListKafkaSaslSslPlainCredential(BaseModel):
    typename__: Literal["KafkaSaslSslPlainCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListKafkaSaslSslPlainCredentialStats"
    config: "ListCredentialsCredentialsListKafkaSaslSslPlainCredentialConfig"


class ListCredentialsCredentialsListKafkaSaslSslPlainCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListKafkaSaslSslPlainCredentialConfig(BaseModel):
    bootstrap_servers: List[str] = Field(alias="bootstrapServers")
    username: str


class ListCredentialsCredentialsListKafkaSslCredential(BaseModel):
    typename__: Literal["KafkaSslCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListKafkaSslCredentialStats"
    config: "ListCredentialsCredentialsListKafkaSslCredentialConfig"


class ListCredentialsCredentialsListKafkaSslCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListKafkaSslCredentialConfig(BaseModel):
    bootstrap_servers: List[str] = Field(alias="bootstrapServers")
    ca_certificate: str = Field(alias="caCertificate")


class ListCredentialsCredentialsListLookerCredential(BaseModel):
    typename__: Literal["LookerCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListLookerCredentialStats"
    config: "ListCredentialsCredentialsListLookerCredentialConfig"


class ListCredentialsCredentialsListLookerCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListLookerCredentialConfig(BaseModel):
    base_url: str = Field(alias="baseUrl")
    client_id: str = Field(alias="clientId")


class ListCredentialsCredentialsListPostgreSqlCredential(BaseModel):
    typename__: Literal["PostgreSqlCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListPostgreSqlCredentialStats"
    config: "ListCredentialsCredentialsListPostgreSqlCredentialConfig"


class ListCredentialsCredentialsListPostgreSqlCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListPostgreSqlCredentialConfig(BaseModel):
    host: str
    port: int
    user: str
    default_database: str = Field(alias="defaultDatabase")


class ListCredentialsCredentialsListSnowflakeCredential(BaseModel):
    typename__: Literal["SnowflakeCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListSnowflakeCredentialStats"
    config: "ListCredentialsCredentialsListSnowflakeCredentialConfig"


class ListCredentialsCredentialsListSnowflakeCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListSnowflakeCredentialConfig(BaseModel):
    account: str
    user: str
    role: Optional[str]
    warehouse: Optional[str]


class ListCredentialsCredentialsListTableauConnectedAppCredential(BaseModel):
    typename__: Literal["TableauConnectedAppCredential"] = Field(alias="__typename")
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListTableauConnectedAppCredentialStats"
    config: "ListCredentialsCredentialsListTableauConnectedAppCredentialConfig"


class ListCredentialsCredentialsListTableauConnectedAppCredentialStats(BaseModel):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListTableauConnectedAppCredentialConfig(BaseModel):
    host: str
    site: str
    user: str
    client_id: str = Field(alias="clientId")
    secret_id: str = Field(alias="secretId")


class ListCredentialsCredentialsListTableauPersonalAccessTokenCredential(BaseModel):
    typename__: Literal["TableauPersonalAccessTokenCredential"] = Field(
        alias="__typename"
    )
    id: CredentialId
    name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_name: str = Field(alias="resourceName")
    resource_namespace: str = Field(alias="resourceNamespace")
    stats: "ListCredentialsCredentialsListTableauPersonalAccessTokenCredentialStats"
    config: "ListCredentialsCredentialsListTableauPersonalAccessTokenCredentialConfig"


class ListCredentialsCredentialsListTableauPersonalAccessTokenCredentialStats(
    BaseModel
):
    source_count: int = Field(alias="sourceCount")
    catalog_asset_count: int = Field(alias="catalogAssetCount")


class ListCredentialsCredentialsListTableauPersonalAccessTokenCredentialConfig(
    BaseModel
):
    host: str
    site: str
    token_name: str = Field(alias="tokenName")


ListCredentials.model_rebuild()
ListCredentialsCredentialsListCredential.model_rebuild()
ListCredentialsCredentialsListCredentialStats.model_rebuild()
ListCredentialsCredentialsListAwsAthenaCredential.model_rebuild()
ListCredentialsCredentialsListAwsAthenaCredentialStats.model_rebuild()
ListCredentialsCredentialsListAwsAthenaCredentialConfig.model_rebuild()
ListCredentialsCredentialsListAwsCredential.model_rebuild()
ListCredentialsCredentialsListAwsCredentialStats.model_rebuild()
ListCredentialsCredentialsListAwsCredentialConfig.model_rebuild()
ListCredentialsCredentialsListAwsRedshiftCredential.model_rebuild()
ListCredentialsCredentialsListAwsRedshiftCredentialStats.model_rebuild()
ListCredentialsCredentialsListAwsRedshiftCredentialConfig.model_rebuild()
ListCredentialsCredentialsListAzureSynapseEntraIdCredential.model_rebuild()
ListCredentialsCredentialsListAzureSynapseEntraIdCredentialStats.model_rebuild()
ListCredentialsCredentialsListAzureSynapseEntraIdCredentialConfig.model_rebuild()
ListCredentialsCredentialsListAzureSynapseSqlCredential.model_rebuild()
ListCredentialsCredentialsListAzureSynapseSqlCredentialStats.model_rebuild()
ListCredentialsCredentialsListAzureSynapseSqlCredentialConfig.model_rebuild()
ListCredentialsCredentialsListDatabricksCredential.model_rebuild()
ListCredentialsCredentialsListDatabricksCredentialStats.model_rebuild()
ListCredentialsCredentialsListDatabricksCredentialConfig.model_rebuild()
ListCredentialsCredentialsListDbtCloudCredential.model_rebuild()
ListCredentialsCredentialsListDbtCloudCredentialStats.model_rebuild()
ListCredentialsCredentialsListDbtCloudCredentialConfig.model_rebuild()
ListCredentialsCredentialsListDbtCloudCredentialConfigWarehouseCredential.model_rebuild()
ListCredentialsCredentialsListDbtCoreCredential.model_rebuild()
ListCredentialsCredentialsListDbtCoreCredentialStats.model_rebuild()
ListCredentialsCredentialsListDbtCoreCredentialConfig.model_rebuild()
ListCredentialsCredentialsListDbtCoreCredentialConfigWarehouseCredential.model_rebuild()
ListCredentialsCredentialsListKafkaSaslSslPlainCredential.model_rebuild()
ListCredentialsCredentialsListKafkaSaslSslPlainCredentialStats.model_rebuild()
ListCredentialsCredentialsListKafkaSaslSslPlainCredentialConfig.model_rebuild()
ListCredentialsCredentialsListKafkaSslCredential.model_rebuild()
ListCredentialsCredentialsListKafkaSslCredentialStats.model_rebuild()
ListCredentialsCredentialsListKafkaSslCredentialConfig.model_rebuild()
ListCredentialsCredentialsListLookerCredential.model_rebuild()
ListCredentialsCredentialsListLookerCredentialStats.model_rebuild()
ListCredentialsCredentialsListLookerCredentialConfig.model_rebuild()
ListCredentialsCredentialsListPostgreSqlCredential.model_rebuild()
ListCredentialsCredentialsListPostgreSqlCredentialStats.model_rebuild()
ListCredentialsCredentialsListPostgreSqlCredentialConfig.model_rebuild()
ListCredentialsCredentialsListSnowflakeCredential.model_rebuild()
ListCredentialsCredentialsListSnowflakeCredentialStats.model_rebuild()
ListCredentialsCredentialsListSnowflakeCredentialConfig.model_rebuild()
ListCredentialsCredentialsListTableauConnectedAppCredential.model_rebuild()
ListCredentialsCredentialsListTableauConnectedAppCredentialStats.model_rebuild()
ListCredentialsCredentialsListTableauConnectedAppCredentialConfig.model_rebuild()
ListCredentialsCredentialsListTableauPersonalAccessTokenCredential.model_rebuild()
ListCredentialsCredentialsListTableauPersonalAccessTokenCredentialStats.model_rebuild()
ListCredentialsCredentialsListTableauPersonalAccessTokenCredentialConfig.model_rebuild()
