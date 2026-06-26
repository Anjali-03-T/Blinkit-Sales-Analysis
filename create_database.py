import mysql.connector

# Connect to MySQL Server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your pssw"
)

cursor = connection.cursor()

# Create Database
query = """
CREATE DATABASE IF NOT EXISTS blinkit_sales_db;
"""

cursor.execute(query)

print("✅ Database 'blinkit_sales_db' created successfully!")

cursor.close()
connection.close()
