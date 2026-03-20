"""st=input("Enter a string: ")
if st==st[::-1]:
    print("palindrome")
else:
    print("not palindrome")
"""
"""
st='abracadabra'
fc=st[0]
newst=fc
for i in st[1:]:
    if i==fc:
        newst+='$'
    else:
        newst+=i
print(newst)
"""
"""
text = "abc"
converted = ""

for char in text:

    ascii_value = ord(char)
    uppercase_char = chr(ascii_value - 32)
    converted += uppercase_char

print(converted)
"""
"""
age=34
name='james'
#print("my name is",name," and i am", age,"years old")
print("my name is"+name+" and i am"+str(age)+"year's old")
"""


"""
st = 'python'
print(st[])
"""

"""
age = 35
name = "james"
st = "my name is {} and i am {} year's old".format(name,age)
st = f"my name is {name} and i am {age} year's old"
print(st)
"""

"""heading = ["eid","name","salary","did","location"]
lst = [101,"James Bond",80000,10,"Noida"]
print("{0:<10} {1:<15} {2:<10} {3:<10} {4:<10}".format(*heading))
print("-"*63)
print("{0:<10} {1:<15} {2:<10} {3:<10} {4:<10}".format(*lst))
print("-"*63)
"""
"""
st = "JAMES BOND"
print(st.center(40,'-'))
print(st.ljust(40,'-'))
print(st.rjust(40,'-'))

st='mississippi'
print(st.count("s"))
"""
"""
st = 'python'
print(st.encode(encoding = "ascii",errors="strict"))
"""
"""
st = 'pytho'+'n'
print(st.encode(encoding="ascii",errors="ignore"))
"""
"""
import hashlib
name="kuldeep"
encname=hashlib.md5(name.encode())
print(encname.hexdigest())  \

"""


st = "neena,blake,king,smith"
lst = st.split(" , ")
print(lst)
print("*".join(lst))


