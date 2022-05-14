

intro = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
'''

all_items = {
    'Appetizers':['Wings', 'Cookies', 'Spring Rolls'],
    'Entrees':['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
    'Desserts':['Ice Cream', 'Cake', 'Pie'],
    'Drinks':['Coffee', 'Tea', 'Unicorn Tears'],
}

all_items_arr = ['Wings', 'Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears']

receive = '''
***********************************
** What would you like to order? **
***********************************
'''

print(intro)

for meal in all_items:
    print(meal)
    print('--------')
    for food in all_items[meal]:
        print(food)
    print(' ')

print(receive)

order = []

loop = True
while loop:
    item = input('> ')
    if item == 'quit':
        print('Thank you for visiting the Snakes Cafe!')
        break
    if item in all_items_arr:
        order.append(item)
        item_count = order.count(item)
        if item_count <= 1:
            orders = 'order'
        else:
            orders = 'orders'
        print(f'** {item_count} {orders} of {item} have been added to your meal **')
    else:
        print('Sorry, we don\'t carry that, please order something on the menu.')
