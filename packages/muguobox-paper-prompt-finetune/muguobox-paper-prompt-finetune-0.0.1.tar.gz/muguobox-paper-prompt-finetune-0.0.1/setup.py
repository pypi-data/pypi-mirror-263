from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fp:
  long_description = fp.read()

setup(
  name='muguobox-paper-prompt-finetune',
  version='0.0.1',
  description="A muguo toolkit for finetuning AIGC prompts",
  long_description=long_description,
  long_description_content_type="text/markdown",
  package_dir={"": "src"},
  packages=find_namespace_packages(
    where="src", include=["muguobox.*"]
  ),
  install_requires=[
    "snqueue",
    "pydantic-settings",
    "mediqbox-download",
    "mediqbox-gptchat",
  ]
)