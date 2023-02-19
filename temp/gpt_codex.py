import requests

# Set up the API endpoint and authentication headers
url = "https://api.openai.com/v1/engines/davinci-codex/completions"
headers = {
    "Authorization": "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",
    "Content-Type": "application/json"
}

# Define a test prompt to send to the API
prompt = "Hello, world!"

# Send a request to the API and check the response status code
response = requests.post(url, headers=headers, json={
    "prompt": prompt,
    "max_tokens": 100
})
if response.status_code == 200:
    print("The OpenAI API is available")
else:
    print("The OpenAI API is not available")

