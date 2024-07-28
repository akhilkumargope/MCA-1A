# order_rental_management.py

class OrderRentalManagement:
    def __init__(self, inventory):
        self.orders = []
        self.rentals = []
        self.inventory = inventory

    def place_order(self, username, isbn):
        """Place an order for a book."""
        book = self.inventory.books.get(isbn)
        if not book:
            return "Book not found."
        if book['stock'] <= 0:
            return "Book out of stock."
        self.orders.append({
            'username': username,
            'isbn': isbn
        })
        book['stock'] -= 1
        return "Order placed successfully."

    def rent_book(self, username, isbn):
        """Rent a book."""
        book = self.inventory.books.get(isbn)
        if not book:
            return "Book not found."
        if book['stock'] <= 0:
            return "Book out of stock."
        self.rentals.append({
            'username': username,
            'isbn': isbn
        })
        book['stock'] -= 1
        return "Book rented successfully."

    def return_book(self, username, isbn):
        """Return a rented book."""
        rental = next((r for r in self.rentals if r['username'] == username and r['isbn'] == isbn), None)
        if not rental:
            return "Rental not found."
        self.rentals.remove(rental)
        self.inventory.books[isbn]['stock'] += 1
        return "Book returned successfully."

# Example usage
# if __name__ == "__main__":
#     from Inventory_Management_Module import InventoryManagement

#     im = InventoryManagement()
#     orm = OrderRentalManagement(im)

#     im.add_book('1234567890', 'Book Title', 'Author Name', 5)
#     print(orm.place_order('john_doe', '1234567890'))
#     print(orm.rent_book('john_doe', '1234567890'))
#     print(orm.return_book('john_doe', '1234567890'))
