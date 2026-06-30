import csv

filename = "library.csv"
library = {}

def load_from_csv():
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                library[row["stdid"]] = row
    except FileNotFoundError:
        pass

def save_to_csv():
    with open(filename, "w", newline="") as f:
        fieldnames = ["stdid", "name", "booksissued","doi", "booksreturned", "dor", "Latefine"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for book in library.values():
            writer.writerow(book)

def issue_book():
    stdid = input("Enter student ID: ")
    if stdid in library:
        bookissued = int(input("Enter number of books issued: "))
        doi = str(input("Enter date of issue: "))
        # bookreturned = float(input("Enter number of books returned: "))
        # dor = str(input("Enter date of returnen: "))
        latefine = float(input("Enter late fine: "))
        
        
    name = input("Enter Name: ")
    bookissued = int(input("Enter number of books issued: "))
    doi = str(input("Enter date of issue: "))
    # bookreturned = float(input("Enter number of books returned: "))
    # dor = float(input("Enter date of returnen: "))
    latefine = float(input("Enter late fine: "))

    library[stdid] = {
        "stdid": stdid, "name": name,
        "booksissued": bookissued, "doi": doi,
        "booksreturned": 00, "dor": 00, "Latefine":latefine
    }
    save_to_csv()
    print("Book record added successfully.")

def display_library():
    if not library:
        print("No records found.")
    else:
        for book in library.values():
            print(book)

def returned_book():
    stdid = input("Enter student ID to search: ")
    if stdid in library:
        # bookissued = float(input("Enter number of books issued: "))
        # doi = float(input("Enter date of issue: "))
        bookreturned = int(input("Enter number of books returned: "))
        dor = str(input("Enter date of returnen: "))
        latefine = float(input("Enter late fine: "))
        
        
    name = input("Enter Name: ")
    # bookissued = float(input("Enter number of books issued: "))
    # doi = float(input("Enter date of issue: "))
    bookreturned = int(input("Enter number of books returned: "))
    dor = str(input("Enter date of returnen: "))
    latefine = float(input("Enter late fine: "))

    library[stdid] = {
        "stdid": stdid, "name": name,
        "booksissued": 00, "doi": 00,
        "booksreturned": 00, "dor": 00, "Latefine":latefine
    }
    save_to_csv()
    print("Book record added successfully.")

def update_library():
    stdid = input("Enter student ID to update: ")
    if stdid in library:
        name = input("Enter new Name: ")
        bookissued = int(input("Enter number of books issued: "))
        doi = str(input("Enter date of issue: "))
        bookreturned = int(input("Enter number of books returned: "))
        dor = str(input("Enter date of returnen: "))
        latefine = float(input("Enter late fine: "))

        library[stdid] = {
            "stdid": stdid, "name": name,
            "booksissued":bookissued, "doi": doi,
            "booksreturned": bookreturned, "dor": dor, "Latefine":latefine
        }
        save_to_csv()
        print("Book record updated.")
    else:
        print("Record not found.")

def delete_book_record():
    stdid = input("Enter Student ID to delete: ")
    if stdid in library:
        del library[stdid]
        save_to_csv()
        print("Book record deleted.")
    else:
        print("Record not found.")

def main():
    load_from_csv()
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book Record")
        print("2. Display Book Records")
        print("3. Return Book ")
        print("4. Update Book Record")
        print("5. Delete Book Record")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            issue_book()
        elif choice == "2":
            display_library()
        elif choice == "3":
            returned_book()
        elif choice == "4":
            update_library()
        elif choice == "5":
            delete_book_record()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
