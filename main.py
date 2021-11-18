import time

from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
          title=" Drink Water",
          message="paani pee lee bhai...............",

          timeout=5
        )
        time.sleep(6)
