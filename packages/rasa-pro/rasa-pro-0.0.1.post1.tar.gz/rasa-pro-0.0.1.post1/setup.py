from setuptools import setup
import os

# Get the long description from the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rasa-pro",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        # supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
    version="0.0.1post1",
    description="Rasa Pro package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rasa Technologies GmbH",
    author_email="hi@rasa.com",
    maintainer="Tom Bocklisch",
    maintainer_email="tom@rasa.com",
    license="Apache 2.0",
    keywords="nlp machine-learning machine-learning-library bot bots "
             "botkit rasa conversational-agents conversational-ai chatbot"
             "chatbot-framework bot-framework",
    url="https://rasa.com",
    project_urls={
        "Bug Reports": "https://github.com/rasahq/rasa/issues",
        "Source": "https://github.com/rasahq/rasa",
    },
)

if not os.getenv("OVERRIDE"):
    raise RuntimeError('You are installing rasa-pro from pypi.org, which will not work. Please make sure you are installing from the Rasa python package registry. More information can be found at https://rasa.com/docs/rasa-pro/installation/python/installation')
