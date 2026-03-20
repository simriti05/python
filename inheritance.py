#INHERITANCE
# 1)it is the mechanism of acquiring some attributes of any existing class type into a new class type
# 2)establishes a 'is a' relationship
# 3)establishes a hierachial relationship among classes
# 4)establishes a superclass/subclass relationship
# class Employee:
#     def __init__(self,eid,name):
#         self.eid=eid
#         self.name=name

#     def printEmp(self):
#         print(f"""
# Eid:{self.eid}
# Name:{self.name}""")

# class RegEmployee(Employee):
#     def __init__(self,eid,name,basic,hra,da):
#         super().__init__(eid,name)
#         self.basic=basic
#         self.hra=hra
#         self.da=da
#         self.salary=self.basic+self.hra+self.da

#     def printReg(self):
#         print(f"""
# Basic:{self.basic}
# HRA:{self.hra}
# DA:{self.da}
# Basic:{self.salary}""")


# class DWEmployee(Employee):
#     def __init__(self,eid,name,dw,nod):
#         self.dw=dw
#         self.nod=nod
#         self.salary=dw*nod
#     def printDWEmp(self):
#         super().printEmp()
#         print(f"""
# Daily Wage:{self.dw}
# Num of days:{self.nod}
# Salary:{self.salary}""")

# regemp = Employee(202,"James",50000,12000,10000)
# regemp.printEmp()
# regemp.printReg()


# dwageemp = DWEmployee(101,"king",600,22)
# dwageemp.printDWemp()





#PROGRAM 1
# from abc import ABC,abstractmethod
# class MediaPlayer(ABC):
#     def playAudio(Self):
#         print("can play audio")
# @abstractmethod
# def playVideo(Self):
#     pass

# class SoundRecorder(MediaPlayer):
#     def playvideo():
#         print("I can not play video")

# class VLCPlayer(MediaPlayer):
#     def playvideo():
#         print("I can play video")



# #ob.VLCPlayer()

# ob=SoundRecorder()
# ob.pLayAudio()
# ob.playVideo()


#     def playVideo():
#         pass




#PROGRAM 2
# from abc import ABC,abstractmethod
# class MediaPlayer(ABC):
#     def playAudio(self):
#         print("can play audio")

#     @abstractmethod
#     def playVideo(self):
#         pass

# class SoundRecorder(MediaPlayer):
#     def playVideo(self):
#         print("I can not play video")

# class VLCPlayer(MediaPlayer):
#     def playVideo(self):
#         print("I can play video")

# ob=SoundRecorder()
# ob.playAudio()
# ob.playVideo()


#QUESTION:-
# Shape
# prop:name
# methods:
# 1)PrintParameter
# 2)PrintArea

# a)circle   b)triangle   c)square


#ANSWER:-
# from abc import ABC, abstractmethod
# import math

# # Abstract base class
# class Shape(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def PrintParameter(self):
#         pass

#     @abstractmethod
#     def PrintArea(self):
#         pass


# # Circle subclass
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def PrintParameter(self):
#         perimeter = 2 * math.pi * self.radius
#         print(f"Perimeter of {self.name}: {perimeter:.2f}")

#     def PrintArea(self):
#         area = math.pi * self.radius ** 2
#         print(f"Area of {self.name}: {area:.2f}")


# # Triangle subclass
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         super().__init__("Triangle")
#         self.a = a
#         self.b = b
#         self.c = c

#     def PrintParameter(self):
#         perimeter = self.a + self.b + self.c
#         print(f"Perimeter of {self.name}: {perimeter:.2f}")

#     def PrintArea(self):
#         s = (self.a + self.b + self.c) / 2
#         area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
#         print(f"Area of {self.name}: {area:.2f}")


# # Square subclass
# class Square(Shape):
#     def __init__(self, side):
#         super().__init__("Square")
#         self.side = side

#     def PrintParameter(self):
#         perimeter = 4 * self.side
#         print(f"Perimeter of {self.name}: {perimeter:.2f}")

#     def PrintArea(self):
#         area = self.side ** 2
#         print(f"Area of {self.name}: {area:.2f}")


# # Example usage
# if __name__ == "__main__":
#     c = Circle(5)
#     t = Triangle(3, 4, 5)
#     s = Square(4)

#     for shape in [c, t, s]:
#         print(f"\nShape: {shape.name}")
#         shape.PrintParameter()
#         shape.PrintArea()




#PROGRAM 3
# class Address:
#     def __init__(self,street,city,state,pin):
#         self.street=street
#         self.city=city
#         self.state=state
#         self.pin=pin
#     def printAddress(self):
#         print(f"Street:{Self.street} City:{self.city} State:{self.state} Pin{self.pin}")


# class Student:
#     def __init__(self,sid,name,address):
#         self.sid=sid
#         self.name=name
#         self.address=address

#     def printStudent(self):
#         print(f"Sid:{self.sid} Name:{self.name}")
#         self.address.printAddress()


# class Employee:
#     def __init__(self,sid,name,street,city,state,pin):
#         self.eid=eid
#         self.name=name
#         self.address=address
#     def printEmployee(self):
#         print(f"Sid:{self.sid} Name:{self.name}")
#         self.address.printAddress()

# add=Address("sector-18","noida","up","241000")


# stu=Student(1,"king",add)
# stu.printEmployee()


# stu=Student(1,"james",add)
# stu.printStudent()











