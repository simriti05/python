#MANUAL 13
# fp = open("demo.txt","w")
# msg=input("enter your message ")
# fp.write(msg)
# fp.close()

# fp=open("demo.txt","r")
# text=fp.read()
# lst=text.split(" ")
# lst=list(set(lst))
# lst.sort()

# for i in lst:
#     print(i,end=" ")




#MANUAL 14
# name=input("Enter file name ")
# fp=open(name,"w")
# count = int(input("Enter number of lines "))
# for i in range(count):
#     msg=input("Enter your message")+"\n"
#     fp.write(msg)

# fp.close()






#MANUAL 9
import os
from abc import ABC

class Department:
    def __init__(self,did,dname,location):
        self.did = did
        self.dname = dname
        self.location = location

    def __str__(self):
        return f'{self.did} {self.dname} {self.location}'


class Employee(ABC):
    def __init__(self,eid,name,department):
        self.eid = eid
        self.name = name
        self.department = department

    def __str__(self):
        pass


class DailyWageEmp(Employee):
    def __init__(self,name,eid,dw,nod,department):
        super().__init__(eid,name,department)
        self.dw = dw
        self.nod = nod
        self.salary = self.dw * self.nod
        self.etype = "Daily Wage"
    
    def updateSalary(self,newdw):
        self.dw = newdw
        self.salary = self.dw * self.nod

    def __str__(self):
        return f'{self.eid} {self.name} {self.salary} {self.etype} {self.department}'


class RegularEmp(Employee):
    def __init__(self,eid,name,hra,basic,department):
        super().__init__(eid,name,department)
        self.hra = hra
        self.basic = basic
        self.salary = self.hra + self.basic
        self.etype = "Regular"

    def updateSalary(self,newbasic):
        self.basic = newbasic
        self.salary = self.hra + self.basic

    def __str__(self):
        return f'{self.eid} {self.name} {self.salary} {self.etype} {self.department}'


db = []

while True:
    os.system("cls")
    choice = int(input('''Main Menu
1)Insert Employee
2)Update Salary
3)Delete Employee
4)Search Employee
5)Show all employees
6)Show all departments
7)Exit
Enter Your Choice:- '''))

    if choice == 1:
        emp = None
        ch = int(input("1.Regular Employee 2.Daily Wage Employee: "))
        eid = int(input("Enter Eid: "))
        name = input("Enter Name: ")
        did = input("Enter Did: ")
        dname = input("Enter Dname: ")
        loc = input("Enter Location: ")

        dept = Department(did,dname,loc)

        if ch == 1:
            basic = int(input("Enter Basic: "))
            hra = int(input("Enter HRA: "))
            emp = RegularEmp(eid,name,hra,basic,dept)

        elif ch == 2:
            dw = int(input("Enter Daily Wage: "))
            nod = int(input("Enter working days: "))
            emp = DailyWageEmp(name,eid,dw,nod,dept)

        db.append(emp)
        input("Press any key to continue ")

    elif choice == 2:
        eid = int(input("Enter Eid: "))
        amt = int(input("Enter updated amount: "))
        for e in db:
            if e.eid == eid:
                e.updateSalary(amt)
        input("Press any key to continue ")

    elif choice == 3:
        eid = int(input("Enter Eid to delete: "))
        for i in range(len(db)):
            if db[i].eid == eid:
                del db[i]
                break
        input("Press any key to continue ")

    elif choice == 4:
        eid = int(input("Enter Eid: "))
        for e in db:
            if e.eid == eid:
                print(e)
                break
        input("Press any key to continue ")

    elif choice == 5:
        for e in db:
            print(e)
        input("Press any key to continue ")

    elif choice == 6:
        for e in db:
            print(e.department)
        input("Press any key to continue ")

    elif choice == 7:
        break

    else:
        print("Invalid choice")
        input("Press any key to continue ")

















