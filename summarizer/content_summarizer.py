import ollama
import requests
import json


def summarize_content(content: str, client_type: str, service_url: str = None) -> str:
    """
    Summarizes the provided content using either the Ollama client or a REST API.

    Args:
        content (str): The raw text content to be summarized.
        client_type (str): The client type to use ('ollama' or 'rest').
        service_url (str, optional): URL of the REST service (required for 'rest' client type).

    Returns:
        str: The summary of the content as a JSON string.
    """
    # Define shared prompts
    system_prompt = f"Only use the following information to answer the question. Do not use anything else: {content}"
    prompt = (
        "Summary the following content briefly in a maximum of 20 words. "
        "Respond in JSON with two fields: "
        "'summary' (the summary of the content) and "
        "'category' (describing the category of the content)."
    )

    if client_type == "ollama":
        try:
            response = ollama.generate(
                model="llama3.2",
                prompt=prompt,
                system=system_prompt,
                format="json",
                stream=False,
            )
            return response.get("response", "Error: No response from Ollama")
        except Exception as e:
            return f"Error: Failed to call Ollama service. Details: {e}"
    elif client_type == "rest":
        if not service_url:
            return "Error: 'service_url' is required for REST client type."

        payload = {
            "model": "llama3.2",
            "system": system_prompt,
            "prompt": prompt,
            "format": "json",
            "stream": False,
        }

        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(service_url, json=payload, headers=headers)
            if response.status_code == 200:
                return json.loads(response.text).get(
                    "response", "Error: No response from REST service"
                )
            else:
                return (
                    f"Error: REST service returned status code {response.status_code}"
                )
        except requests.RequestException as e:
            return f"Error: Failed to connect to REST service. Details: {e}"

    else:
        return "Error: Invalid client type. Choose 'ollama' or 'rest'."
