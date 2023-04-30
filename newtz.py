import pytz
from datetime import datetime

time_zone = input("Enter the time zone:")
tz = pytz.timezone(time_zone)
curr_time = datetime.now(tz)
print(curr_time)