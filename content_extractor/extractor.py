import requests
from bs4 import BeautifulSoup


def extract_content_old(url: str) -> str:
    """
    Fetches the content of a given URL.

    :param url: Web page URL
    :return: Raw text content of the page
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Error fetching content from {url}: {e}"


def extract_content(url: str) -> str:
    """
    Fetches and extracts the plain text content of a given URL.

    :param url: Web page URL
    :return: Plain text content of the page
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract and return the plain text
        return soup.get_text(strip=True)
    except requests.RequestException as e:
        return f"Error fetching content from {url}: {e}"


# Example usage
if __name__ == "__main__":
    url = "https://thecleverprogrammer.com/2021/06/22/r2-score-in-machine-learning/"
    print(extract_content_old(url))
