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

cur.execute("""INSERT INTO PhoneBook (name, phone_number) VALUES
            ('aida', '87768082005'),
            ('ayim', '87761231233'),
            ('azamat', '87012847143'),
            ('anuar', '87053489922');
""")

conn.commit()

cur.execute('SELECT name, phone_number FROM PhoneBook')
print (cur.fetchall())

cur.execute("""UPDATE PhoneBook
            SET phone_number = '87777777777'
            WHERE name = 'aiym';
""")

conn.commit()

#deleting names 
cur.execute("""DELETE FROM PhoneBook
            WHERE name = 'aiym';
""")

conn.commit()



