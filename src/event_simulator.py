# import random
# import time
# import json

# EVENT_TYPES = ["normal", "rush_hour", "accident", "roadblock", "emergency"]

# def emit_event():
#     event = {"type": random.choice(EVENT_TYPES)}
#     print(f"\n📢 Simulated Event: {event['type']}")
#     with open("event.json", "w") as f:
#         json.dump(event, f)
#     return event

# if __name__ == "__main__":
#     while True:
#         emit_event()
#         time.sleep(5)





# import json, random, time

# while True:
#     traffic_data = {
#         "north": random.randint(0, 30),
#         "south": random.randint(0, 30),
#         "east": random.randint(0, 30),
#         "west": random.randint(0, 30)
#     }
#     with open("datasets/traffic_data.json", "w") as f:
#         json.dump(traffic_data, f)
    
#     time.sleep(5)  # simulate update every 5 seconds



import json
import random
import time

EVENTS = ["rush_hour", "roadblock", "normal"]

def simulate_event():
    return random.choice(EVENTS)

def simulate_traffic_data():
    return {
        "junction_1": {
            "vehicle_count": random.randint(10, 60),
            "avg_speed": random.randint(20, 50)
        },
        "junction_2": {
            "vehicle_count": random.randint(10, 60),
            "avg_speed": random.randint(20, 50)
        }
    }

while True:
    event = simulate_event()
    with open('event.json', 'w') as f:
        json.dump({"event": event}, f)
    print(f"\n📢 Simulated Event: {event}")

    traffic_data = simulate_traffic_data()
    with open('datasets/traffic_data.json', 'w') as f:
        json.dump(traffic_data, f, indent=4)
    print("🚦 Simulated Traffic Data Updated")

    time.sleep(5)


# import json
# import random
# import time

# EVENTS = ["rush_hour", "roadblock", "normal"]

# def simulate_event():
#     return random.choice(EVENTS)

# def simulate_traffic_data():
#     return {
#         "junction_1": {
#             "vehicle_count": random.randint(10, 60),
#             "avg_speed": random.randint(20, 50)
#         },
#         "junction_2": {
#             "vehicle_count": random.randint(10, 60),
#             "avg_speed": random.randint(20, 50)
#         }
#     }

# while True:
#     event = simulate_event()
#     with open('event.json', 'w') as f:
#         json.dump({"event": event}, f)
#     print(f"\n📢 Simulated Event: {event}")

#     traffic_data = simulate_traffic_data()
#     with open('datasets/traffic_data.json', 'w') as f:
#         json.dump(traffic_data, f, indent=4)
#     print("🚦 Simulated Traffic Data Updated")

#     time.sleep(5)
