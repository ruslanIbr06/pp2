import psycopg2 ##pip install psycopg2-binary esli vidaet oshibku
import csv

conn = psycopg2.connect(
    dbname="phonesdb",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            phone VARCHAR(15) NOT NULL
        )
    """)
    conn.commit()


def insert_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            username, phone = row
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()


def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()

    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, phone])


def update_user(identifier, new_username=None, new_phone=None):
    if new_username:
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s OR phone = %s",
                    (new_username, identifier, identifier))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s OR phone = %s",
                    (new_phone, identifier, identifier))
    conn.commit()


def query_data(filter_by=None, value=None):
    if filter_by == "username":
        cur.execute("SELECT * FROM phonebook WHERE username = %s", (value,))
    elif filter_by == "phone":
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (value,))
    else:
        cur.execute("SELECT * FROM phonebook")

    rows = cur.fetchall()
    for row in rows:
        print(row)


def delete_user(identifier):
    cur.execute("DELETE FROM phonebook WHERE username = %s OR phone = %s", (identifier, identifier))
    conn.commit()


def search_by_pattern(pattern):
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insert_or_update_user(username, phone):
    cur.execute("CALL insert_or_update_user(%s, %s)", (username, phone))
    conn.commit()


def insert_many_users(usernames, phones):
    cur.callproc("insert_many_users", (usernames, phones))
    result = cur.fetchone()
    if result and result[0]:
        print("Invalid entries:")
        for entry in result[0]:
            print(entry)
    else:
        print("All entries were valid and inserted successfully.")
    conn.commit()



def get_users_paginated(limit, offset):
    cur.execute("SELECT * FROM get_users(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def delete_user_by_identifier(identifier):
    cur.execute("CALL delete_user_by_identifier(%s)", (identifier,))
    conn.commit()



if __name__ == "__main__":
    create_table()
    # insert_from_csv('contacts.csv')
    # insert_from_console()  # Run this to add new user data
    # update_user("John", new_phone="1234567890")
    # query_data("username", "John")
    # delete_user("1234567890")
    #search_by_pattern("ruslan")
    #insert_or_update_user("ruslan", "987654321")
    '''
    usernames = ['Damir', 'Islam', 'Timur', 'Tamerlan']
    phones = ['1234567', '00993388', '987654321', '12345']
    insert_many_users(usernames, phones)
    '''
    #delete_user_by_identifier("77777777777")



    cur.close()
    conn.close()