# azure-ai-services-demo

This repository provides sample Python code for making REST calls to the [Language Service API for Azure AI Services](https://learn.microsoft.com/en-us/azure/ai-services/language-service/).

### Prerequisites

[Python](https://www.python.org/) 3.8 or later

[python-dotenv](https://pypi.org/project/python-dotenv/) library

[Azure Language Service](https://learn.microsoft.com/en-us/azure/ai-services/language-service/language-detection/quickstart?tabs=macos&pivots=programming-language-python) configured in Azure

### Setup

- Clone the repo:  `git clone https://github.com/doitintl/azure-ai-services-demo.git`
- Install library for reading environment variables file .env:  `pip install python-dotenv`
- Modify .env file to use your Azure Language Service Key and Endpoint.
- Execute one of the python files where you will be prompted to provide text to be analyzed:  `python <filename>`

