import psutil
import requests
from time import sleep


API_URL = "API_URL"
MEMORY_ALARM_PERCENT = 90
sleep_time = 20


def main():
    while True:
        if psutil.virtual_memory().percent >= MEMORY_ALARM_PERCENT:
            requests.post(API_URL, json={"message": "High memory usage detected!"})
        sleep(sleep_time)


if __name__ == "__main__":
    main()
