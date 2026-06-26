import pandas as pd
import mysql.connector
import numpy as np

# Read CSV
df = pd.read_csv("dataset/Blinkit_Sales_Cleaned.csv")

# Replace NaN with None for MySQL
df = df.replace({np.nan: None})

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your pssw",
    database="blinkit_sales_db"
)

cursor = connection.cursor()

query = """
INSERT INTO blinkit_sales (
    Order_ID,
    Date,
    City,
    Product_Name,
    Category,
    Quantity,
    Unit_Price,
    Total_Sales,
    Delivery_Time,
    Customer_Rating,
    Payment_Mode,
    Delivery_Type,
    Seller_Name
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for row in df.itertuples(index=False):
    cursor.execute(query, tuple(row))

connection.commit()

print(f"✅ {len(df)} records imported successfully!")

cursor.close()
connection.close()
