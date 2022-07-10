import argparse
import json
import os

import requests


def send(message: str):
    """Send a message to the Discord API."""
    webhook_url = os.environ.get("INPUT_WEBHOOK_URL")
    if not webhook_url:
        raise ValueError("No webhook URL provided.")
    data = {"content": message}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code != 204:
        print("Error: {}".format(response.text))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="The message to send")
    args = parser.parse_args()

    send(args.message)
    print("Message sent")
