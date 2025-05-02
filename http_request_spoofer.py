"""
Simple HTTP Request Spoofer

This script allows you to send HTTP requests with customizable headers
to a specified URL and view the response.

Usage:
    Run this script and follow the prompts to enter the target URL and headers.
"""

import requests

def get_custom_headers():
    print("Enter custom headers you want to spoof. Leave header name empty to finish.")
    headers = {}
    while True:
        name = input("Header name: ").strip()
        if not name:
            break
        value = input(f"Value for '{name}': ").strip()
        headers[name] = value
    return headers

def main():
    print("=== Simple HTTP Request Spoofer ===")
    url = input("Enter the target URL (including http:// or https://): ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Invalid URL format. Please include 'http://' or 'https://'. Exiting.")
        return

    headers = get_custom_headers()
    if not headers:
        print("No custom headers provided. Sending request with default headers.")

    try:
        print("\nSending request...")
        response = requests.get(url, headers=headers)
        print(f"Response Status Code: {response.status_code}")
        print("Response Headers:")
        for k, v in response.headers.items():
            print(f"  {k}: {v}")

        # Display first 500 characters of response body
        content_preview = response.text[:500]
        print("\nResponse Content Preview (first 500 characters):")
        print(content_preview)

        # Optionally save full response to file
        save = input("\nSave full response content to a file? (y/n): ").strip().lower()
        if save == 'y':
            filename = input("Enter filename to save response content (default: response.txt): ").strip()
            if not filename:
                filename = "response.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Response content saved to {filename}")

        print("\nRequest completed successfully.")

    except requests.RequestException as e:
        print(f"Error sending request: {e}")

if __name__ == "__main__":
    main()
