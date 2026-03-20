"""
IF ELIF ELSE
"""
"""per = int(input("Enter your percentage: "))
if (100>=per and per>=90):
    print("Your grade is A")
elif (per<90 and per>=80):
    print("Your grade is B")
elif (per<80 and per>=60):
    print("Your grade is C")
elif (per<60 and per>=50):
    print("Your grade is D")
else:

    print("NO GRADE!")
"""

"""num = int(input("Enter the number: "))
if (num>0):
    print("Number is postive")
elif (num==0):
    print("ZERO")
else:
    print("number is negative")
"""


"""num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if(num1>num2 and num1>num3):
    print("number 1 is the greatest = ",num1)
if(num2>num1 and num2>num3):
    print("number 2 is the greatest = " ,num2)
else:
    print("number 3 is the greatest = " ,num3)
"""


"""num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
res=(num1 if num1>num3 else num3) if num1>num2 else(num2 if(num2>num3) else num3
print(res,"is greatest")"""

char=input("enter any character").lower()
if len(char)==1:
    match char:
        case'a':print('vowel')
        case'e':print('vowel')
        case'i':print('vowel')
        case'o':print('vowel')
        case'u':print('vowel')
        case _:print('consonant')
else:
    print("invalid character")
