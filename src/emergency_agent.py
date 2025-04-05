import time
import json
import os

def emergency_alert(event):
    if event["type"] == "emergency":
        print("🚨 Emergency detected! Clearing path.")
    else:
        print("[Emergency Agent] Monitoring...")

if __name__ == "__main__":
    while True:
        if os.path.exists("event.json"):
            with open("event.json", "r") as f:
                event = json.load(f)
                print(f"[Emergency Agent] Event Type: {event['type']}")  # Debug print
            emergency_alert(event)
        else:
            print("[Emergency Agent] Waiting for event.json...")  # Debug print
        time.sleep(3)
