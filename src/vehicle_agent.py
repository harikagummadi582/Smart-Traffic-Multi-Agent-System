import time
import json
import os

def vehicle_action(event):
    if event["type"] == "rush_hour":
        print("[Vehicle Agent] Traffic is heavy! Slowing down.")
    elif event["type"] == "accident":
        print("[Vehicle Agent] Accident detected! Avoiding area.")
    elif event["type"] == "roadblock":
        print("[Vehicle Agent] Roadblock detected! Re-routing.")
    elif event["type"] == "emergency":
        print("[Vehicle Agent] Emergency vehicle detected! Clearing path.")
    else:
        print("[Vehicle Agent] Normal driving conditions.")

if __name__ == "__main__":
    while True:
        if os.path.exists("event.json"):
            with open("event.json", "r") as f:
                event = json.load(f)
                print(f"[Vehicle Agent] Event Type: {event['type']}")  # Debug print
            vehicle_action(event)
        else:
            print("[Vehicle Agent] Waiting for event.json...")  # Debug print
        time.sleep(3)
