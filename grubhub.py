import psycopg2
import os

try:
    with psycopg2.connect(f"dbname=grubhub user=codeplaton") as conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE if exists orders CASCADE")
            cur.execute("DROP TABLE if exists restaurants CASCADE")
            cur.execute("DROP TABLE if exists dishes CASCADE")
            cur.execute("DROP TABLE if exists users CASCADE")
            cur.execute("DROP TABLE if exists order_dishes CASCADE")

            cur.execute("CREATE TABLE users (id serial PRIMARY KEY, name varchar(50))")
            cur.execute("CREATE TABLE orders (id serial PRIMARY KEY, total money, user_id INTEGER REFERENCES users(id))")
            cur.execute("CREATE TABLE restaurants (id serial PRIMARY KEY, name varchar(50))")
            cur.execute("CREATE TABLE dishes (id serial PRIMARY KEY, name varchar(50), restaurant_id INTEGER REFERENCES restaurants(id))")
            cur.execute("CREATE TABLE order_dishes (id serial PRIMARY KEY, order_id INTEGER REFERENCES orders(id), dish_id INTEGER REFERENCES dishes(id))")
finally:
    conn.close()




