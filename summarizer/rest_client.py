import requests
import json
from utils.timing import timing_decorator

"""
def summarize_content_langchaing(content: str, service_url: str) -> str:

    ollama = Ollama(base_url="http://localhost:11434", model="llama3.2")

    return ollama("# A simple python function to remove whitespace from a string:")
"""


# @timing_decorator
def summarize_content(content: str, service_url: str) -> str:
    """
    Sends the content to the LLM REST service for summarization.

    :param content: The raw text content to be summarized
    :param service_url: URL of the REST service
    :return: Summary of the content
    """
    # Define the URL
    # url = "http://localhost:11434/api/generate"

    systemPrompt = f"Only use the following information to answer the question. Do not use anything else: {content}"
    prompt = f"Summary the following content birefly in maximum of 20 words in your response include just the answer no extra explanation"

    # Define the request payload as a dictionary
    payload = {
        "model": "llama3.2",
        "system": systemPrompt,
        "prompt": prompt,
        "stream": False,
    }

    # Convert the payload to JSON format
    payload_json = json.dumps(payload)

    # Define the headers
    headers = {"Content-Type": "application/json"}

    # Make the POST request
    response = requests.post(service_url, data=payload_json, headers=headers)

    a_response = json.loads(response.text)["response"]

    # Check the response status code
    if response.status_code == 200:
        return a_response
    else:
        return f"Request failed with status code {response.status_code}"


cont = """
Use macOS Recovery on an Intel-based Mac
macOS Recovery is the built-in recovery system on your Mac.

You can use the apps in macOS Recovery on an Intel-based Mac to repair your computer’s internal storage device, reinstall macOS, restore your files from a Time Machine backup, set security options, and more.

Reinstalling macOS requires an internet connection. To connect to the internet, you can use a wireless or wired network connection. If you’re trying to connect to Wi-Fi through a captive portal (for example, at a coffee shop, library, or hotel) or an enterprise network, you might not be able to access the internet in macOS Recovery. See Connect to the internet using Wi-Fi.
"""
url = "http://localhost:11434/api/generate"

if __name__ == "__main__":
    print("\n")
    # cont = "Explain prime numbers"
    summary = summarize_content(cont, url)
    print(f"\nUrl     : ({url}) \nSummary : {summary}")
