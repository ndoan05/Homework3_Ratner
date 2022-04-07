# Nam Doan
# 1847037

class ItemToPurchase:

    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name

        self.item_description = description

        self.item_price = price

        self.item_quantity = quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity

        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, total))

    def print_item_description(self):
        print('%s: %s' % (self.item_name, self.item_description))


class ShoppingCart:

    def __init__(self, customer_name='none', current_date='none', cart_items=[]):

        self.customer_name = customer_name

        self.current_date = current_date

        self.cart_items = cart_items

    def add_item(self, string):
        print('ADD ITEM TO CART', end='\n')
        item_name = str(input('Enter the item name:'))
        item_description = str(input('\nEnter the item description:'))
        item_price = int(input('\nEnter the item price:'))
        item_quantity = int(input('\nEnter the item quantity:\n'))


        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))


    def get_cost_of_cart(self):

        total_cost = 0

        cost = 0

        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)

            total_cost += cost

        return total_cost

    def print_total():

        total_cost = self.get_cost_of_cart()

        if (total_cost == 0):

            print('SHOPPING CART IS EMPTY')

        else:

            self.output_cart()


    def print_descriptions(self):

        if len(self.cart_items) == 0:

            print('SHOPPING CART IS EMPTY')

        else:

            print('\nOUTPUT ITEMS\' DESCRIPTIONS')

            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')

            print('\nItem Descriptions', end='\n')

            for item in self.cart_items:
                item.print_item_description()

    def output_cart(self):
        new = ShoppingCart()
        print('OUTPUT SHOPPING CART', end='\n')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('Number of Items:', new.get_num_items_in_cart(), end='\n\n')
        tc = 0
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        for item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity,
                                             item.item_price, (item.item_quantity * item.item_price)), end='\n')
            tc += (item.item_quantity * item.item_price)
        print('\nTotal: ${}'.format(tc), end='\n')

    def remove_item(self):

        print('REMOVE ITEM FROM CART', end='\n')

        string = input('Enter name of item to remove:\n')

        tremove_item = False

        for item in self.cart_items:

            if item.item_name == string:
                self.cart_items.remove(item)

                tremove_item = True

                break

        if not tremove_item:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self):

        print('\nCHANGE ITEM QUANTITY', end='\n')

        name = input('Enter the item name:\n')

        quantity = int(input('Enter the new quantity:\n'))

        tmodify_item = False

        for item in self.cart_items:

            if name == item.item_name:
                item.item_quantity = quantity

                tmodify_item = True

                break

        if not tmodify_item:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):

        num_items = 0

        for item in self.cart_items:
            num_items = num_items + item.item_quantity

        return num_items


def print_menu(newCart):
    customer_Cart = newCart

    menu = ('\nMENU\n'

            'a - Add item to cart\n'

            'r - Remove item from cart\n'

            'c - Change item quantity\n'

            'i - Output items\' descriptions\n'

            'o - Output shopping cart\n'

            'q - Quit\n')

    command = ''

    while (command != 'q'):

        string = ''

        print(menu, end='\n')

        command = input('Choose an option:\n')

        while (
                command != 'a' and command != 'o' and command != 'i' and command != 'q' and command != 'r' and command != 'c'):
            command = input('Choose an option:\n')

        if (command == 'a'):
            customer_Cart.add_item(string)

        if (command == 'o'):
            customer_Cart.output_cart()

        if (command == 'i'):
            customer_Cart.print_descriptions()

        if (command == 'r'):
            customer_Cart.remove_item()

        if (command == 'c'):
            customer_Cart.modify_item()


if __name__ == "__main__":
    customer_name = input('Enter customer\'s name:\n')

    current_date = input('Enter today\'s date:\n')

    print("\nCustomer name:", customer_name, end='\n')

    print('Today\'s date:', current_date, end='\n')

    newCart = ShoppingCart(customer_name, current_date)

    print_menu(newCart)
