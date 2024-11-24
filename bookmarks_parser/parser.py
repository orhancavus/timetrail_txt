import json
from typing import List, Dict
from bs4 import BeautifulSoup


def parse_bookmarks(file_path: str) -> List[Dict[str, str]]:
    """
    Parses a bookmarks file and extracts the URLs and metadata.
    Supports both JSON and HTML-formatted bookmark files.

    :param file_path: Path to the bookmarks file
    :return: List of dictionaries with keys 'url' and 'title'
    """
    if file_path.endswith(".json"):
        return _parse_json_bookmarks(file_path)
    elif file_path.endswith(".html"):
        return _parse_html_bookmarks(file_path)
    else:
        raise ValueError("Unsupported file format. Only JSON and HTML are supported.")


def _parse_json_bookmarks(file_path: str) -> List[Dict[str, str]]:
    """
    Parses a JSON-formatted bookmarks file.

    :param file_path: Path to the JSON bookmarks file
    :return: List of dictionaries with keys 'url' and 'title'
    """
    with open(file_path, "r") as file:
        data = json.load(file)

    bookmarks = []
    for item in data.get("bookmarks", []):
        bookmarks.append(
            {"url": item.get("url"), "title": item.get("title", "No Title")}
        )
    return bookmarks


def _parse_html_bookmarks(file_path: str) -> List[Dict[str, str]]:
    """
    Parses an HTML-formatted bookmarks file.

    :param file_path: Path to the HTML bookmarks file
    :return: List of dictionaries with keys 'url' and 'title'
    """
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    bookmarks = []
    for anchor in soup.find_all("a"):
        url = anchor.get("href")
        title = anchor.text.strip()
        if url:  # Ensure the link is valid
            bookmarks.append({"url": url, "title": title if title else "No Title"})
    return bookmarks
