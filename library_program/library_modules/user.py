class User: 

    def __init__(self, name, surname, book_list = []):
        self.name = name
        self.surname = surname
        self.book_list = book_list

    def borrow_book(self, book):
        pass

    def return_book(self):
        pass

    def get_user_data(self):
        return f"{self.name} {self.surname}"
