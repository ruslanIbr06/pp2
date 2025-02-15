#1 Write a Python program to subtract five days from current date.
import datetime

today = datetime.datetime.now()

print(f"Today is {today.strftime("%Y.%m.%d")}")                        #Today is 2025.02.15
print(f"Five days ago was {today.strftime("%Y.%m")}.{today.day - 5}")  #Five days ago was 2025.02.10

#2 Write a Python program to print yesterday, today, tomorrow.
print(f"Yesterday was {today.strftime("%Y.%m")}.{today.day - 1}")      #Yesterday was 2025.02.14
print(f"Today is {today.strftime("%Y.%m.%d")}")                        #Today is 2025.02.15
print(f"Tomorrow will be {today.strftime("%Y.%m")}.{today.day + 1}")   #Tomorrow will be 2025.02.16


#3 Write a Python program to drop microseconds from datetime.

print(today.strftime("%Y.%m.%d - %M minutes %S seconds"))#2025.02.15 - 27 minutes 02 seconds

#4 Write a Python program to calculate two date difference in seconds.

date1 = datetime.datetime(2025, 5, 19, 12, 15, 00)
date2 = datetime.datetime(2025, 5, 24, 14, 40, 00)

difference = abs((date1-date2).total_seconds())
print(f'The difference between {date1} and {date2} is {difference} seconds') #The difference between 2025-05-19 12:15:00 and 2025-05-24 14:40:00 is 440700.0 seconds
