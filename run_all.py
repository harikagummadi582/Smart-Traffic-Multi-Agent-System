import subprocess

# List of Python scripts to run
scripts = [
    "src/event_simulator.py",
    "src/emergency_agent.py",
    "src/vehicle_agent.py",
    "src/traffic_light_agent.py"
]

# Run each script in the background
processes = []
for script in scripts:
    process = subprocess.Popen(["python3", script])
    processes.append(process)

# Wait for all processes to finish
for process in processes:
    process.communicate()
