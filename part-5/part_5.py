### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. 
# Follow the instructions to create and call a function to add a book, based off of the previous dictionaries 
# for our library, to the .txt file properly formatted with commas as separators.

# Code here

def create_new_book():
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

    with open("mitchlibrary.txt", "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library,
#  but gets the info from a list, and make it work by reading the information in your home 
# library's .txt document. This will take some new logic, but you can do it.

# Code here

def print_books():
    
    with open("mitchlibrary.txt", "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")
       
        print (f"Book title: {title}, Author:{author}, Year published:{year}, Rating:{rating}, Page count:{pages} ")


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't 
# accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

def menu():

    active = True

    while active:

        select = input("Type '1' to enter a new book or type '2' to see all books. Type '3' to quit. - ")

        if select == "1":
            create_new_book()
        elif select == "2":
            print_books()
        elif select == "3":
            print('\nThanks and Goodbye!')
            active = False
        else:
            print("\nPlease enter a '1', '2' or '3'")

menu()


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code.
#  Make your application functional. Great job getting your first Python application finished!




# # if __name__ == “__main__”:
#     menu("mitchlibrary.txt")

