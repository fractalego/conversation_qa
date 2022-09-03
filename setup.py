from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="conversation-qa",
    version="0.0.9",
    url="http://github.com/fractalego/conversation_qa",
    author="Alberto Cetoli",
    author_email="alberto@fractalego.io",
    description="Conversational QA.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        "conversation_qa",
    ],
    install_requires=[
        "transformers==4.17.0",
        "sentence_transformers==2.0.0",
        "torch==1.9.0",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
    zip_safe=False,
)
