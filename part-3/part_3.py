my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

catcher_book = {
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "year": 1951,
    "rating": 4.9,
    "pages": 234
}

gatsby_book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "rating": 4.7,
    "pages": 208
}

# Follow the instructions in this part of the project. Define and flesh out your function below, 
# which should accept a dictionary as an argument when called, 
# and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_info(book_dict):
    book_str = f"{book_dict['author']} wrote {book_dict['title']} in {book_dict['year']}. It is {book_dict['pages']} pages long and has a rating of {book_dict['rating']}."
    return book_str

print(book_info(catcher_book))
# Once you are finished with that function, create several more functions which return individual 
# pieces of information from the book.

# Code below

def book_title(book_dict):
    title_str = f"The name of the book is {book_dict['title']}."
    return title_str

print(book_title(my_book))

def book_author(book_dict):
    author_str = f"The author of the book is {book_dict['author']}."
    return author_str

print(book_author(my_book))

def published_year(book_dict):
    published_str = f"The book was first published in {book_dict['year']}."
    return published_str

print(published_year(gatsby_book))


# Finally, create at least three new functions that might be useful as we expand our home library app. 
# Perhaps thing of a way you could accept additional arguments when the function is called? 
# Also, imagine you have a list filled with dictionaries like above.

# Code below

    #A function that takes your current page number and tells you how many pages left to go til finished
def pages_left (book_dict, current_page_number):
    pages_remaining = (book_dict['pages'] - current_page_number)
    pr_str = f"You have {pages_remaining} left to read until finished."
    return pr_str
print(pages_left(catcher_book, 57))


    # A function that takes in dictionaries of books and returns a string stating the highest rated
def highest_rated_book(*args):
    high_rating = args[0]
    for book_dict in args:
        if book_dict['rating'] > high_rating['rating']:
            high_rating = book_dict
    return f"The highest-rated book is {high_rating['title']}"

print (highest_rated_book(my_book, catcher_book, gatsby_book))

    # A function that takes in dictionaries of books and returns a string stating the oldest and year published
def earliest_published(*args):
    earliest_year = args[0]
    for book_dict in args:
        if book_dict['year'] < earliest_year['year']:
            earliest_year = book_dict
    return f"The oldest book in the list is {earliest_year['title']} which was published in {earliest_year['year']}."

print (earliest_published(my_book, gatsby_book, catcher_book))