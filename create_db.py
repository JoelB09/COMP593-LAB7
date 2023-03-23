import os
import inspect
from datetime import datetime
from faker import Faker
import sqlite3

fake = Faker()

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    conn = sqlite3.connect(db_path)
    create_people_table(conn)
    populate_people_table(conn)
    conn.close()

def create_people_table(conn):
    #Creates the people table in the database
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE people
                (id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                email TEXT,
                created_at TEXT,
                updated_at TEXT)''')
    conn.commit()

def populate_people_table(conn):
    #Populates the people table with 200 fake people
    cursor = conn.cursor()
    for i in range(200):
        name = fake.name()
        age = fake.random_int(min=1, max=100)
        email = fake.email()
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO people (name, age, email, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                       (name, age, email, created_at, updated_at))
    conn.commit()

def get_script_dir():
    #Determines the path of the directory in which this script resides
    # Returns:str: Full path of the directory in which this script resides
    
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()
