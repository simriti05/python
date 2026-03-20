# MANUAL 2
# isse pehle write defintions of LIST DICTIONARY LOOP ki
# lst=["red","green","blue","cyan","black"]

# for color in lst:
#     print(color)
# print()


# d={101:"james",102:"neena",103:"blake",104:"king"}

# for i in d.keys():
#     print(i,end=" ")
# print()

# for i in d.values():
#     print(i,end=" ")
# print()

# for eid,name in d.items():
#     print(eid," ",name)




# MANUAL 6
# def studentRecords():
#     students=[]
#     count=int(input("Number of students "))
#     for i in range(count):
#         student={}
#         student["id"]=int(input("Enter student id "))  #id name ki key
#         student["name"]=input("Enter name ")  
#         student["per"]=float(input("Enter percentage "))  
#         student["branch"]=input("Enter branch ")
#         students.append(student)
#     return students
# def search(db,id):
#     for record in db:
#         if record['id']==id:
#             print(record)

# if __name__=="__main__":
#         db=studentRecords()
#         for i in db:
#             print(i) 
#         id=int(input("enter the id of the student"))
#         search(db,id)





#MANUAL 7
# def studentRecords():
#     students=[]
#     count=int(input("Number of students "))
#     for i in range(count):

       
#         id=int(input("Enter student id "))  
#         name=input("Enter name ")  
#         per=float(input("Enter percentage "))  
#         branch=input("Enter branch ")
#         student=(id,name,per,branch)
#         students.append(student)
#     return students

# def displaydb(db):
#     print("-"*40)
#     print(f"{'id:<5'}{'name:<10'}{'per:<5'}{'branch:<10'}")
#     print("-"*40)
#     for record in db:
#         print(f"{record[0]:<5}{record[1]:<10}{record[2]:<8}{record[3]:<10}")
#     print("-"*40)


# if __name__=="__main__":
#         db=studentRecords()
#         displaydb(db)
      
        