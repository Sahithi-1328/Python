x=int(input())
#1
if (x%400==0 or (x%4==0 and x%100!=0)):
        print("leap")
else:
        print("Not leap")
#2
def is_leap_year(year):
    return True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False
print(is_leap_year(x))
#3
import calendar
print(calendar.isleap(x))
#4
a = lambda x: True if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0) else False
print(a(x))
