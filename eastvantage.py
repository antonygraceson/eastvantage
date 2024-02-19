import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect(r"C:\Users\anton\Pictures\eastvantage\Data_Engineer_ETL_Assignment.db")
    sql_query = """
    SELECT c.customer_id AS Customer,c.age AS Age,i.item_name AS Item,sum(o.quantity) AS Quantity FROM orders as o 
    JOIN customers c on c.customer_id = s.customer_id
    JOIN sales s on s.sales_id = o.sales_id
    JOIN items i on i.item_id = o.item_id
    WHERE o.quantity IS NOT NULL AND c.age BETWEEN 18 AND 35  
    GROUP BY c.customer_id, c.age, i.item_name
    HAVING Quantity > 0
    ORDER BY c.customer_id, i.item_name;
    """
    df = pd.read_sql_query(sql_query, conn)
    df.to_csv('output.csv', index=False)

except Exception as e:
    print("Error:", e)
finally:
    if conn:
        conn.close()
