import random
import time

def collect_data():
    temperature = round(random.uniform(0, 40), 2)  # Simulate temperature data
    humidity = round(random.uniform(20, 80), 2)    # Simulate humidity data
    location = "Location A"                        # Static location for now
    return {"Temperature": temperature, "Humidity": humidity, "Location": location}

while True:
    data = collect_data()
    print(f"Collected Data: {data}")
    time.sleep(2)  # Collect data every 2 seconds
