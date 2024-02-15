import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\anton\Pictures\eastvantage\EastVantage.db")
sql_query = """
SELECT c.customer_id,c.age,item_name,sum(o.quantity) AS sum_of_quantity FROM Orders as o 
JOIN Customer c on c.customer_id = s.customer_id
JOIN Sales s on s.sales_id = o.sales_id
JOIN Items i on i.item_id = o.item_id
WHERE c.age BETWEEN 18 AND 35 
GROUP BY c.customer_id
HAVING sum_of_quantity > 0
"""
df = pd.read_sql_query(sql_query, conn)
df.to_csv('output.csv')
conn.close()
