from pydantic import Field

from validio_sdk.scalars import JsonTypeDefinition

from .base_model import BaseModel


class InferSnowflakeSchema(BaseModel):
    snowflake_infer_schema: JsonTypeDefinition = Field(alias="snowflakeInferSchema")


InferSnowflakeSchema.model_rebuild()
