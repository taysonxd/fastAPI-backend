
from datetime import datetime

now = datetime.now()

def print_dates(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.microsecond)
    print(date.timestamp())

year_2023 = datetime(2023, 1, 1)

print_dates(year_2023)

from datetime import time

current_time = time(21, 6, 0)

print('================')
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print('================')
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 9, 11)

print('================')
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year + 1, current_date.month + 1, current_date.day)

print('================')
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)


diff_datetime = now - year_2023
diff_date = current_date - now.date()
print('================')
print(diff_datetime)
print(diff_date)


from datetime import timedelta

start_timedelta = timedelta(300, 100, 100, weeks=20)
end_timedelta = timedelta(500, 100, 100, weeks=10)

print('================')
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
