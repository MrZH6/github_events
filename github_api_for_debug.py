import pandas as pd
import json
import requests

with open("credentials.json", 'r') as file:
    creds = json.load(file)
TOKEN = creds["api_token"]

REPOS = [
    "datamole-ai/edvart",
    "keboola/python-component",
    "json-editor/json-editor",
    "astanin/python-tabulate",
    "vacanza/python-holidays"
]

out_data = []
out_data_headers = ["repo", "event_id", "event_type", "user", "created_at"]

for repo in REPOS:
    url = f"https://api.github.com/repos/{repo}/events"

    headers = {
      'Accept': 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
      'Authorization': f"Bearer {TOKEN}"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params={"per_page": 50, "page": 5}
    )

    # print(response.text)
    response_parsed = json.loads(response.content.decode('utf-8'))

    for elem in response_parsed:
        out_data.append([
            repo,
            elem["id"], elem["type"], elem["actor"]["login"], elem["created_at"]
        ])

print(out_data)