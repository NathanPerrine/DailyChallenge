# Kitchen View

# A restaurant ordering system accepts food orders one item at a time. Each item entered is for a specific person sitting at a particular table.
# The kitchen is not concerned with which person ordered which item. They just need to know what menu items have been ordered for each table.
# Write a program that will read a list of individual orders and "pivot" that set into a display of food items for each table in the diner. The total number of each item per table will be displayed on a column for that food item.
# For example, the orders:
# Sarah,7,Green Salad
# Sarah,7,Cappuccino
# Michael,2,Club Sandwich
# Marcus,5,Sparkling Water

# Would be displayed for the kitchen as:
# Table,Cappuccino,Club Sandwich,Green Salad,Sparkling Water
# 2,0,1,0,0
# 5,0,0,0,1
# 7,1,0,1,0

# Note that the menu items are listed in alphabetical order across the overall list.
# Input:
# A comma-delimited list of names, table numbers, and menu items.
# Output:
# A comma-delimited list of table numbers and item counts with a header row as the first line. The first column name is "Table".

orders = [
    "Sarah,7,Green Salad",
    "Sarah,7,Cappuccino",
    "Michael,2,Club Sandwich",
    "Marcus,5,Sparkling Water"
]

tables = {}

menu = []


for order in orders: 
    new_order = order.split(",")
    table_number = new_order[1]
    item = new_order[-1]

    if table_number not in tables:
        tables[table_number] = []
        tables[table_number].append(item)
    else: 
        tables[table_number].append(item)
    
    if item not in menu:
        menu.append(item)


for table in tables:
    # print(table)

    # print(tables[table])
    table_order = tables[table]
    order_list = [0] * len(menu)
    
    for item in table_order:
        i = menu.index(item)
        # print(i)
        order_list[i] += 1
    tables[table] = order_list

    print(table, tables[table])