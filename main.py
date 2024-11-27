import re
from bookmarks_parser.parser import parse_bookmarks
from content_extractor.extractor import extract_content
from summarizer.content_summarizer import summarize_content
from utils.logging_config import setup_logging


# Configuration
BOOKMARKS_FILE = "bookmarks.html"  # Path to your bookmarks file
LLM_SERVICE_URL = "http://localhost:11434/api/generate"  # REST service URL


def remove_consecutive_spaces(text: str) -> str:
    """
    Removes consecutive spaces in a given text string.

    Args:
        text (str): The input text string.

    Returns:
        str: The text string with single spaces.
    """
    return re.sub(r"\s+", " ", text).strip()


def process_bookmark(bookmark: dict) -> str:
    """
    Processes a single bookmark: extracts content and summarizes it.

    Args:
        bookmark (dict): A bookmark with 'url' and 'title' keys.

    Returns:
        str: Summary of the bookmark content or an error message.
    """
    url = bookmark.get("url")
    title = remove_consecutive_spaces(bookmark.get("title", "Untitled"))

    print(f"\nProcessing Title : {title}")
    print(f"Processing URL   : {url}")

    # Step 1: Extract content
    content = extract_content(url)
    if content.startswith("Error"):
        print("Content Extraction Failed!")
        return f"Error: Could not extract content from {url}"

    # Step 2: Summarize content
    summary = summarize_content(
        content=content, client_type="ollama", service_url=LLM_SERVICE_URL
    )
    return summary


def main():
    # start ollama before using thsi program
    print("\n\n--- Travel In Time with Bookmarks ---")
    logger = setup_logging()

    logger.info("Processing bookmark - start ollama before using this program")
    # Step 1: Parse bookmarks
    bookmarks = parse_bookmarks(BOOKMARKS_FILE)
    logger.info("Bookmarks parsed")
    if not bookmarks:
        print("No bookmarks found! Please check your bookmarks file.")
        return

    print(f"Found {len(bookmarks)} bookmarks. Processing...\n")

    logger.info("Start Bookmark processing with local LLM served with ollama")

    # Step 2: Process each bookmark
    for idx, bookmark in enumerate(bookmarks, start=1):
        print(f"Bookmark {idx}/{len(bookmarks)}")
        summary = process_bookmark(bookmark)
        print(f"Summary          : {summary}")
        print("=" * 120)
    logger.info("Bookmark processing ended .. ")

    print("\nDone! All bookmarks processed.")


if __name__ == "__main__":
    main()
