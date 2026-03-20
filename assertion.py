def checkAge(age):
    try:
        assert age>18,"you are minor"
        print("you are not allowed to vote")
    except AssertionError as ob:
        print(ob)
        print("end of code")

checkAge(int(input("Enter your age ")))w