import calendar
import datetime

input_date = input()
date = input_date.split('-')
print(date[2] + '/' + date[1] + '/' + date[0])
print(calendar.month_name[int(date[1])])

day = datetime.date(int(date[0]), int(date[1]), int(date[2]))
last_day = datetime.date(int(date[0]), 12, 31)
print(last_day - day)