class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def show_info(self):
        print("Name:", self.name)
        print("Member ID:", self.member_id)


class StudentMember(Member):
    def __init__(self, name, member_id, grade):
        super().__init__(name, member_id)
        self.grade = grade

    def show_info(self):
        print("Name:", self.name)
        print("Member ID:", self.member_id)
        print("Grade:", self.grade)
        print("Borrow Limit: 3 books")


class TeacherMember(Member):
    def __init__(self, name, member_id, department):
        super().__init__(name, member_id)
        self.department = department

    def show_info(self):
        print("Name:", self.name)
        print("Member ID:", self.member_id)
        print("Department:", self.department)
        print("Borrow Limit: 5 books")


s1 = StudentMember("Rahul", 101, "10th")
t1 = TeacherMember("Dr. Mehta", 201, "Computer Science")

print("Student Member Details:")
s1.show_info()

print("\nTeacher Member Details:")
t1.show_info()



