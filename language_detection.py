from dotenv import load_dotenv
import http.client
import json
import os
from typing import Dict, Any

# env var file constants
CONFIG_ENDPOINT = 'COGNITIVE_SERVICES_ENDPOINT'
CONFIG_PATH = 'LANGUAGE_DETECTION_PATH'
CONFIG_KEY = 'COGNITIVE_SERVICES_KEY'


def load_config() -> Dict[str, str]:
    """Load configuration settings from env var file."""

    load_dotenv()

    config = {
        "endpoint": os.getenv(CONFIG_ENDPOINT),
        "path": os.getenv(CONFIG_PATH),
        "key": os.getenv(CONFIG_KEY),
    }

    if not all(config.values()):
        raise ValueError("Missing configuration settings. Please check your .env file.")
    
    return config


def detect_language(prompt: str, endpoint: str, path: str, key: str) -> None:
    """Analyze the sentiment of the given text using the Text Analytics API."""

    try:
        # JSON request body expects a document list, but only one item here for demo purposes
        json_body = {
            "documents": [
                {
                    "id": 1,
                    "text": prompt
                }
            ]
        }

        print("\nRequest:\n", json.dumps(json_body, indent=2))

        # make a REST call to the Text Analytics API resource for sentiment analysis, and include the API key in the header
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': key
        }
        conn = http.client.HTTPSConnection(endpoint)
        conn.request("POST", path, json.dumps(json_body).encode('utf-8'), headers)

        # get the response and display results if successful
        response = conn.getresponse()
        data = response.read().decode("UTF-8")

        if response.status == 200:
            results = json.loads(data)
            print("\nResponse:\n", json.dumps(results, indent=2))

            for document in results["documents"]:
                print("\nLanguage:", document["detectedLanguage"]["name"], "\n")
        else:
            print(f"Error: {response.status} - {data}")

        conn.close()

    except Exception as ex:
        print(f"An error occurred during language detection: {ex}")


def main() -> None:
    """Main function to gather input text from the user and detect its language."""

    try:
        config = load_config()
        endpoint = config["endpoint"].rstrip('/').replace('https://', '')
        path = config["path"]
        key = config["key"]

        while True:
            prompt = input('Enter some text to detect its language. Enter q to quit.\n\n')
            if prompt.lower() == 'q':
                break
            detect_language(prompt, endpoint, path, key)

    except ValueError as ve:
        print(f"Configuration error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    main()
