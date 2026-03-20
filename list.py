#list properties:
#1)It is a sequence (it allow indexing and slicing)
#2)It is an ordered collection
#3)it is mutable(operations like insertion updation)
#4)It may contain duplicate elements
#5)It preserve the insertion ordere
#6)It may contain different type of objects
#7)It is dynamic(it can grow and shrink at runtime)

#'data' "data" '''data''' """data"""  => "str"
#['data1','data2']  => list
#(data1,data2,data3)  => tuple
#{data1,data2,data3}  => set
#{k1:d1,k2:d2,k3:d3}  => ndarray

#list()  =>
#[]  =>






#lst=[[1,2,3],
#     [4,5,6],
#     [7,8,9]]
#print(len(lst))"""
#l1=lst[-1] 
#print(l1[-2])
# OR print(lst[-1][-2])
#for row in lst:
#    for col in row:
#        print(col,end=" ")
#        print()
#        

#lst=[[1,2,3],
#     [4,5,6],
#     [7,8,9]]
#     for row in lst:
#        if col %2==0:
#            print(" ",end=" ")
#        else:
#            print("*",end=" ")
#    print()



#limit = int(input("Enter limit"))
#lst=[]
#for i in range(limit):
#    lst.append(int(input("Enter a number")))
#print(lst)



#res=['j','a','m','e','s']
#print(res[len(res)-1])


#import sys
#lst=[]
#print(sys.getsizeof(lst))  #empty list ka size is 56 so eventually jaise jaise ham elemenent add krte rhege, har individual ka size hame 8 bit milega AND string ke har ek element ko jaise jaise add krte rhege usmein 1 bit for each element milta hai

#for i in dir(list):
#    if i.startswith("__"):
#        pass
#    else:
#        print(i)


#lst=[]
#print(lst)
#lst.append("james")
#print(lst)
#lst.append(123)
#print(lst)
#list.append(lst,12+5j)
#print(lst)
#lst.insert(1,"neena")
#print(lst)
#lst2=["king","blake","paul"]

#lst.extend(lst2)
#print(lst)

#lst[-1]="jack"
#print(lst)

#lst.clear()
#print(lst)


#lst=[13,16,46,95,76,32,46,99,64,11]
#print(f"Before sort :{lst}")
#lst.sort()
#print(lst)
#print(f"After sort :{lst}")

#lst=[13,16,46,95,76,32,46,99,64,11]
#res=sorted(lst,reverse=True)
#print(res)
#print(lst)


#lst=[13,16,46,95,76,32,46,99,64,11]
#print("Before reverse: ",lst)
#lst.reverse()
#print("After reverse: ",lst)


#lst=[13,16,46,95,76,32,46,99,64,11]
#print("Before reversing: ",lst)
#res=lost(reversed(lst))
#print("After reverse: ",res)
#print("Original list: ",lst)


#lst=[10,[100]]
#lst2=lst
#print(lst,lst2)
#lst2[0]=20
#lst2[1].append(200)
#print(lst,lst2)



#import copy
#lst=[10,[100]]
#lst2=copy.deepcopy(lst)
#lst2[0]=20
#lst2[1].append(200)
#print(lst,lst2)


#empdb=[]

#while True:
#    choice=int(input('''
#    MAIN MENU
#    1)Insert Employee Details
#    2)Update Salary
#    3)Remove Employee Details
#    4)Search Employee
#    5)Show all Employees
#    6)Exit
#    Enter your choice->'''))
#
#    if(choice==1):
#        eid=int(input("Enter EID:"))
#        
#    elif(choice==2):
#        pass
#    elif(choice==3):
#        pass
#    elif(choice==4):
#        pass
#    elif(choice==5):
#        pass
    