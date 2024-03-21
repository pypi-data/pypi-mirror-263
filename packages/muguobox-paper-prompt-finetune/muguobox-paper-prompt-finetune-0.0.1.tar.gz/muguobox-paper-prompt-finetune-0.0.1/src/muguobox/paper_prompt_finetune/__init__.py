import asyncio
import json
import shutil
import tempfile

from snqueue.service import SqsVirtualQueueClient
from snqueue.service.helper import parse_response

from mediqbox.abc.async2sync import Async2Sync
from mediqbox.download.download import *
from mediqbox.gptchat.chat import *

from muguobox.paper_prompt_finetune.utils import *

cfg = ChatConfig(
  aws_profile_name=settings.AWS_PROFILE_NAME,
  request_topic_arn=settings.GPTCHAT_TOPIC_ARN,
  response_topic_arn=settings.RESPONSE_TOPIC_ARN,
  response_sqs_url=settings.RESPONSE_SQS_URL
)
async_chat = Chat(cfg)
chat = Async2Sync(async_chat)

def parse_pdf(
    filename: str,
    output_dir: str
) -> dict[str, str]:
  print("Parsing pdf...")

  # Upload the pdf file to S3
  bucket_name, object_key = upload_to_s3(
    filename, "raw.pdf", sha256sum(filename)
  )
  with S3Client(settings.AWS_PROFILE_NAME) as s3:
    pdf_url = s3.create_presigned_get(bucket_name, object_key)

  # Request parsing
  client = SqsVirtualQueueClient(
    settings.RESPONSE_SQS_URL, settings.AWS_PROFILE_NAME)
  response = asyncio.run(client.request(
    settings.PDF_PARSING_TOPIC_ARN,
    { "pdf_url": pdf_url },
    response_topic_arn=settings.RESPONSE_TOPIC_ARN
  ))
  status, msg, _ = parse_response(response)
  assert status == 200

  print("Downloading results...")

  # Download results
  result = json.loads(msg)
  scipdf_url, loadpdf_url = result['scipdf']['url'], result['loadpdf']['url']

  with tempfile.TemporaryDirectory() as tmpdir:
    downloader = Download(DownloadConfig(target_dir=tmpdir))
    downloaded = asyncio.run(downloader.process(DownloadInputData(
      urls=[scipdf_url, loadpdf_url]
    )))

    text_file = os.path.join(output_dir, "texts.json")
    figure_file = os.path.join(output_dir, "figures.zip")

    shutil.copyfile(downloaded[0], text_file)
    shutil.copyfile(downloaded[1], figure_file)

  return {
    "text_file": text_file,
    "figure_file": figure_file
  }

def ask_gpt(
    prompt: str,
    content: str,
    model: str = "gpt-4"
) -> str:
  return json.loads(chat.process(ChatInputData(
    model=model,
    messages=[
      ChatMessage(role='system', content=prompt),
      ChatMessage(role='user', content=content)
    ]
  )))['choices'][0]['message']['content']