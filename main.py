from books import Books

book = Books()

print("Welcome to the Library!")
while True:
    user_choice = int(input("You have these options at your disposal: \n"
                            "0 - add a book\n"
                            "1 - take a book\n"
                            "2 - turn in a book\n"
                            "3 - list of all books\n"
                            "4 - list of currently available books\n"
                            "5 - list of unavailable books\n"
                            "6 - return a book\n"))
    if user_choice == 0:
        book.add_book()
    elif user_choice == 1:
        book.hand_out_the_book()
    elif user_choice == 2:
        book.return_book()
    elif user_choice == 3:
        book.show_our_books()
    elif user_choice == 4:
        book.show_current_books()
    elif user_choice == 5:
        book.books_are_being_read()
    else:
        book.return_book()
    user_choice_2 = input("Would you like to continue using our library?Yes or No?\n").lower()
    if user_choice == "no":
        break
