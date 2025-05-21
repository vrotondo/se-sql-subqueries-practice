import sqlite3
import pandas as pd
conn = sqlite3.Connection('data.sqlite')

# Step 1
q = """
SELECT
    customerNumber,
    contactLastName,
    contactFirstName
FROM customers
JOIN orders 
    USING(customerNumber)
WHERE orderDate = '2003-01-31'
;
"""
df1 = pd.read_sql(q, conn)
# print(df1)

# Step 2
q = """
SELECT
    productName,
    COUNT(orderNumber) AS numberOrders,
    SUM(quantityOrdered) AS totalUnitsSold
FROM products
JOIN orderdetails
    USING (productCode)
GROUP BY productName
ORDER BY totalUnitsSold DESC
;
"""
df2 = pd.read_sql(q, conn)
# print(df2)

# Step 3
q = """
SELECT productName, COUNT(DISTINCT customerNumber) AS numPurchasers
FROM products
JOIN orderdetails
    USING(productCode)
JOIN orders
    USING(orderNumber)
GROUP BY productName
ORDER BY numPurchasers DESC
;
"""
df3 = pd.read_sql(q, conn)
# print(df3)

# Step 4
q = """
SELECT
    DISTINCT employeeNumber,
    officeCode,
    o.city,
    firstName,
    lastName
FROM employees AS e
JOIN offices AS o
    USING(officeCode)
JOIN customers AS c
    ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders
    USING(customerNumber)
JOIN orderdetails
    USING(orderNumber)
WHERE productCode IN (
    SELECT productCode
    FROM products
    JOIN orderdetails
        USING(productCode)
    JOIN orders
        USING(orderNumber)
    GROUP BY productCode
    HAVING COUNT(DISTINCT customerNumber) < 20
)
;
"""
df4 = pd.read_sql(q, conn)
# print(df4)

# Step 5
q = """
SELECT
    employeeNumber,
    firstName,
    lastName,
    COUNT(customerNumber) AS numCustomers
FROM employees AS e
JOIN customers As c
    ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY employeeNumber
HAVING AVG(creditLimit) > 15000
;
"""
df5 = pd.read_sql(q, conn)
print(df5)

conn.close()