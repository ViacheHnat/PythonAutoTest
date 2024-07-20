class Student:
    def __init__(self, first_name, second_name, age, average_mark):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.average_mark = average_mark

    def change_average_mark(self, average_mark):
        self.average_mark = average_mark


student = Student("Stan", "Lee", 35, 78)
print('Student {} {}, age: {}, average mark: {}'.format(student.first_name, student.second_name, student.age,
                                                        student.average_mark))
student.change_average_mark(89)
print('Student {} {}, age: {}, average mark: {}'.format(student.first_name, student.second_name, student.age,
                                                        student.average_mark))


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:

    def __init__(self):
        self.list_of_book = []

    def add_book(self, title, author):
        self.list_of_book.append(Book(title, author))

    def get_books(self):
        return self.list_of_book




class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

