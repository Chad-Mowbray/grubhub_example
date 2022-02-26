# Grubhub using psycopg2

This is just a preview of what we will be doing later (using Python as a wrapper around SQL).  When we get to Django, it will look even less like SQL.

## To Run It
1. Create and activate a virtual environment
2. pip install psycopg2
3. Change your `user` (in line 5 of both files)
4. Create a database called `grubhub`
4. Run `grubhub.py` first, then `grubhub_data.py`

You can then enter the grubhub database and poke around.  Notice that an order can have many dishes and a dish can belong to many orders because of the order_dishes table.

Q: How would you get the total and dish names for the first order?
A: select total, name from orders join order_dishes on orders.id = order_dishes.order_id join dishes on order_dishes.dish_id = dishes.id where orders.id = 1;

Feel free to play around with different queries.