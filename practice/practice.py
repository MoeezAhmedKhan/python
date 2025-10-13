# 1. Check current time and display appropriate greeting

import datetime as dt
import pytz

pk_time  = dt.datetime.now(pytz.timezone("Asia/Karachi"))
currentHour = pk_time.hour
print(f"Current Hour {currentHour}")

if(5 <= currentHour < 12): # if currentHour is greater then 5 means morning start and currentHour is less then 12. Morning end before 12
    print("Good Morning")
elif(12 <= currentHour < 17): # 12 to 5 - Afternoon
    print("Good Afternoon")
elif(17 <= currentHour <= 20): # 5 to 8 - Evening
    print("Good Evening")
else:
    print("Good Night")


# 2. Change order into reverse (Reverse number) - 1234 into 4321

num = int(input("Enter a number: "))
rev = 0

while num > 0: # Its mean any number end before zero in the reverse order.
    digit = num % 10       # Get the last digit of num
    rev = rev * 10 + digit # Append the digit to the reversed number
    num = num // 10        # Remove the last digit from num

print(rev)


# 3. Check if a number is a palindrome or not.
# Reverse the number and compare it with the original.
# If both are the same, then it is a palindrome.

num = int(input("Enter a number: "))
orignalNum = num
rev = 0
while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if orignalNum == rev:
    print(orignalNum, "Its is orignal ",rev, "Its is reversed and its is paindrom")
else:
    print(orignalNum, "Its is orignal ",rev, "Its is reversed and its is not paindrom")