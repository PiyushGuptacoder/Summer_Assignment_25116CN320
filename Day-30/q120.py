

titles = []
authors = []
status = []   

def add_book(title, author):
    titles.append(title)
    authors.append(author)
    status.append("Available")
    print("Book added.")

def display_books():
    if not titles:
        print("No books in library.")
        return
    
    for i in range(len(titles)):
        print(f" {titles[i]} by {authors[i]} - {status[i]}")
        print("\n")
              

def search_book(title):
    if title in titles:
        i = titles.index(title)
        print(f"Found → {titles[i]} by {authors[i]} - {status[i]}")
    else:
        print("Book not found.")

def issue_book(title):
    if title in titles:
        i = titles.index(title)
        if status[i] == "Available":
            status[i] = "Issued"
            print("Book issued.")
        else:
            print("Already issued.")
    else:
        print("Book not found.")

def return_book(title):
    if title in titles:
        i = titles.index(title)
        status[i] = "Available"
        print("Book returned.")
    else:
        print("Book not found.")

# Menu-driven loop
while True:
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        t = input("Enter Title: ")
        aut = input("Enter Author: ")
        add_book(t, aut)
    elif choice == "2":
        display_books()
    elif choice == "3":
        t = input("Enter Title to search: ")
        search_book(t)
    elif choice == "4":
        t = input("Enter Title to issue: ")
        issue_book(t)
    elif choice == "5":
        t = input("Enter Title to return: ")
        return_book(t)
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")
