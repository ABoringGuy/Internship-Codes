import csv
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import os

"""
CONVERSION OF ALL DATABASE TO REQUIRED FORMAT
"""
class Converter(ABC):
    id: str
    CSV_FIELDS = []

    @abstractmethod
    def to_dict(self):
        """Convert object to dictionary for CSV"""
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, obj_id, data):
        """Convert dictionary to object for operations"""
        pass

"""
DATABASE FOR BOOK
"""
class Book:
    CSV_FIELDS= ["title","author","available_quantity","total_quantity"]
    def __init__(self,book_id:str,title:str,author:str,available_quantity:int, total_quantity:int):
        self.id=book_id
        self.title = title
        self.author = author
        self.available_quantity = int(available_quantity)
        self.total_quantity=int(total_quantity)

    @property
    def assigned_quantity(self):
        return self.total_quantity - self.available_quantity

    def __str__(self):
        return f"""({self.id}) Title: {self.title}, Author:{self.author}, Available Quantity: {self.available_quantity}, Total Quantity: {self.total_quantity}"""

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "available_quantity": self.available_quantity,
            "total_quantity": self.total_quantity
        }

    @classmethod
    def from_dict(cls, obj_id, data):
        return cls(obj_id, **data)

"""
DATABASE FOR MEMBERS
"""
class Members:
    CSV_FIELDS= ["first_name","last_name","contact_info"]
    def __init__(self,member_id:str, first_name:str, last_name:str, contact_info:str):
        self.id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.contact_info = contact_info

    def __str__(self):
        return f"""({self.id}) Name: {self.first_name} {self.last_name}, Contact Info: {self.contact_info} """

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "contact_info": self.contact_info
        }

    @classmethod
    def from_dict(cls, obj_id, data):
        return cls(obj_id, **data)

"""
DATABASE FOR ASSIGNMENT
"""
class Assignment:
    CSV_FIELDS = ["book_id", "member_id", "issue_date", "due_date", "return_status"]
    def __init__(self,assignment_id:str, book_id:str, member_id:str, issue_date, due_date, return_status:bool):
        self.id = assignment_id
        self.book_id = book_id
        self.member_id = member_id
        self._issue_date=issue_date
        self._due_date=due_date
        """If we simply do:
        self.return_status=bool(return_status), then true is returned for any data present rather than checking if data is true.
        """
        if isinstance(return_status, str):
            self.return_status=return_status=="True"
        else:
            self.return_status=return_status

    @property
    def issue_date(self):
        return self._issue_date

    @property
    def due_date(self):
        return self._due_date

    def update_dates(self, issue=None, due=None):
        new_issue = issue if issue is not None else self._issue_date
        new_due = due if due is not None else self._due_date

        if new_due <= new_issue:
            return False

        self._issue_date = new_issue
        self._due_date = new_due
        return True

    def __str__(self):
        issue=self.issue_date.strftime("%Y/%m/%d")
        due=self.due_date.strftime("%Y/%m/%d")
        return f"""({self.id}) Book ID:{self.book_id}, Member ID:{self.member_id}, Issue Date:{issue}, Due Date:{due}, Return Status:{self.return_status}"""

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "member_id": self.member_id,
            "issue_date": self.issue_date,
            "due_date": self.due_date,
            "return_status": self.return_status
        }

    @classmethod
    def from_dict(cls, obj_id, data):
        return cls(
            obj_id,
            data["book_id"],
            data["member_id"],
            data["issue_date"],
            data["due_date"],
            data["return_status"]
        )

"""
USED TO LOAD AND STORE THE .CSV FILES
"""
class CSVStorage:
    def load_database(self, filename, id_field, date_fields=None):
        data_dict = {}

        if not os.path.exists(filename):
            return data_dict

        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                key = row[id_field]
                row.pop(id_field)

                if date_fields:
                    for field in date_fields:
                        if field in row:
                            row[field] = datetime.strptime(row[field], "%Y/%m/%d")

                data_dict[key] = row

        return data_dict

    def save_database(self, filename, data_dict, id_field, csv_fields):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=[id_field] + csv_fields)
            writer.writeheader()

            for key, value in data_dict.items():
                data = value.to_dict()
                row = {id_field: key}

                for field in csv_fields:
                    val = data.get(field)
                    if isinstance(val, datetime):
                        val = val.strftime("%Y/%m/%d")

                    row[field] = val

                writer.writerow(row)

"""
PERFORMS OPERATIONS THAT ARE COMMON FOR ALL DATABASE
"""
class DatabaseManager(CSVStorage):
    def __init__(self,filename, id_field, model_class, date_fields=None):
        self.records={}
        self.filename= filename
        self.id_field=id_field
        self.model_class= model_class
        self.date_fields=date_fields
        self.load_data()

    def load_data(self):
        raw_data=self.load_database(self.filename, self.id_field, self.date_fields)

        for obj_id, info in raw_data.items():
            self.records[obj_id] = self.model_class.from_dict(obj_id,info)

    def save_data(self):
        self.save_database(self.filename, self.records, self.id_field, self.model_class.CSV_FIELDS)

    def add_record(self, obj_record):
        self.records[obj_record.id]= obj_record
        self.save_data()

    def get_record(self, obj_id):
        return self.records.get(obj_id)

    def remove(self, obj_id):
        if obj_id in self.records:
            del self.records[obj_id]

            self.save_data()

    def display_all(self):
        if not self.records:
            print("No records found")
            return

        """Note that vars returns a DICT attribute of an object"""
        for obj_record in self.records.values():
            print(obj_record)

    def generate_id(self, prefix):
        if not self.records:
            return f"{prefix}0"

        latest_id = max(
            int(obj_id.replace(prefix, ""))
            for obj_id in self.records.keys()
        )

        return f"{prefix}{latest_id+1}"

"""
PERFORMS ALL DATABASE SPECIFIC OPERATIONS AS WELL AS ACTS AS UI
"""
class System:
    def __init__(self):
        self.books= DatabaseManager("book_database.csv","book_id", Book)
        self.members= DatabaseManager("members_database.csv","member_id", Members)
        self.assignments= DatabaseManager("assignments_database.csv","assignment_id", Assignment,date_fields=["issue_date", "due_date"])

    """
    ALL VALIDATION OPERATIONS
    """
    def check_empty_value(self, prompt:str)->str:
        while True:
            value = input(prompt).strip()
            if not value:
                print("Input cannot be Empty!")
                continue
            break
        return value

    def set_default_value(self, prompt:str)->str:
        value=input(prompt).strip()
        if not value:
            print("No data was given. Setting to 'Unknown'")
            value="Unknown"
        return value

    def check_positive_value(self, prompt:str)->int:
        while True:
            try:
                value=int(input(prompt))
                if value <= 0:
                    print("Value must be positive")
                    continue
                break
            except ValueError:
                print("Value must be an integer")
        return value

    def validate_date(self, date_string):
        try:
            return datetime.strptime(date_string,"%Y/%m/%d")
        except ValueError:
            return None

    def validate_date_range(self, date):
        if not date:
            return False
        return 2000<=date.year<=datetime.now().year+2

    def date_operations(self, prompt, current_value=None):
        value=input(prompt).strip()

        if not value:
            return current_value

        parsed_date= self.validate_date(value)

        if not parsed_date:
            print("Invalid Date Format. Keeping Previous Value")
            return current_value

        if not self.validate_date_range(parsed_date):
            print("Date is out of allowed range. Keeping Previous Value")
            return current_value

        return parsed_date

    def is_member_overdue(self, member_id):
        now=datetime.now()

        for assignment in self.assignments.records.values():
            if assignment.member_id == member_id and not assignment.return_status:
                if assignment.due_date < now:
                    return True
        return False

    def check_overdue_books_of_member(self):
        member_id=input("Enter Member ID: ")
        found=False
        count=0

        for assignment in self.assignments.records.values():
            if assignment.member_id == member_id and not assignment.return_status and assignment.due_date < datetime.now():
                book=self.books.get_record(assignment.book_id)
                if book:
                    count=+1
                    print(f"""({book.id}) Title:{book.title}, Issue Date:{assignment.issue_date}, Due Date:{assignment.due_date}""")
                    found=True

        if not found:
            print("No overdue books found")
            return
        print("Number of Overdue Books:",count)

    def get_all_members_with_overdue_books(self):
        for assignment in self.assignments.records.values():
            if not assignment.return_status and assignment.due_date < datetime.now():
                book=self.books.get_record(assignment.book_id)
                member=self.members.get_record(assignment.member_id)
                print(f"""({assignment.id})Member ID:{member.id}, Name:{member.first_name} {member.last_name}, Book ID:{book.id}, Book Title:{book.title}""")


    """
    ALL INSERTION OPERATIONS
    """
    def add_book(self):
        book_id=self.books.generate_id("BID")

        if self.books.get_record(book_id):
            print("Book ID already exists")
            return

        title= self.check_empty_value("Input Book Title: ")
        author= self.set_default_value("Input Author Name: ")
        total_quantity=self.check_positive_value("Input Total Quantity: ")
        available_quantity=total_quantity

        books = Book(book_id, title, author, available_quantity, total_quantity)
        self.books.add_record(books)

        print("Book added successfully")

    def add_member(self):
        member_id = self.members.generate_id("MID")

        if self.members.get_record(member_id):
            print("Member ID already exists")
            return

        first_name = self.check_empty_value("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        contact_info = self.set_default_value("Enter Contact Info: ")

        members= Members(member_id, first_name, last_name, contact_info)
        self.members.add_record(members)
        print("Member added successfully")


    def add_assignment(self):
        assignment_id = self.assignments.generate_id("ASS_ID")

        if self.assignments.get_record(assignment_id):
            print("Assignment ID already exists")
            return

        book_id = input("Enter Borrowed Book ID: ")
        books = self.books.get_record(book_id)
        if not books:
            print("Book doesn't exist")
            return

        member_id = input("Enter Borrowed Member ID: ")
        members = self.members.get_record(member_id)
        if not members:
            print("Member doesn't exist")
            return

        if self.is_member_overdue(member_id):
            print("Member has overdue books. Cannot assign books before returning previous books")
            return

        issue_date=self.date_operations("Enter Issue Date(YYYY/MM/DD): ")
        if not issue_date:
            issue_date=datetime.now()
        due_date=self.date_operations("Enter Due Date(YYYY/MM/DD): ")
        if due_date is None or due_date <= issue_date:
            print("Invalid or past Due Date. Setting +14 days from Issue Date.")
            due_date = issue_date + timedelta(days=14)
        return_status=False

        if books.available_quantity<=0:
            print("All Books are Booked(pun intended)")
        else:
            books.available_quantity-=1
            self.books.save_data()
            assignments=Assignment(assignment_id, book_id, member_id, issue_date, due_date, return_status)
            self.assignments.add_record(assignments)
            print("Assignment added successfully")

    """
    ALL UPDATE OPERATIONS
    """
    def update_assignment_status(self):
        assignment_id = input("Enter Assignment ID: ")
        assignment=self.assignments.get_record(assignment_id)
        book= self.books.get_record(assignment.book_id)

        if not assignment.return_status:
            assignment.return_status = True
            book.available_quantity+=1
            self.books.save_data()
            self.assignments.save_data()

    def update_issue_dates(self):
        assignment_id=input("Enter Assignment ID: ")
        assignment=self.assignments.get_record(assignment_id)
        if not assignment:
            print("Assignment doesn't exist")
            return
        new_issue_date = self.date_operations("Enter New Issue Date(YYYY/MM/DD): ")
        if not assignment.update_dates(issue=new_issue_date):
            print("Invalid update: Issue date must be before due date")
        else:
            self.assignments.save_data()

    def update_due_date(self):
        assignment_id=input("Enter Assignment ID: ")
        assignment=self.assignments.get_record(assignment_id)
        if not assignment:
            print("Assignment doesn't exist")
            return
        new_due_date = self.date_operations("Enter New Due Date(YYYY/MM/DD): ")
        if not assignment.update_dates(due=new_due_date):
            print("Invalid update: Due date must be after issue date")
        else:
            self.assignments.save_data()

    def update_book_details(self):
        book_id = input("Enter Book ID: ")
        book = self.books.get_record(book_id)
        if not book:
            print("Book doesn't exist")
            return
        choice = input(f"""What do you want to change?
[1] Book Name
[2] Author Name
[3] Total Quantity

Choice=""")
        match choice:
            case "1":
                new_title = self.check_empty_value("Enter new Book Name: ")
                book.title = new_title
                self.books.save_data()
            case "2":
                new_author = self.set_default_value("Enter new Book Author: ")
                book.author = new_author
                self.books.save_data()
            case "3":
                new_quantity = self.check_positive_value("Enter number of Book Quantity: ")
                book.total_quantity += new_quantity
                book.available_quantity += new_quantity
                self.books.save_data()
            case _:
                print("Invalid Choice")

    def update_member_details(self):
        member_id = input("Enter Member ID: ")
        member = self.members.get_record(member_id)
        if not member:
            print("Member doesn't exist")
            return

        choice = input(f"""What do you want to change?
        [1] Member Fist Name
        [2] Member Last Name
        [3] Member Contact Information

        Choice=""")

        match choice:
            case "1":
                new_first_name = self.check_empty_value("Enter new First Name: ")
                member.first_name = new_first_name
                self.members.save_data()
            case "2":
                new_last_name = input("Enter new Last Name: ")
                member.last_name = new_last_name
                self.members.save_data()
            case "3":
                new_contact = self.set_default_value("Enter new Contact Information: ")
                member.contact_info = new_contact
                self.members.save_data()
            case _:
                print("Invalid Choice")


    """
    ALL SEARCH OPERATIONS
    """
    def get_active_assignment(self):
        active_assignments= []
        for assignment in self.assignments.records.values():
            if not assignment.return_status:
                active_assignments.append(assignment)
        return active_assignments

    def search_assigned_members(self):
        assigned_member_id = set()
        for assignment in self.get_active_assignment():
            assigned_member_id.add(assignment.member_id)

        for member in self.members.records.values():
            if member.id in assigned_member_id:
                print(member)

    def search_not_assigned_members(self):
        assigned_members_id=set()#Created a Set because of fast search
        for assignment in self.get_active_assignment():
            assigned_members_id.add(assignment.member_id)

        for member in self.members.records.values():
            if member.id not in assigned_members_id:
                print(member)

    def search_book(self):
        book_id = input("Enter Book ID to search: ")
        book=self.books.get_record(book_id)

        if book:
            print(book)
        else:
            print("Book doesn't exist")

    def search_member(self):
        member_id = input("Enter Member ID to search: ")
        member=self.members.get_record(member_id)

        if member:
            print(member)
        else:
            print("Member doesn't exist")

    def search_assignment(self):
        assignment_id = input("Enter Assignment ID: ")
        assignment=self.assignments.get_record(assignment_id)

        if assignment:
            print(assignment)
        else:
            print("Assignment doesn't exist")

    def get_assigned_books(self):
        for book in self.books.records.values():
            if book.available_quantity!=book.total_quantity:
                print(book)
                print("The total assigned book is:",book.assigned_quantity)

    def get_unassigned_books(self):
        for book in self.books.records.values():
            if book.available_quantity==book.total_quantity:
                print(book)

    def get_all_books(self):
        self.books.display_all()

    def get_all_members(self):
        self.members.display_all()

    def get_all_assignments(self):
        self.assignments.display_all()

    def get_all_books_member_has(self):
        member_id=input("Enter Member ID: ")
        for assignment in self.assignments.records.values():
            if assignment.member_id==member_id and not assignment.return_status:
                book = self.books.get_record(assignment.book_id)
                print(book)

    def get_all_members_who_has_book(self):
        book_id=input("Enter Book ID: ")
        for assignment in self.assignments.records.values():
            if assignment.book_id==book_id and not assignment.return_status:
                member=self.members.get_record(assignment.member_id)
                print(member)


    """
    ALL DELETE OPERATIONS
    """
    def remove_book_by_id(self):
        book_id = input("Enter Book ID: ")
        for assignment in self.assignments.records.values():
            if assignment.book_id == book_id and not assignment.return_status:
                print("Cannot Delete Book")
                return
        self.books.remove(book_id)
        self.books.save_data()

    def remove_member_by_id(self):
        member_id = input("Enter Member ID: ")
        for assignment in self.assignments.records.values():
            if assignment.member_id == member_id and not assignment.return_status:
                print("Cannot Delete Member")
                return
        self.members.remove(member_id)
        self.members.save_data()


    """
    ALL MENU OPERATIONS
    """
    def main_menu(self):
        while True:
            print("""Welcome to the Library Management System!
            [1]Manage Books
            [2]Manage Members
            [3]Manage Assignments
            [4]Exit""")
            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    self.book_menu()
                case "2":
                    self.member_menu()
                case "3":
                    self.assignment_menu()
                case "4":
                    exit()
                case _:
                    print("Invalid Choice")


    def book_menu(self):
        while True:
            choice=input("""You have entered Book Management System!
            [1] Add Book
            [2] Update Book Details
            
            [3] View All Books
            [4] View All Unassigned Books
            [5] View All Assigned Books
            
            [6] Search Book Details
            
            [7] Remove Book Permanently
            [8] Search Members Who Has Book
            
            [9] Return to Main Menu
            [10] Exit
            
            Enter your choice:
            """)

            match choice:
                case "1":
                    self.add_book()
                case "2":
                    self.update_book_details()
                case "3":
                    self.get_all_books()
                case "4":
                    self.get_unassigned_books()
                case "5":
                    self.get_assigned_books()
                case "6":
                    self.search_book()
                case "7":
                    self.remove_book_by_id()
                case "8":
                    self.get_all_members_who_has_book()
                case "9":
                    return
                case "10":
                    exit()
                case _:
                    print("Invalid Choice")

    def member_menu(self):
        while True:
            choice=input("""You have entered Member Management System!
            [1] Add Member
            [2] Update Member
            
            [3] View All Members
            [4] View All Members With Due Books
            [5] View All Members With No Due Books
            
            [6] Search Member
            [7] Search Books that Member has Due
            
            [8] Permanently Remove Member
            
            [9] Return to Main Menu
            [10] Exit
            
            Enter your choice:""")

            match choice:
                case "1":
                    self.add_member()
                case "2":
                    self.update_member_details()
                case "3":
                    self.get_all_members()
                case "4":
                    self.search_assigned_members()
                case "5":
                    self.search_not_assigned_members()
                case "6":
                    self.search_member()
                case "7":
                    self.get_all_books_member_has()
                case "8":
                    self.remove_member_by_id()
                case "9":
                    return
                case "10":
                    exit()
                case _:
                    print("Invalid Choice")

    def assignment_menu(self):
        while True:
            choice=input("""You have entered Assignment Management System!
            [1] Add Assignment
            [2] Update Return Status of Books
            [3] Update Issue Date
            [4] Update Due Date
            
            [5] View All Assignments
            [6] View All Overdue Books of Members
            [7] View All Members with Overdue Books
            
            [7] Return to Main Menu
            [8] Exit
            
            Enter your choice:""")

            match choice:
                case "1":
                    self.add_assignment()
                case "2":
                    self.update_assignment_status()
                case "3":
                    self.update_issue_dates()
                case "4":
                    self.update_due_date()
                case "5":
                    self.get_all_assignments()
                case "6":
                    self.check_overdue_books_of_member()
                case "7":
                    self.get_all_members_with_overdue_books()
                case "8":
                    return
                case "9":
                    exit()
                case _:
                    print("Invalid Choice")


run_system=System()
run_system.main_menu()