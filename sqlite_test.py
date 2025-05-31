import sqlite3
import pandas as pd

connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()

# cursor.execute('''ALTER TABLE fruits ADD COLUMN color VARCHAR(20)''')

fruits = [
    {"name": "apple", "color": "red"},
    {"name": "banana", "color": "yellow"},
    {"name": "grape", "color": "purple"},
    {"name": "orange", "color": "orange"},
    {"name": "kiwi", "color": "green"},
    {"name": "blueberry", "color": "blue"},
    {"name": "watermelon", "color": "green"},
    {"name": "mango", "color": "orange"},
    {"name": "lemon", "color": "yellow"},
    {"name": "cherry", "color": "red"}, 
    {"name": "pineapple", "color": "brown"},
]

# # for fruit in fruits:
#     cursor.execute(f'''INSERT INTO fruits(name, color) VALUES(?, ?)''', (fruit["name"], fruit["color"]))
#     connection.commit()

cursor.execute('''SELECT * FROM fruits;''')
results = cursor.fetchall()

df = pd.read_sql_query("SELECT * FROM fruits", connection)
df.to_csv("fruits.csv", index=False)
connection.close()
# print(results)