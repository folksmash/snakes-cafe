

#items to be ordered
menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **

**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears"""
#variable of what is ordered 
order_prompt = """***********************************
** What would you like to order? **
***********************************
"""

#need to take in order info
#need to display order info 
##separating items
##each item and how many ordered
#need to
print(menu)
print(order_prompt)


#function used to take in order info and place the > back on screen to order more items


def take_order():
    order_response = input(">")
    if order_response == "quit":
        print('goodbye')
        quit()
    else:
        print(f"1 order of {order_response} have been added to your meal") 
    take_order()





take_order()