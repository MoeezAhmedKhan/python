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


# 4. Check number is even or odd

num = int(input("Enter a anumber: "))
while(num != 0):
    if(num % 2 == 0):
        print(num, "is even")
    else:
        print(num, "is odd")
    num = int(input("Enter a anumber: "))
else:
    print(num, "is zero")
    

# 5. Print a table

num = int(input("Enter a anumber: "))
i = 1
while(i <= 10):
    print(num, "*", i, "=", (num * i))
    i = i + 1
else:
    print("Table Printed Successful")


# 6. Lets Start Develop a Small Game

questionList = [
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars",
        "amount": 10,
        "isUserRight": False
    },
    {
        "question": "What is the chemical symbol for water?",
        "answer": "H2O",
        "amount": 20,
        "isUserRight": False
    },
    {
        "question": "Which language is used to create Android Apps?",
        "answer": "Kotlin",
        "amount": 30,
        "isUserRight": False
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "answer": "Pacific Ocean",
        "amount": 40,
        "isUserRight": False
    },
    {
        "question": "Which device is used to measure atmospheric pressure?",
        "answer": "Barometer",
        "amount": 50,
        "isUserRight": False
    }
]

winingAmount = 0
i = 0

while i < len(questionList):
    print("\nQuestion no", i + 1, ":", questionList[i]["question"])
    getInput = input("Give your answer: ")

    if getInput.lower() == questionList[i]["answer"].lower():
        winingAmount += questionList[i]["amount"]
        questionList[i]["isUserRight"] = True
        print("Correct! You won", questionList[i]["amount"], "$")
    else:
        print("Wrong! Correct answer was:", questionList[i]["answer"])

    i += 1

print("\n--------------- Result ----------------\n")
print("🎉 Total Winning Amount:", winingAmount, "$ 🎉")

print("Wrong Questions with Correct Answers:\n")
for i in questionList:
    if not i["isUserRight"]:
        print("-", i["question"], "→", i["answer"])
