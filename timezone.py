from datetime import datetime, timezone

utc_dt = datetime.now(timezone.utc) # UTC time
dt = utc_dt.astimezone() # local time


#or from pytz database
import pytz

tz = pytz.timezone('Europe/Berlin')
berlin_now = datetime.now(tz)