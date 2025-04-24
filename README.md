# Practice for SQL Subqueries

## Set Up

* Fork and Clone the GitHub Repo
* Install dependencies and enter the virtual environment:
    * `pipenv install`
    * `pipenv shell`

Next, let's set up our code in `main.py`. Import libraries and connect to the database.

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')
```

## Practice Queries

1. Write an Equivalent Query using a Subquery

The following query works using a JOIN. Rewrite it so that it uses a subquery instead.

```sql
SELECT
    customerNumber,
    contactLastName,
    contactFirstName
FROM customers
JOIN orders
    USING(customerNumber)
WHERE orderDate = '2003-01-31'
;
```

2. Select the Total Number of Orders for Each Product Name
- Sort the results by the total number of items sold for that product.

3. Select the Product Name and the Total Number of People Who Have Ordered Each Product
- Sort the results in descending order.

4. Select the Employee Number, First Name, Last Name, City (of the office), and Office Code of the Employees who sold products that have been ordered by fewer than 20 people.
- Hint:  To start, think about how you might break the problem up. Be sure that your results only list each employee once.

5. Select the Employee Number, First Name, Last Name, and Number of Customers for Employees whose customers have an average credit limit over 15K.