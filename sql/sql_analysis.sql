-- Total Revenue
SELECT SUM(Total_Sales) AS Total_Revenue
FROM blinkit_sales;

SELECT COUNT(Order_ID) AS Total_Orders
FROM blinkit_sales;

SELECT ROUND(AVG(Total_Sales), 2) AS Average_Order_Value
FROM blinkit_sales;

SELECT
    Category,
    ROUND(SUM(Total_Sales), 2) AS Revenue
FROM blinkit_sales
GROUP BY Category
ORDER BY Revenue DESC;

SELECT
    Product_Name,
    SUM(Quantity) AS Quantity_Sold
FROM blinkit_sales
GROUP BY Product_Name
ORDER BY Quantity_Sold DESC
LIMIT 10;

SELECT
    Delivery_Type,
    COUNT(*) AS Orders
FROM blinkit_sales
GROUP BY Delivery_Type;