import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_pass",
    database="your_db"
)
df = pd.read_sql("SELECT * FROM test_table", conn)
df.to_csv("output.csv", index=False)
conn.close()
