from .user import User
from .book import Book

class Library:

    def __init__(self):
        self.user_list = []
        self.book_list = []

    def add_user(self, name, surname):
        user = User(name, surname)
        self.user_list.append(user)

    def delete_user(self):
        pass

    def add_book(self, author, title):
        pass

    def delete_book(self):
        pass

    def get_book_list(self):
        pass

    def get_user_list(self):
        print(self.user_list[0].get_user_data())

