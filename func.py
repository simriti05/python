# THIS IS A FUNCTION IN C LANGUAGE
# void add(int i,int j)
# {
#     print("%d",i+j)
# }


# def add(i,j):
#     print(i+j)
# print(add(10,20)) GIVES OUTPUT-> 30 AND NONE becoz 10+20=30 but add does not return anything so it gives output NONE


# def add(i,j):
#     print(i*j)
# add("james ",5)


# def add(i:int,j:int):  if we want to hint the user about what type of value i and j have [is called TYPE HINTING]
#     print(i*j)
# add("james ",5)


# def add(i,j)->list:
#     print(i*j)
# add("james ",5)


# def add():
#     i,j=map(int,input("Enter 2 nums").split(" "))
#     return(i*j)

# print(add())


# lst=["MIET"]

# def test(data):
#     data.append("Jammu")

# print(lst)
# test(lst)
# print(lstr)


# """
# 1) Required positional argument
# 2) Default/Optional argument
# default parameter hamesha last mein aayega aur mandatory parameter is always written pehle
# 3)keyword argument
# 4)var arg
# 5)key var arg
# """


# def printName(fname,mname="N/A",lname="N/A")->None:
#     """Function argument demo"""
#     print(f"First Name:{fname} Middle Name:{mname} Last Name:{lname}")

# printName("James",lname="Bond") #lname parameter list mein  hona chahiye tbhi kam krega


# def add(num1,num2):
#     print(num1+num2)

# def add(num1,num2,num3=0):
#     print(num1+num2_num3)

# def add(num1,num2,num3=0,num4=0):
#     print(num1+num2+num3+num4)

# # add(1,1) #This gives error and says 2 arguments are missing becoz python last wale add ko hi consider krega becoz hamne same name se bhout sare variables bnaye hai. Toh ham pehle hi num3 aur num4 ko zero kr dege so that agr inn dono ki values ham input na bhi kre toh vo error dene ki jagah automatically uski value zero le lega
# add(1,1,1,1)


# def addn(*nums):
#     print(sum(nums))
# addn()
# addn(1)
# addn(1,2)
# addn(1,2,3)
# addn(1,2,3,4,5,6,7,8,9)



# def addn(**nums):
#     print(nums)

# addn(a=1)
# addn(a=1,b=2)
# addn(a=1,b=2,c=3)
# addn(a=1,b=2,c=3,d=4)



# def testpara(a,b,*c,d=10,e=20,**f):
#     print(f"""
#     a={a}  b={b}  #1 2
#     c={c}         #(3,4,5,6,7)
#     d={d}  e={e}  #10 20
#     f={f}         #z:100 y:200 x:300
#     """)
# testpara(1,2,3,4,5,6,7,z=100,y=200,x=300)


# def greet():
#     return "Hello World"
# msg=greet  #msg=greet() agr ham use krte hai toh vo uski value print kr dega-> here "Hello World" aur without brackets use krege toh vo ek hexa decimal value print krega [uska address]
# print(msg)


# def outer():
#     print("Hello World from outer function!")
#     def inner():
#         print("Hello World from inner function!")
#     return inner #kyuki hamne inner function ko outer function ke andar bnaya hai toh usko ham call bhi outside the body of inner but inside the body of outer call krege tab hi vo kaam krega aur output print krke dega [inner()]
# res=outer()
# res()
# #using this way we can use inner function outside the body of outer function



