# Travel In Time with Bookmarks

Author : Orhan Cavus

This Python program processes a collection of web bookmarks, extracts the content from each URL, and generates a concise summary using a local Large Language Model (LLM) served via Ollama. The application is designed for users who wish to revisit their saved bookmarks and gain quick insights into the content.

## Features

- Parses bookmarks from an HTML file (e.g., exported browser favorites).
- Extracts raw text content from the specified URLs.
- Summarizes content using a REST API connected to a local LLM service.
- Logs the processing details for debugging and monitoring.

## Requirements

- Python 3.8 or higher.
- A locally running LLM service served by **Ollama** at `http://localhost:11434/api/generate`.
- An exported bookmarks HTML file (e.g., `bookmarks.html`).

## Setup

1. **Install Dependencies**:
   - Create a virtual environment and activate it:

     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

   - Install the required Python libraries:

     ```bash
     pip install -r requirements.txt
     ```

2. **Prepare the Bookmarks File**:
   - Place your exported bookmarks HTML file in the project root directory.
   - Ensure the file is named `bookmarks.html` (or update the `BOOKMARKS_FILE` constant in `main.py`).

3. **Run Ollama LLM Service**:
   - Ensure Ollama is installed and running locally.
   - Start the service using:

     ```bash
     ollama serve
     ```

## Usage

Run the application as follows:

```bash
python main.py
