import psycopg2

conn= psycopg2.connect(
    host = 'localhost', 
    dbname = 'phonebook', 
    user = 'postgres', 
    password = 'Kz@08122005'
    )

cur = conn.cursor() 

cur.execute('DROP TABLE PhoneBook;')
conn.commit()

cur.execute(""" CREATE TABLE phonebook(
            name VARCHAR(255),
            phone_number VARCHAR(20) PRIMARY KEY
);
""")

conn.commit()
import csv 

filename = "phonebook.csv"

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        #print(row)
        name, phone_number = row
        #print(name, phone_number)
        

        cur.execute(f"""INSERT INTO PhoneBook (name, phone_number) VALUES
                     ('{name}', '{phone_number}');
         """)

        conn.commit()


