import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your pssw",
    database="blinkit_sales_db"
)

cursor = connection.cursor()

# Create Table
query = """
CREATE TABLE IF NOT EXISTS blinkit_sales (
    Order_ID INT PRIMARY KEY,
    Date DATE,
    City VARCHAR(50),
    Product_Name VARCHAR(100),
    Category VARCHAR(50),
    Quantity INT,
    Unit_Price DECIMAL(10,2),
    Total_Sales DECIMAL(10,2),
    Delivery_Time INT,
    Customer_Rating DECIMAL(2,1),
    Payment_Mode VARCHAR(20),
    Delivery_Type VARCHAR(20),
    Seller_Name VARCHAR(100)
);
"""

cursor.execute(query)

print("✅ Table 'blinkit_sales' created successfully!")

connection.commit()

cursor.close()
connection.close()
