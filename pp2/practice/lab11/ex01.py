import psycopg2

conn = psycopg2.connect(database="phonebook",
                        host="localhost",
                        user="postgres",
                        password="Kz@08122005",)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE phonebook (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        phone TEXT UNIQUE NOT NULL
    )
""")

conn.commit()
conn.close()


#Function that returns all records based on a pattern
def search_pattern(pattern):
    conn = psycopg2.connect(database="phonebook",
                            host="localhost",
                            user="postgres",
                            password="Kz@08122005")

    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM phonebook
        WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s
    """, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))

    results = cur.fetchall()

    conn.close()

    return results

#Create procedure to insert new user by name and phone, update phone if user already exists
def insert_user(name, surname, phone):
    conn = psycopg2.connect(database="phonebook",
                            host="localhost",
                            user="postgres",
                            password="Kz@08122005")

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO phonebook (name, surname, phone)
        VALUES (%s, %s, %s)
        ON CONFLICT (phone) DO UPDATE SET name=%s, surname=%s
    """, (name, surname, phone, name, surname))

    conn.commit()
    conn.close()

    # Procedure to delete data from tables by username or phone
def delete_data(conn, pattern):
    try:
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM phonebook 
            WHERE name LIKE %s 
            OR surname LIKE %s
            OR phone LIKE %s;
        """, (f'%{pattern}%', f'%{pattern}%',f'%{pattern}%'))
        conn.commit()
        print("Data deleted successfully")
    except psycopg2.Error as e:
        print("Error deleting data:", e)
