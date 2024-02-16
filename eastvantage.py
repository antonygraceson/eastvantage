import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect(r"C:\Users\anton\Pictures\eastvantage\EastVantage.db")
    sql_query = """
    SELECT c.customer_id AS Customer,c.age AS Age,item_name AS Item,sum(o.quantity) AS Quantity FROM Orders as o 
    JOIN Customer c on c.customer_id = s.customer_id
    JOIN Sales s on s.sales_id = o.sales_id
    JOIN Items i on i.item_id = o.item_id
    WHERE o.quantity IS NOT NULL AND c.age BETWEEN 18 AND 35  
    GROUP BY c.customer_id
    HAVING Quantity > 0
    """
    df = pd.read_sql_query(sql_query, conn)
    df.to_csv('output.csv', index=False)

except Exception as e:
    print("Error:", e)
finally:
    if conn:
        conn.close()
