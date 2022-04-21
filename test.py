import datetime as dt
from datetime import datetime, timedelta, date

start_day=7
year = "2020"
strt_date = date(int(year), 1, 1)
res_date = strt_date + timedelta(days=int(start_day) - 1)
first_timestamp=res_date.strftime("%m/%d/%Y %H:%M")
my_time=datetime.strptime(first_timestamp, "%m/%d/%Y %H:%M")

time_stamp_list=[]

for i in range(100):
    next_time=timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=i, weeks=0)
    new_time=my_time+next_time
    time_stamp_list.append(new_time)


li=[1,2,4,5,6,7,7]
print(sum(li[4:]))