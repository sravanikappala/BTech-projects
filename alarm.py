import time
from datetime import datetime

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time, end="\r")

    if current_time == alarm_time:
        print("\n⏰ Wake up! Alarm ringing!")
        for i in range(5):
            print("BEEP! BEEP!")
            time.sleep(1)
        break

    time.sleep(1)
