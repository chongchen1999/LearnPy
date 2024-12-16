import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


for path in sys.path:
    print(path)

# from library import books, members, transactions
import library.books as books
import library.members as members
import library.transactions as transactions

# Using the books module
books.add_book("1984", "George Orwell")
books.list_books()

# Using the members module
members.add_member("Alice")
members.list_members()

# Using the transactions module
transactions.borrow_book("Alice", "1984")
transactions.return_book("Alice", "1984")
