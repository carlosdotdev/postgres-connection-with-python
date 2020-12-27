from decouple import config
import psycopg2

conn = psycopg2.connect(
    host=config('HOST'),
    database=config('DATABASE'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD')
)

cur = conn.cursor()

cur.execute('''CREATE TABLE client (
    username VARCHAR ( 50 ) UNIQUE NOT NULL,
    email VARCHAR ( 50 ) UNIQUE NOT NULL
);''')

conn.commit()

cur.close()
conn.close()
