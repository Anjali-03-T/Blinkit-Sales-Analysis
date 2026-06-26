import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="your pssw",
    database="blinkit_sales_db"
)

cursor = conn.cursor()

cursor.execute("SHOW TABLES")
print("Tables:")
for table in cursor.fetchall():
    print(table)

cursor.execute("SELECT COUNT(*) FROM blinkit_sales")
print("Total Records:", cursor.fetchone()[0])

conn.close()
