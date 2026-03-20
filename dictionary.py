#d = {}
# d["james"] = 78000 #INSERT KEY
# print(d)
# d["james"] = 90000 #KEY UPDATE
# print(d)
# del(d["james"]) #KEY DELETE
# print(d)

# name="james"
# sal=90000
# d[name]=sal
# print(d)


# d=dict(r="red",g="green",b="blue")
# d={"r":"red","g":"green","b":"blue"}
# for i in d:
#     print(i,d[i])

# print(d.keys())
# print(d.values())
# print(d.items())

# for i,j in d.items():
#     print(i,j)

# for i in d.values():
#     print(i)




# lst = ["james", "blake", "ana", "king"]
# for i in lst[:]:
#     if len(i)<5:
#         lst.append(i)
# print(lst)        


# lst = ["james", "blake", "ana", "king","kuldeep","neo"]
# lenlist=[]
# for name in lst:
#     lenlist.append(len(name))
# print(lenlist)

# print([len(i) for i in lst])  #LIST COMPREHENSION

#Create a list of even numbers upto a given range
n=int(input("Enter a range for even numbers: "))
even_numbers=[]
for i in range(n):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)        



