from datetime import datetime, timezone, timedelta
import time
#def utc_to_local(utc_dt):
#    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

def utc_to_local(dt):
    if time.localtime().tm_isdst:
        return dt - timedelta(seconds = time.altzone)
    else:
        return dt - timedelta(seconds = time.timezone)


utc_time = '4:39:22 PM'
t = datetime.strptime(utc_time, '%I:%M:%S %p')
cet = utc_to_local(t)
print(cet)