

import sys
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

slow_print("--- Age Calculator Pro Max Ultra ---")
slow_print("Enter your birth date: YYYY-MM-DD")
slow_print("Or with time if you remember: YYYY-MM-DD HH:MM:SS")

user_input = input("Your birth date: ")

try:
    # If user entered date + time
    birth = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
except ValueError:
    # If user entered date only, assume 00:00:00 midnight
    birth = datetime.strptime(user_input, "%Y-%m-%d")

now = datetime.now()
diff = now - birth
seconds = diff.total_seconds()
delta = relativedelta(now, birth)

slow_print(f"You have been alive for:")
time.sleep(0.5)
slow_print(f"{delta.years} years, {delta.months} months, {delta.days} days")
time.sleep(0.5)
slow_print(f"That's about {seconds:,.0f} seconds")
time.sleep(0.5)
slow_print(f"Or {seconds * 1000:,.0f} milliseconds 🔥")
time.sleep(0.5)
slow_print(f"Or {seconds * 1000000:,.0f} microseconds... you're ancient 😂")
