
from User_Management_Module import UserManagement
if __name__ == "__main__":
    um = UserManagement()
    print(um.register_user('john_doe', 'password123', 'john@example.com'))
    print(um.login_user('john_doe', 'password123'))
    print(um.view_profile('john_doe'))
    print(end='\n')



from Inventory_Management_Module import InventoryManagement

if __name__ == "__main__":
    im = InventoryManagement()
    print(im.add_book('1234567890', 'Book Title', 'Author Name', 5))
    print(im.update_stock('1234567890', 10))
    print(im.view_book_details('1234567890'))
    print(end='\n')

from Order_and_Rental_Management import OrderRentalManagement

if __name__ == "__main__":
    # from Inventory_Management_Module import InventoryManagement

    im = InventoryManagement()
    orm = OrderRentalManagement(im)

    im.add_book('1234567890', 'Book Title', 'Author Name', 5)
    print(orm.place_order('john_doe', '1234567890'))
    print(orm.rent_book('john_doe', '1234567890'))
    print(orm.return_book('john_doe', '1234567890'))
    print(end='\n')
    print(end='\n')


import calculator

print(calculator.add_two(4,5))
print(calculator.multiply_two(10,2))
