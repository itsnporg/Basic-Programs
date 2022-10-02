#Python program to find difference between 2 time periods
from datetime import datetime

strt_time = "4:22:52"
end_time = "10:35:53"
t1 = datetime.strptime(strt_time, "%H:%M:%S")
print('Start time is', t1.time())

t2 = datetime.strptime(end_time, "%H:%M:%S")
print('End time is', t2.time())
diff = t2 - t1

# time difference in seconds
print(f"Time difference is {diff.total_seconds()} seconds")
