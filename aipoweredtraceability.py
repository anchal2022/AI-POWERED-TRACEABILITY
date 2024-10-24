import random
import time

# Real-Time Data Collection Function
def collect_data():
    temperature = round(random.uniform(0, 40), 2)  # Simulate temperature data
    humidity = round(random.uniform(20, 80), 2)    # Simulate humidity data
    location = "Location A"                        # Static location for now
    return {"Temperature": temperature, "Humidity": humidity, "Location": location}

# AI Anomaly Detection Function
def detect_anomaly(data):
    if data["Temperature"] > 30 or data["Humidity"] < 30:
        return "Anomaly Detected: Take action!"
    else:
        return "Data Normal"

# Alert System Function
def send_alert(data):
    if detect_anomaly(data) == "Anomaly Detected: Take action!":
        print("ALERT! Contamination risk detected!")
    else:
        print("All systems normal.")

# Example usage to run 5 times
for i in range(5):
    data = collect_data()
    print(f"Collected Data: {data}")
    send_alert(data)
    time.sleep(2)  # Adding delay for better real-time simulation
