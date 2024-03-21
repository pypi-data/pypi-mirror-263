import hashlib

from snqueue.boto3_clients import S3Client

from muguobox.paper_prompt_finetune.settings import settings

def sha256sum(filename: str) -> str:
  with open(filename, 'rb', buffering=0) as f:
    return hashlib.file_digest(f, 'sha256').hexdigest()
  
def hash2path(hashcode: str) -> str:
  return f"{'/'.join(hashcode[i:i+2] for i in range(0,6,2))}/{hashcode[6:]}"

def upload_to_s3(
    local_file: str,
    target_filename: str,
    hashcode: str
) -> tuple[str, str]:
  # Constructs S3 object key
  object_key = f"{settings.S3_OBJECT_PREFIX}/{hash2path(hashcode)}/{target_filename}"

  with S3Client(settings.AWS_PROFILE_NAME) as s3:
    with open(local_file, 'rb') as fp:
      s3.client.upload_fileobj(fp, settings.S3_BUCKET_NAME, object_key)

  return settings.S3_BUCKET_NAME, object_key