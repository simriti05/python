"""init=0
while init<5:
    print("hello world")
    init+=1
"""
"""
while True:
    print("hello world!")
    ch=input("do you want to print it again y/n")
    if ch=='n':
        print("Exit!")
        break
"""
"""
arr=[12,23,34,45,56,68,45,56,67,78,89,90]
init=0
while init<len(arr):
    print(arr[init])
    init+=1
"""
"""
num=int(input("Enter the nummber = "))
i=1
while (i<=10):
    print(num,'X','i','=',num*i)
    i+=1

"""
"""
arr=[1,2,3,4,5,6,7,8,9,10]
num=int(input("Enter the number = "))


init=0
while init<len(arr):
    print(num," x ",arr[init], " = ",num*arr[init])
    init+=1

"""
"""
import random
num=random.randint(1,100)
count=0
while True:
    count+=1
    guess=int(input("Enter any number between 1 to 100: "))
    if(guess==num):
        print("Your number is same!")
        print(count)
        break
    elif(guess<num):
        print("taken number is lower")
    else:
        print("taken number is higher")
"""
"""
arr=[12,13,54,94,61,43,65]
num=int(input("enter a number: "))
flag=0
for temp in arr:
    if num==temp:
        print("number is in the list")
        flag=1
        break

if flag==0:
    print("number is not in the list")
   """
    

