from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  AWS_PROFILE_NAME: str = ""

  S3_BUCKET_NAME: str = "mediq-dev"
  S3_OBJECT_PREFIX: str = "pdf-parsing"

  RESPONSE_TOPIC_ARN: str = "arn:aws:sns:us-east-1:284584416663:public_test"
  RESPONSE_SQS_URL: str  = "https://sqs.us-east-1.amazonaws.com/284584416663/public_test"

  PDF_PARSING_TOPIC_ARN: str = "arn:aws:sns:us-east-1:284584416663:mediq-prod-pdf-parsing"
  GPTCHAT_TOPIC_ARN: str = "arn:aws:sns:us-east-1:284584416663:mediq-prod-openai-chat"

settings = Settings()