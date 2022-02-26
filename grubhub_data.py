import psycopg2
import os

try:
    with psycopg2.connect(f"dbname=grubhub user=codeplaton") as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users(name) VALUES('Bob')")
            cur.execute("INSERT INTO users(name) VALUES('Sally')")

            cur.execute("INSERT INTO orders(total, user_id) VALUES(12.98, 1)")
            cur.execute("INSERT INTO orders(total, user_id) VALUES(21.98, 2)")
            cur.execute("INSERT INTO orders(total, user_id) VALUES(120.976, 1)")

            cur.execute("INSERT INTO restaurants(name) VALUES('Slopshop')")
            cur.execute("INSERT INTO restaurants(name) VALUES('7-11 Premium')")

            cur.execute("INSERT INTO dishes(name, restaurant_id) VALUES('burger',1)")
            cur.execute("INSERT INTO dishes(name, restaurant_id) VALUES('nuggets',1)")
            cur.execute("INSERT INTO dishes(name, restaurant_id) VALUES('hot dog',2)")
            cur.execute("INSERT INTO dishes(name, restaurant_id) VALUES('old hot dog',2)")
            cur.execute("INSERT INTO dishes(name, restaurant_id) VALUES('slurpee',2)")


            cur.execute("INSERT INTO order_dishes(order_id, dish_id) VALUES(1,1)")
            cur.execute("INSERT INTO order_dishes(order_id, dish_id) VALUES(1,2)")
            cur.execute("INSERT INTO order_dishes(order_id, dish_id) VALUES(2,4)")
            cur.execute("INSERT INTO order_dishes(order_id, dish_id) VALUES(3,2)")
            cur.execute("INSERT INTO order_dishes(order_id, dish_id) VALUES(3,2)")
            cur.execute("INSERT INTO order_dishes(order_id, dish_id) VALUES(3,2)")



finally:
    conn.close()