# QUESTION 1
# import json
# import os

# FILE_NAME = "students.json"
# def load_data():
#     if os.path.exists(FILE_NAME):
#         with open(FILE_NAME, "r") as f:
#             return json.load(f)
#     return {}

# def save_data(data):
#     with open(FILE_NAME, "w") as f:
#         json.dump(data, f)

# def add_student(students):
#     roll = input("Enter Roll Number: ")
#     if roll in students:
#         print("Student already exists!")
#         return
#     name = input("Enter Name: ")
#     marks = []
#     for i in range(1, 6):
#         m = int(input(f"Enter marks for subject {i}: "))
#         marks.append(m)
#     students[roll] = {"name": name, "marks": marks}
#     print("Student added successfully!")

# def display_students(students):
#     if not students:
#         print("No student records found!")
#         return
#     for roll, info in students.items():
#         total = sum(info["marks"])
#         avg = total / 5
#         grade = get_grade(avg)
#         print("\nRoll No:", roll)
#         print("Name:", info["name"])
#         print("Marks:", info["marks"])
#         print("Total:", total)
#         print("Average:", round(avg, 2))
#         print("Grade:", grade)

# def get_grade(avg):
#     if avg >= 90:
#         return "A+"
#     elif avg >= 80:
#         return "A"
#     elif avg >= 70:
#         return "B"
#     elif avg >= 60:
#         return "C"
#     elif avg >= 50:
#         return "D"
#     else:
#         return "F"

# def search_student(students):
#     if not students:
#         print("No records to search!")
#         return
#     choice = input("Search by (1) Roll No or (2) Name: ")
#     if choice == "1":
#         roll = input("Enter Roll Number: ")
#         if roll in students:
#             info = students[roll]
#             total = sum(info["marks"])
#             avg = total / 5
#             print("\nName:", info["name"])
#             print("Marks:", info["marks"])
#             print("Total:", total)
#             print("Average:", round(avg, 2))
#         else:
#             print("Student not found!")
#     elif choice == "2":
#         name = input("Enter Name: ").lower()
#         found = False
#         for roll, info in students.items():
#             if info["name"].lower() == name:
#                 total = sum(info["marks"])
#                 avg = total / 5
#                 print("\nRoll No:", roll)
#                 print("Marks:", info["marks"])
#                 print("Total:", total)
#                 print("Average:", round(avg, 2))
#                 found = True
#         if not found:
#             print("Student not found!")
#     else:
#         print("Invalid choice!")

# def update_marks(students):
#     roll = input("Enter Roll Number to update: ")
#     if roll not in students:
#         print("Student not found!")
#         return
#     marks = []
#     for i in range(1, 6):
#         m = int(input(f"Enter new marks for subject {i}: "))
#         marks.append(m)
#     students[roll]["marks"] = marks
#     print("Marks updated successfully!")

# def delete_student(students):
#     roll = input("Enter Roll Number to delete: ")
#     if roll in students:
#         del students[roll]
#         print("Student deleted successfully!")
#     else:
#         print("Student not found!")

# def show_topper(students):
#     if not students:
#         print("No student records found!")
#         return
#     highest_avg = 0
#     toppers = []
#     for roll, info in students.items():
#         avg = sum(info["marks"]) / 5
#         if avg > highest_avg:
#             highest_avg = avg
#             toppers = [roll]
#         elif avg == highest_avg:
#             toppers.append(roll)
#     print("\n--- Class Topper(s) ---")
#     for roll in toppers:
#         print(f"{students[roll]['name']} (Roll No: {roll}) - Avg: {round(highest_avg, 2)}")

# def main():
#     students = load_data()

#     while True:
#         print("\n===== Student Result Management System =====")
#         print("1. Add Student")
#         print("2. Display All Students")
#         print("3. Search Student")
#         print("4. Update Marks")
#         print("5. Delete Student")
#         print("6. Show Class Topper")
#         print("7. Save & Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_student(students)
#         elif choice == "2":
#             display_students(students)
#         elif choice == "3":
#             search_student(students)
#         elif choice == "4":
#             update_marks(students)
#         elif choice == "5":
#             delete_student(students)
#         elif choice == "6":
#             show_topper(students)
#         elif choice == "7":
#             save_data(students)
#             print("Data saved. Exiting program.")
#             break
#         else:
#             print("Invalid choice! Try again.")

# if __name__ == "__main__":
#     main()



#QUESTION 2
import json
import os
from datetime import date
BOOKS_FILE = "books.json"
ISSUED_FILE = "issued_books.json"

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)

def add_book(books):
    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("Book already exists!")
        return
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    genre = input("Enter Genre: ")
    copies = int(input("Enter Number of Copies: "))
    books[book_id] = {"title": title, "author": author, "genre": genre, "copies": copies}
    print("Book added successfully!")

def display_books(books):
    if not books:
        print("No books in library!")
        return
    for bid, info in books.items():
        print("\nBook ID:", bid)
        print("Title:", info["title"])
        print("Author:", info["author"])
        print("Genre:", info["genre"])
        print("Copies:", info["copies"])

def search_book(books):
    if not books:
        print("No books to search!")
        return
    choice = input("Search by (1) Title or (2) Author: ")
    keyword = input("Enter search word: ").lower()
    found = False
    for bid, info in books.items():
        if (choice == "1" and keyword in info["title"].lower()) or \
           (choice == "2" and keyword in info["author"].lower()):
            print("\nBook ID:", bid)
            print("Title:", info["title"])
            print("Author:", info["author"])
            print("Genre:", info["genre"])
            print("Copies:", info["copies"])
            found = True
    if not found:
        print("No matching books found!")

def issue_book(books, issued):
    book_id = input("Enter Book ID to issue: ")
    if book_id not in books:
        print("Book not found!")
        return
    if books[book_id]["copies"] <= 0:
        print("No copies left!")
        return
    student = input("Enter Student Name: ")
    books[book_id]["copies"] -= 1
    today = str(date.today())
    if today not in issued:
        issued[today] = []
    issued[today].append({"book_id": book_id, "title": books[book_id]["title"], "student": student})
    print("Book issued successfully!")

def return_book(books):
    book_id = input("Enter Book ID to return: ")
    if book_id not in books:
        print("Book not found!")
        return
    books[book_id]["copies"] += 1
    print("Book returned successfully!")

def books_by_genre(books):
    if not books:
        print("No books available!")
        return
    genre_name = input("Enter Genre: ").lower()
    found = False
    for bid, info in books.items():
        if info["genre"].lower() == genre_name:
            print("\nBook ID:", bid)
            print("Title:", info["title"])
            print("Author:", info["author"])
            print("Copies:", info["copies"])
            found = True
    if not found:
        print("No books found for that genre.")

def delete_zero_copies(books):
    to_delete = []
    for bid, info in books.items():
        if info["copies"] == 0:
            to_delete.append(bid)
    for bid in to_delete:
        del books[bid]
    print(len(to_delete), "book(s) deleted with zero copies.")

def books_issued_today(issued):
    today = str(date.today())
    if today not in issued or not issued[today]:
        print("No books issued today.")
        return
    print("\nBooks Issued Today:")
    for record in issued[today]:
        print(f"Book ID: {record['book_id']}, Title: {record['title']}, Student: {record['student']}")

def main():
    books = load_data(BOOKS_FILE)
    issued = load_data(ISSUED_FILE)

    while True:
        print("\n===== Library Book Inventory System =====")
        print("1. Add New Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Show Books by Genre")
        print("7. Delete Books with Zero Copies")
        print("8. Books Issued Today Report")
        print("9. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            display_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            issue_book(books, issued)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            books_by_genre(books)
        elif choice == "7":
            delete_zero_copies(books)
        elif choice == "8":
            books_issued_today(issued)
        elif choice == "9":
            save_data(BOOKS_FILE, books)
            save_data(ISSUED_FILE, issued)
            print("All changes saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
