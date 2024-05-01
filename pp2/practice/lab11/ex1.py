import psycopg2

# Function to connect to the database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="phonebook",
            user="postgres",
            password="Kz@08122005"
        )
        print("Connected to the database")
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

# Procedure to insert or update user
def insert_or_update_user(conn, full_name, phone_number, operator):
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO phonebook (full_name, phone_number, operator) 
            VALUES (%s, %s, %s)
            ON CONFLICT (full_name) 
            DO UPDATE SET phone_number = EXCLUDED.phone_number;
        """, (full_name, phone_number, operator))
        conn.commit()
        print("User inserted or updated successfully")
    except psycopg2.Error as e:
        print("Error inserting or updating user:", e)

# Procedure to delete data from tables by username or phone
def delete_data(conn, pattern):
    try:
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM phonebook 
            WHERE full_name LIKE %s 
            OR phone_numbeк LIKE %s
            OR operator LIKE %s;
        """, (f'%{pattern}%', f'%{pattern}%',f'%{pattern}%'))
        conn.commit()
        print("Data deleted successfully")
    except psycopg2.Error as e:
        print("Error deleting data:", e)

# Function to search for records based on a pattern
def search_records(conn, pattern):
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM phonebook 
            WHERE full_name LIKE %s 
            OR phone_number LIKE %s
            OR operator LIKE %s;
        """, (f'%{pattern}%', f'%{pattern}%',  f'%{pattern}%'))


        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("Search completed successfully")
    except psycopg2.Error as e:
        print("Error searching records:", e)

# Main function
def main():
    # Connect to the database
    conn = connect_to_database()
    if conn is None:
        return

    # Insert or update user
    insert_or_update_user(conn, "Kair Aiym", "1234567890", "Tele2")

    # Search for records
    search_records(conn, "Aiym")

    # Delete data by username or phone
    delete_data(conn, "Aiym")

    # Close the database connection
    conn.close()
    print("Connection to the database closed")

# Execute the main function
if __name__ == "__main__":
    main()