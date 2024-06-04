import psycopg2
#1-masala
#2-masala
db_name = 'n47'
password = 'jasur'
host = 'localhost'
port = 5432
user = 'postgres'

with psycopg2.connect(dbname=db_name,
                      user=user,
                      password=password,
                      host=host,
                      port=port) as conn:
    with conn.cursor() as cur:

        #create qismi
        create_table_query="""create table if not exists product(
         id serial PRIMARY KEY,
         name varchar(70) not null unique,
         price float,
         color varchar(25),
         image varchar(255)
         );
         """

        cur.execute(create_table_query)
        conn.commit()
        print('Table Successfully Created')
        #2-masala

        #select qismi
        select_data_query = "select * from product;"
        cur.execute(select_data_query)
        for row in cur.fetchall():
            print(row)



        #insert qismi
        name=input('name:')
        price = float(input('Title : '))
        color=input('color:')
        image = input('Image : ')


        insert_data_query = "insert into product(name,price,color,image) values(%s,%s,%s,%s);"
        insert_data_params = (name,price,color, image)
        cur.execute(insert_data_query, insert_data_params)
        conn.commit()


       #delete qismi
        _id = int(input('ID : '))
        delete_data_query = 'delete from product where id = %s;'
        data = (_id,)
        cur.execute(delete_data_query, data)
        conn.commit()


        #update qismi
        update_data_query = """update product set title = %s,image = %s where id = %s"""
        name = input('Enter name: ')
        price=float(input('price:'))
        color=input('color:')
        image = input('Enter Image : ')
        _id = int(input('ID : '))
        cur.execute(update_data_query, (name,price,color, image, _id))
        conn.commit()
#3-masala
class Alifbo:
   def __iter__(self):
       return self
   def __next__(self):
     my_list = [chr(i) for i in range(97, 123)]

     iterator = iter(my_list)
     try:
       while True:
           print(next(iterator))

     except StopIteration:
        pass
alifbo=Alifbo()
for i in alifbo:
    print(i)



#4-masala
import threading
import time
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_leters():
    for i in 'ABCDE':
        print(i)
        time.sleep(1)

print_numbers()
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_leters)
thread1.start()
thread2.start()
#agar join() ishlatsak bittasi bajarilib turib keyin keyingisiga utadi
#thread1.join()
#5-masala
from  typing import Optional
class Product:

    def __init__(self, name:Optional[str]=None,price:Optional[float]=None,color:Optional[str]=None,image:Optional[str]=None):
        self.name = name
        self.price=price
        self.color=color
        self.image=image

    def save(self):
            insert_into_car = """INSERT INTO product(name,price,color,image)
            values (%s,%s,%s,%s);
            """
            cur.execute(insert_into_car, (self.name,self.price,self.color,self.image))
            cur.commit()
            print('Successfully saved >malumot qushildi')
product1=Product('muzlatkich',12333,'oq','image1')
product1.save()
product2=Product('a32',345,'qora','image2')
product2.save()
#save metodi orqali malumot qushsak bulaveradi



#6-masala
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()
db_params = {
    'database': os.getenv('database'),
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'host': os.getenv('host'),
    'port': os.getenv('port'),
}
class ConnectDB:
    def __init__(self, db_params: dict):
        self.db_params = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_params)
        self.cur = self.conn.cursor()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        if self.conn:
            self.cur.close()
            self.conn.close()

    def commit(self):
        self.conn.commit()


class Product1:
    def __init__(self, name,price,color,image):
        self.name = name
        self.price=price
        self.color=color
        self.image=image

    def save(self):
        with ConnectDB(db_params) as db:
            insert_into_car = """INSERT INTO product(name,price,color,image)
            values (%s,%s,%s,%s);
            """
            db.cur.execute(insert_into_car, (self.name,self.price,self.color,self.image))
            db.commit()
            print('Successfully saved')


obj1 = Product1('a54','123','oq','image')
obj1.save()
#malumot ham qushib quydm
#7-masala



import requests
import psycopg2
url = f'https://dummyjson.com/products/'

r = requests.get(url)
# print(r.status_code, r.text)

conn=psycopg2.connect(**db_params)
cur=conn.cursor()
create_table_products_query = """create table products3(
        id serial primary key ,
        title varchar(255) ,
        description text ,
        price int,
        discountPercentage float,
        rating float ,
        stock int,
        brand varchar(255),
        category varchar(200),
        thumbnail varchar(255),
        images jsonb
);"""


cur.execute(create_table_products_query)
conn.commit()

insert_into_query = """insert into products (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail,images)

    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);

"""

for product in r.json()['products3']:
    cur.execute(insert_into_query, (
        product3['title'], product3['description'], product3['price'], product3['discountPercentage'], product3['rating'],
        product3['stock'], product3['brand'], product3['category'], product3['thumbnail'], str(product3['images'])))
    conn.commit()


#Axmatullayev Jasur



