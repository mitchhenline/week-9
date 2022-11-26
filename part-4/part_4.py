### Step 1 - Input function

## Create five input statements to gather user's book they want to 
# input to the system. After that be sure to turn it into a function.

# Code here
# def create_new_book():
#     title = input("What book do you want to add? - ")
#     author = input("Who is the author? - ")
#     pages = input("How many pages is the book? - ")
#     rating = input("What is the book's rating? - ")
#     year = input("What year was the book published? - ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "pages": pages,
#         "rating": rating,
#         "pages": pages,
#         "year": year
#     }

#     return book_dictionary


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. 
# Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

def create_new_book_2():
    title = input("What book do you want to add? - ")
    author = input("Who is the author? - ")
    pages = int(input("How many pages is the book? - "))
    rating = float(input("What is the book's rating? - "))
    year = int(input("What year was the book published? - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "pages": pages,
        "rating": rating,
        "pages": pages,
        "year": year
    }

    return book_dictionary

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user 
# type an answer that doesn't convert data-type properly.

# Code here

def create_new_book_3():
    title = input("What book do you want to add? - ")
    author = input("Who is the author? - ")
    try:
        pages = int(input("How many pages is the book? - "))
    except:
        pages = int(input("Please put in a number for pages - "))
    try:
        rating = float(input("What is the book's rating? - "))
    except:
        rating = float(input("Please enter a number between 0 and 5 - "))
    try:
        year = int(input("What year was the book published? - "))
    except:
        year = int(input("Please enter a number using digits (0-9) - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "pages": pages,
        "rating": rating,
        "pages": pages,
        "year": year
    }

    return book_dictionary

# print(create_new_book_3())

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. 
# Handle their choices with if/elif/else statements.

# Code here


# def menu(book_db):

#     select = input("Type '1' to enter a new book or type '2' to see all books. Type '3' to quit. - ")

#     if input == "1":
#         book_db.append(create_new_book())
#     elif input == "2":
#         print_books(book_db)
#     elif input == "3":
#         print('\nThanks and Goodbye!')
#         active = False
#     else:
#         print("\nPlease enter a '1', '2' or '3'")





# def create_new_book():
#     title = input("What book do you want to add? - ")
#     author = input("Who is the author? - ")
#     pages = input("How many pages is the book? - ")
#     rating = input("What is the book's rating? - ")
#     year = input("What year was the book published? - ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "pages": pages,
#         "rating": rating,
#         "pages": pages,
#         "year": year
#     }

#     return book_dictionary
        


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, 
# and continually asking for input until the user chooses to exit the program. 
# Call the main menu to ensure it functions properly.

# Code here

books = [
{
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
},
{
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "year": 1951,
    "rating": 4.9,
    "pages": 234
},
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "rating": 4.7,
    "pages": 208
}
]

def create_new_book():
    title = input("What book do you want to add? - ")
    author = input("Who is the author? - ")
    pages = input("How many pages is the book? - ")
    rating = input("What is the book's rating? - ")
    year = input("What year was the book published? - ")

    book_dictionary = {
        "title": title,
        "author": author,
        "pages": pages,
        "rating": rating,
        "pages": pages,
        "year": year
    }

    return book_dictionary

def print_books(book_list):

    for books in book_list:
        title = books["title"]
        author = books["author"]
        year = books["year"]
        rating = books["rating"]
        pages = books["pages"]

        print (f"Book title: {title}, Author:{author}, Year published:{year}, Rating:{rating}, Page count:{pages} ")




def menu(book_db):

    active = True

    while active:

        select = input("Type '1' to enter a new book or type '2' to see all books. Type '3' to quit. - ")

        if select == "1":
            book_db.append(create_new_book())
        elif select == "2":
            print_books(book_db)
        elif select == "3":
            print('\nThanks and Goodbye!')
            active = False
        else:
            print("\nPlease enter a '1', '2' or '3'")

menu(books)



