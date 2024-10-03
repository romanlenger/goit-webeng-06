import psycopg2

from pathlib import Path


conn = psycopg2.connect(host="localhost", database="hw-06", user="postgres", password="mort")
cursor = conn.cursor()

def execute_sql_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql = file.read()
        cursor.execute(sql)

    return cursor.fetchall()

query = 'query_4.sql'
print(execute_sql_file(cursor, Path(__file__).resolve().parent / 'queries' / query))

cursor.close()
conn.close()
