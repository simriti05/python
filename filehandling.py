# A stream is simply a sequence of bytes that flows into or out of our program.
# It's an abstract representation of an input or output device.


# 1)Input:- data can be read from
# 2)Output:- data can be written to

# TYPES:
# 1)Binary or byte streams
# 2)Character streams


# fp = open("bkp.txt")
# print(fp)
# fp.close()
# print(fp.closed)


# mode of opening a file in Character
# 1. r
# 2. r+
# 3. w:- ham jo bhi iss file mein likhege vo hamari txt file mein automatically text aajayega. BUT yeh sirf string likh skta hai
# 4. w+
# 5. a 
# 6. a+



# fp = open("bkp.txt")
# if(fp):
#     print("file is open for writing")
#     print("press enter to close the file")
# input()
# fp.close().





# fp = open("bkp.txt","w")
# msg = input("Enter your message")
# msg+="\n"
# fp.write(msg)
# fp.close()

#WRITE aur WRITELINES sirf string write kr skte hai:- to write we have these two functions only

# fp = open("bkp.txt","a")
#     # msg = input("Enter your message")
#     # msg+="\n"
# lst=["noida","jammu","dehradun","delhi"]
# fp.writelines(lst) #sirf write se yeh code nahi chlega toh ham writelines ko use krege aur vo isko print kr dega in txt file but sirf string nikal ke likhega vo[no commas]
# fp.close()





# fp = open("bkp.txt","r")
#      #print(fp.name,fp.mode,fp.encoding,sep="\n")
#      #for reading hamare pass 3 functions hai
#      #read()   readline()    readlines()
# text = fp.read()   #if we want to read only some specific amount of characters we specify it as eg-read(20)
# print(text)
# fp.seek(0)  #put the cursor at the beginning of the file
# print(text)
# fp.close()





#this code would automatically display 5 lines from our txt file [jitni bhi lines we want it can help us display that]
# fp = open("bkp.txt","r")
# for i in range(int(input("Number of lines"))):
#     text = fp.readline()
#     print(text,end="")
# fp.close()



#if we want to read information in form of list we use readlines
# fp = open("bkp2.txt","r")
# text = fp.readlines()
# for line in text:
#     print(line,end="")
# fp.close()



# fp = open("bkp2.txt","r")
# for line in fp.readlines():
#     print(line,end="")
# fp.close()


#copying information written in one bkp file to another bkp2 file
# fpr = open("bkp.txt","r")
# fpw = open("bkp2.txt","w")

# for line in fpr.readlines():
#     fpw.write(line)

# print("file copy done")
# fpw.close()
# fpr.close()




# FILE.CLOSED:- RETURNS TRUE IF FILE IS CLOSED,FALSE OTHERWISE
# FILE.MODE:- RETURNS ACCESS MODE WITH WHICH FILE WAS OPENED
# FILE.NAME:- RETURNS NAME OF THE FILE 



# WRITE():- WRITES ANY STRING TO AN OPEN FILE
# READ():- READS A STRING FROM AN OPEN FILE
# CLOSE():- FLASHES ANY UNWRITEN INFORMATION AND CLOSES THE FILE OBJECT AFTER WHICH NO MORE WRITING CAN BE DONE


# FILE POSITIONS:-
# 1) TELL():- TELLS US THE CURRENT POSITION WITHIN A FILE OF THE CURSOR [CURRENT CURSOR POSITION]
# 2) SEEK(OFFSET,FROM):- HELPS TO SET THE CURSOR POSITION AT A SPECIFIC PLACE IN A FILE
#  OFFSET:- THIS ARGUMENT INDICATES THE NUMBER OF BYTES TO BE MOVED
#  FROM:- THIS ARGUMENT SPECIFIES THE REFERNCE POSITION FROM WHERE THE BYTES ARE TO BE MOVED



# fp = open("bkp.txt","rb")
# fp.read()
# print(fp.tell())
# fp.close()



# fp = open("bkp.txt","rb")
# fp.seek(12,0)
# print(fp.read(4))

# fp.seek(6,1)
# print(fp.read(11))

# fp.seek(-14,1)
# print(fp.read())

# fp.seek(-3,2)
# print(fp.read())
# fp.close()



# PICKLE:- used to serialize and deserialize a python OBJECT
# pickle.dump(object,file):- isse hota hai serialize
# pickle.load(file):- isse hota hai deserialize



#serialization:- ek txt file mein data dala
# import pickle 
# fp = open("dump.txt","wb")
# #a="james"  #idr a=10 print toh ho jata hai dump.txt lekin in binary toh ham sirf string ko read kr skte hai
# lst=["james","king","neena","blake"]
# t=(101,102,103,104)
# d={101:"james",102:"king",103:"neena",104:"blake"}
# pickle.dump(lst,fp)
# pickle.dump(t,fp)
# pickle.dump(d,fp)
# fp.close()




#ek txt file se phirse data ko read kr liya-DESERIALIZATION
# import pickle
# fp=open("dump.txt","rb")
# l=pickle.load(fp)
# t=pickle.load(fp)
# d=pickle.load(fp)
# fp.close()
# print(l,t,d,sep=" ")



# WHERE EXCEPTIONS OCCUR:
# 1) HARDWARE/OS LEVEL
#   ARITHMETIC EXCEPTIONS,MEMORY ACCESS VIOLATIONS
# 2) LANGUAGE LEVEL
#   BOUNDS VIOLATIONS,VALUE ERROR
# 3) PROGRAM LEVEL
#   USER DEFINED EXCEPTIONS





# import os
# os.system("cls")

# def fun2():
#     #div fun
#   print("Inside fun2")
#   num1,num2=map(int,input("Enter num and dnum sep by space").split())
#   res=num1//num2
#   print(f"result is {res}")
#   print("end of fun2")

# def fun1():

#     print("Inside fun1")
#     fun2()
#     print("End of fun1")


# if __name__=="__main__":

#     print("Inside Main")
#     fun1()
#     print("End of Main")




import os
os.system("cls")
def div():
    print("Inside div fun")
num1,num2=map(int,input("Enter num and dnum sep by space").split())
try:
    res=num1//num2
    print(f"result is {res}")

    print("end of fun2")









