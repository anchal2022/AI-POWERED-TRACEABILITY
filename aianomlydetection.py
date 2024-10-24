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

# Example of using this with the real-time data
for i in range(5):  # Run 5 iterations for demonstration
    data = collect_data()
    print(f"Collected Data: {data}")
    result = detect_anomaly(data)
    print(result)
