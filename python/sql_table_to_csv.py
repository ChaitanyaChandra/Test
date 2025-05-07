import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)
df = read_sql("SELECT * FROM test_table")
df.to_csv("output.csv", index=False)
conn.close()
