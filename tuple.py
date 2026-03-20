# Tuple properties
# 1)It is a sequence(it allow indexing and slicing)
# 2)It is an ordered collection
# 3)It is immutable(operations like insertion updation and deletion are not allowed)
# 4)It may contains duplicate elements
# 5)It preserve the insertion order
# 6)It may contain different type of objects
# 7)It is not dynamic(it can't grow and shrink at runtime)


# tup=1,2,3,4,5
# print(tup)

# tup=(12,12.5,"james",12+5j,True,[10,20,30])
# for i in tup:
#     print(i,type(i))


# tup=(12,12.5,"james",12+5j,True,[10,20,30])
# print(tup[-1].append(1000))
# print(tup)

# nums=12,23,34,45
# print(nums)
# a,b,c,d=nums
# print(f"a:{a} b:{b} c:{c} d:{d}")  #a mein 12 ki value b mein 23 and so on


# nums=12,23,34,45
# print(nums)
# a,*b=nums
# print(f"a:{a} b:{b}")  #a mein 12 ki value daal di aur b mein baki sab values


# num1,num2=int(input("num1 ")),int(input("num2 "))
# print(f"Before swap num1 = {num1} num2={num2}")
# num1,num2=num2,num1
# print(f"After swap num1={num1} num2={num2}")  #NUMBER SWAPPING


# FIBONACCI SERIES[METHOD 1] 0 1 1 2 3 5 8 13 21 34
# num1 = 0
# num2 = 1
# print(num1,num2,end=" ")
# for i in range(8):
#     num3=num1+num2
#     print(num3,end=" ")
#     num1=num2
#     num2=num3

#[METHOD 2]
# num1,num2=0,1
# for i in range(10):
#     print(num1,end=" ")
#     num1,num2=num2,num1+num2




