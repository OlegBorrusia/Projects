class Books:
    storage = {}
    default_storage = {}
    with open("List_of_books.txt", "r") as file:
        list_books = file.readlines()
        for x in list_books:
            y = x.strip()
            storage[list_books.index(x)] = y.split(",")
            default_storage[list_books.index(x)] = y.split(",")
    books_out = {}

    def __init__(self):
        self.book_id = 0
        self.book_name = "book_name"
        self.book_author = "book_author"
        self.book_year = 0
        self.book_info = [self.book_name, self.book_author, self.book_year]

    def add_book(self):
        """ Adds book to the library"""
        try:
            self.book_name = input("What's the name of the book?\n")
            self.book_author = input("Who is the author of the book?\n")
            self.book_id = len(Books.storage)
            self.book_year = int(input("When was it published?\n"))
            Books.storage[self.book_id] = self.book_info
            Books.default_storage[self.book_id] = self.book_info
            print("New book has been added to the library")
        except ValueError:
            print("Check the data types of text you are entering. Years and ids are numbers and the rest is string!")
            self.add_book()

    def delete_the_book(self):
        """ Deletes item from the Library"""
        try:
            book_id = int(input("What book to delete? Enter its id number.\n"))
            del Books.storage[book_id]
            del Books.default_storage[book_id]
        except ValueError:
            print("Check the data types of text you are entering. Years and ids are numbers and the rest is string!")
            Books.delete_the_book(self)

    def hand_out_the_book(self):
        """ Hands out a book to a reader after he gives his Id"""
        unavailable = 0
        try:
            reader_id = int(input("Enter your id?\n"))
            Books.books_out[reader_id] = []
            choice = input("How would you like to find the book you need?Enter A by author or enter N by name: \n").lower()
            if choice == "n":
                book_name = input("Enter the name of the book? \n")
                for key in Books.default_storage:
                    if book_name == Books.default_storage[key][0]:
                        Books.books_out[reader_id].append(key)
                        del Books.storage[key]
                        print("The book has been handed out to a reader!")
                    else:
                        unavailable += 1
                if unavailable == len(Books.default_storage):
                    print("The book you are trying to find is not available. Enter another one.")
            else:
                book_author = input("Enter the author of the book? \n")
                for key in Books.default_storage:
                    if book_author != Books.default_storage[key][1]:
                        unavailable += 1
                    else:
                        Books.books_out[reader_id].append(key)
                        del Books.storage[key]
                        print("The book has been handed out to a reader!")
                if unavailable == len(Books.default_storage):
                    print("The book you are trying to find is not available. Enter another one.")
        except ValueError:
            print("Check the data types of text you are entering. Years and ids are numbers and the rest is string!")
            Books.hand_out_the_book(self)

    def return_book(self):
        what_book_to_return = input("What book would you like to return? \n")
        book_id_to_return = 0
        for key in Books.default_storage:
            if what_book_to_return == Books.default_storage[key][0]:
                book_id_to_return = key
        for key in Books.books_out:
            if book_id_to_return in Books.books_out[key]:
                Books.books_out[key].remove(book_id_to_return)
        print("The book has been returned!")
        Books.storage[book_id_to_return] = Books.default_storage[book_id_to_return]
        for key in Books.storage:
            print(", ".join(Books.storage[key]))

    def show_current_books(self):
        print(f"These are the books we have at the moment: \n")
        for key in Books.storage:
            print(", ".join(Books.storage[key]))

    def show_our_books(self):
        print(f"These are the books we possess: \n")
        for key in Books.default_storage:
            print(", ".join(Books.default_storage[key]))

    def books_are_being_read(self):
        print(f"These are the books that are being read right now by our users: \n")
        for key in Books.books_out:
            for x in Books.books_out[key]:
                print(", ".join(Books.default_storage[x]))

# book.add_book()
# book.hand_out_the_book()
# print(Books.books_out)
# book.return_book()
# print(Books.books_out)
# book.hand_out_the_book()
