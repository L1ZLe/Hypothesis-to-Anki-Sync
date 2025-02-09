import requests
import os
import json
from datetime import datetime
import subprocess
import time
import psutil  # For finding and closing Anki

# Replace with your Hypothesis API token
API_TOKEN = "" ##################### add your Hypothes.is API key here
url = "https://hypothes.is/api/search"

# Configuration files
LAST_RUN_FILE = "last_run.txt"
PROCESSED_IDS_FILE = "processed_ids.txt"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

def ensure_anki_is_running():
    """
    Check if AnkiConnect is reachable. If not, open Anki.
    """
    try:
        # Try to connect to AnkiConnect
        requests.get("http://localhost:8765").json()
        print("Anki is already running.")
    except requests.exceptions.ConnectionError:
        # If AnkiConnect is not reachable, open Anki
        print("Anki is not running. Opening Anki...")
        subprocess.Popen(["anki"])  # Command to open Anki
        # Wait for Anki to start (adjust sleep time if needed)
        time.sleep(10)

def close_anki():
    """
    Close Anki after the script finishes.
    """
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'anki':
            print(f"Closing Anki (PID: {proc.info['pid']})...")
            proc.terminate()  # Gracefully terminate Anki
            break

def read_last_run():
    try:
        with open(LAST_RUN_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "2000-01-01T00:00:00.000000+00:00"  # Default old date

def write_last_run(timestamp):
    with open(LAST_RUN_FILE, "w") as f:
        f.write(timestamp)

def read_processed_ids():
    try:
        with open(PROCESSED_IDS_FILE, "r") as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

def write_processed_ids(ids):
    with open(PROCESSED_IDS_FILE, "w") as f:
        for ann_id in ids:
            f.write(f"{ann_id}\n")

def create_anki_note(front, back, tags):
    return {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Hypothes.is",
                "modelName": "Basic",
                "fields": {
                    "Front": front,
                    "Back": back
                },
                "tags": tags
            }
        }
    }

# Ensure Anki is running before proceeding
ensure_anki_is_running()

# Read previous state
last_run = read_last_run()
processed_ids = read_processed_ids()
new_processed_ids = set()

params = {
    "group": "", ##################### add your Hypothes.is group id here
    "limit": 200,
    "sort": "created",
    "order": "asc",
    "query": f'created:>="{last_run}"'
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    annotations = data.get("rows", [])
    
    if annotations:
        # Update last_run to the newest annotation's creation time
        new_last_run = annotations[-1]["created"]
        write_last_run(new_last_run)

    for ann in annotations:
        ann_id = ann.get("id")
        if ann_id in processed_ids:
            continue

        # Extract text quote
        exact_text = "N/A"
        for selector in ann.get("target", [{}])[0].get("selector", []):
            if selector.get("type") == "TextQuoteSelector":
                exact_text = selector.get("exact", "N/A")
                break

        # Prepare Anki card
        front = ann.get("text", "No text")
        back = f"{exact_text}\n\nSource: <a href='{ann.get('uri', '#')}'>Link</a>"
        tags = ann.get("tags", []) + ["Hypothesis"]  # Add custom tag

        note = create_anki_note(front, back, tags)
        
        # Send to AnkiConnect
        try:
            anki_response = requests.post("http://localhost:8765", json=note)
            if anki_response.json().get("error"):
                print(f"Error adding note: {anki_response.json()['error']}")
            else:
                new_processed_ids.add(ann_id)
        except requests.exceptions.ConnectionError:
            print("Could not connect to AnkiConnect. Is Anki running?")
            break

    # Update processed IDs
    processed_ids.update(new_processed_ids)
    write_processed_ids(processed_ids)
    print(f"Successfully processed {len(new_processed_ids)} new annotations")

else:
    print(f"Hypothesis API Error: {response.status_code} - {response.text}")

# Close Anki after processing
close_anki()
