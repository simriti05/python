#4 Write a program to perform searching activity using linear and binary search
# arr = []
# n = int(input("Enter limit"))
# for i in range(n):
#     num=int(input("Enter a number"))
#     arr.append(num)
# print("Array:",arr)    

# x = int(input("Enter a element to search: "))
# for i in range(len(arr)):
#     if arr[i] == x:
#         print(f"Element found at index {i}")
#         break
# else:

#      print("Element not found") 


# arr.sort()
# print("Sorted array: ",arr)
# x = int(input("Enter element to search: "))
# si = 0
# ei = len(arr) - 1
# while si<=ei:
#     mid = (si + ei)// 2
#     if arr[mid] == x:
#         print("Binary search found at index",mid)
#         break
#     elif arr[mid] < x:
#         si = mid+1
#     else:
#         ei = mid-1 
# else:
#     print("binary search element not found")           


#11 Write a program that accepts the length of three sides of a triangle as inputs.The program should indicate whether or not the triangle is a right-angled triangle (Use pythagorean theorem) Also find the area using Heron's formula 


# a = int(input("Enter side 1: "))
# b = int(input("Enter side 2: "))
# c = int(input("Enter side 3: "))

# side1, side2, hypotenuse = sorted([a, b, c])
# if hypotenuse**2 == side1**2 + side2**2:
#     print("It is a right-angled triangle.")
# else:
#     print("It is NOT a right-angled triangle.")

# s = (a + b + c) / 2
# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print("Area of the triangle is:", round(area, 2))



#10 Write a program to create a simple calculator using a switch case and function for every operation

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Cannot divide by zero"

# print("Simple Calculator")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = int(input("Enter your choice (1-4): "))
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == 1:
#     print("Result:", add(num1, num2))
# elif choice == 2:
#     print("Result:", subtract(num1, num2))
# elif choice == 3:
#     print("Result:", multiply(num1, num2))
# elif choice == 4:
#     print("Result:", divide(num1, num2))
# else:
#     print("Invalid choice")


#MANUAL 5
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))
# print("Enter matrix elements row by row: ")

# matrix = []
# for i in range(rows):
#     row = list(map(int, input(f"Enter elements of row {i+1} separated by space: ").split()))
#     if len(row) != cols:
#         print("Error: Number of elements does not match the number of columns.")
#         exit()
#     matrix.append(row)

# k = int(input("Enter kth row you need to reverse: "))

# for i in range(rows):
#     if (i+1) % k == 0:
#         matrix[i] = matrix[i][::-1]

# print("\nMatrix after reversing every kth row:")
# for row in matrix:
#     print(row)


