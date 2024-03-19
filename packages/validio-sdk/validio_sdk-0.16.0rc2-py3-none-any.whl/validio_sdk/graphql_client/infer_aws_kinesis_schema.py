from pydantic import Field

from validio_sdk.scalars import JsonTypeDefinition

from .base_model import BaseModel


class InferAwsKinesisSchema(BaseModel):
    aws_kinesis_infer_schema: JsonTypeDefinition = Field(alias="awsKinesisInferSchema")


InferAwsKinesisSchema.model_rebuild()
