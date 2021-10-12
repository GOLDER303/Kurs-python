class Book: 

    def __init__(self, author, title, borrow_status = False):
        self.author = author
        self.title = title
        self.borrow_status = borrow_status

    def get_borrow_status(self):
        return "Wypożyczona" if self.borrow_status == 1 else "Niewypożyczona"


        
