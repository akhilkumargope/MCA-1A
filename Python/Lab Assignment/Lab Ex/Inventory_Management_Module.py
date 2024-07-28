# inventory_management.py

class InventoryManagement:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, stock):
        """Add a new book to the inventory."""
        if isbn in self.books:
            return "Book already exists."
        self.books[isbn] = {
            'title': title,
            'author': author,
            'stock': stock
        }
        return "Book added successfully."

    def update_stock(self, isbn, stock):
        """Update the stock of a book."""
        if isbn not in self.books:
            return "Book not found."
        self.books[isbn]['stock'] = stock
        return "Stock updated successfully."

    def view_book_details(self, isbn):
        """View details of a book."""
        book = self.books.get(isbn)
        if not book:
            return "Book not found."
        return book

# Example usage
# if __name__ == "__main__":
#     im = InventoryManagement()
#     print(im.add_book('1234567890', 'Book Title', 'Author Name', 5))
#     print(im.update_stock('1234567890', 10))
#     print(im.view_book_details('1234567890'))
