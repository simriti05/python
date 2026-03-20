"""
IF ELIF ELSE
"""
per = int(input("Enter your percentage: "))
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
