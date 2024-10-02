import requests
import time

def fetch_alerts():
    response = requests.get('http://localhost:5000/alerts')
    if response.status_code == 200:
        alerts = response.json()
        for alert in alerts:
            print(alert)
    else:
        print("Failed to fetch alerts.")

while True:
    fetch_alerts()
    time.sleep(10)
