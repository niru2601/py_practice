import psycopg2
import pandas as pd

conn = None
curr = None

try : 
    conn = psycopg2.connect(database="Bank",
                        host="localhost",
                        user="postgres",
                        password="Admin@1299",
                        port=5432)
    

    curr = conn.cursor()

    curr.execute('select * from "Bank_Loan" limit 5')
    for record in curr.fetchall():
        print(record[1],record[2])

except Exception as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
    if curr is not None:
        curr.close()