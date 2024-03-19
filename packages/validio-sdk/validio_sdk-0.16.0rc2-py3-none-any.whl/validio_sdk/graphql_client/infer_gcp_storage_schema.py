from pydantic import Field

from validio_sdk.scalars import JsonTypeDefinition

from .base_model import BaseModel


class InferGcpStorageSchema(BaseModel):
    gcp_storage_infer_schema: JsonTypeDefinition = Field(alias="gcpStorageInferSchema")


InferGcpStorageSchema.model_rebuild()
