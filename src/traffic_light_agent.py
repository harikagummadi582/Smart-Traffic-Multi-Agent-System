# import time
# import json
# import os

# def traffic_light_action(event):
#     if event["type"] == "rush_hour":
#         print("[Traffic Light Agent] Rush hour! Extending green light.")
#     elif event["type"] == "accident":
#         print("[Traffic Light Agent] Accident ahead! Changing light for emergency vehicles.")
#     elif event["type"] == "roadblock":
#         print("[Traffic Light Agent] Roadblock detected! Redirecting traffic flow.")
#     elif event["type"] == "emergency":
#         print("[Traffic Light Agent] Emergency vehicle detected! Switching to green.")
#     else:
#         print("[Traffic Light Agent] Normal traffic flow. Keeping current signals.")

# if __name__ == "__main__":
#     while True:
#         if os.path.exists("event.json"):
#             with open("event.json", "r") as f:
#                 event = json.load(f)
#                 print(f"[Traffic Light Agent] Event Type: {event['type']}")  # Debug print
#             traffic_light_action(event)
#         else:
#             print("[Traffic Light Agent] Waiting for event.json...")  # Debug print
#         time.sleep(3)






# import json, time

# def get_traffic_data():
#     with open("datasets/traffic_data.json") as f:
#         return json.load(f)

# def calculate_priority(traffic_data):
#     # Higher traffic gets higher priority
#     sorted_lanes = sorted(traffic_data.items(), key=lambda x: x[1], reverse=True)
#     return [lane for lane, _ in sorted_lanes]  # ['east', 'north', ...]

# def run_traffic_light_agent():
#     while True:
#         traffic_data = get_traffic_data()
#         priority_order = calculate_priority(traffic_data)

#         print("\n[Traffic Light Agent] Adjusting signals dynamically based on traffic load...")
#         for lane in priority_order:
#             duration = min(max(traffic_data[lane] // 2, 2), 10)  # between 2 and 10 seconds
#             print(f"[Green Signal] {lane.upper()} → {traffic_data[lane]} vehicles, duration: {duration}s")
#             time.sleep(duration)

#         print("[Traffic Light Agent] Re-evaluating...\n")
#         time.sleep(1)


# run_traffic_light_agent()


import json
import time

def read_event():
    try:
        with open('event.json', 'r') as file:
            return json.load(file).get("event", "normal")
    except FileNotFoundError:
        return "normal"

def read_traffic_data():
    try:
        with open('datasets/traffic_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

while True:
    event = read_event()
    print(f"[Traffic Light Agent] Event Type: {event}")

    traffic_data = read_traffic_data()

    # Respond to traffic volume
    for junction, data in traffic_data.items():
        vehicle_count = data.get("vehicle_count", 0)

        if vehicle_count > 40:
            print(f"[Traffic Light Agent] 🚦 Heavy traffic at {junction}. Extending green light.")
        elif vehicle_count < 15:
            print(f"[Traffic Light Agent] 🚥 Light traffic at {junction}. Shortening green light.")
        else:
            print(f"[Traffic Light Agent] Normal traffic at {junction}. Keeping signal duration.")

    # Respond to event
    if event == "rush_hour":
        print("[Traffic Light Agent] Rush hour! Extending green light at major roads.")
    elif event == "roadblock":
        print("[Traffic Light Agent] Roadblock detected! Redirecting traffic flow.")
    else:
        print("[Traffic Light Agent] Normal conditions. Monitoring...")

    time.sleep(5)
