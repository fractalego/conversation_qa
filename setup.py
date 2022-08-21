from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="conversation_qa",
    version="0.0.1",
    url="http://github.com/fractalego/conversation_qa",
    author="Alberto Cetoli",
    author_email="alberto@fractalego.io",
    description="Conversational QA.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        "conversation_qa",
        "conversation_qa.__init__",
        "conversation_qa.qa",
        "conversation_qa.utils",
    ],
    install_requires=[
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
    zip_safe=False,
)
