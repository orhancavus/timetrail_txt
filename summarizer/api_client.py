import ollama


def summarize_content(content: str) -> str:

    systemPrompt = f"Only use the following information to answer the question. Do not use anything else: {content}"

    prompt = f"""Summary the following content birefly in maximum of 20 words in your response include just the answer no extra explanation, Respond in JSON with two fields first field : summary
        second field category describing the category of the content"""

    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        system=systemPrompt,
        format="json",
        stream=False,
    )
    return response["response"]


cont = """
Use macOS Recovery on an Intel-based Mac
macOS Recovery is the built-in recovery system on your Mac.

You can use the apps in macOS Recovery on an Intel-based Mac to repair your computer’s internal storage device, reinstall macOS, restore your files from a Time Machine backup, set security options, and more.

Reinstalling macOS requires an internet connection. To connect to the internet, you can use a wireless or wired network connection. If you’re trying to connect to Wi-Fi through a captive portal (for example, at a coffee shop, library, or hotel) or an enterprise network, you might not be able to access the internet in macOS Recovery. See Connect to the internet using Wi-Fi.
"""

if __name__ == "__main__":
    print("\n")
    # cont = "Explain prime numbers"
    summary = summarize_content(cont)
    print(f"\nSummary : {summary}")
