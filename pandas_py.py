import sqlite3
import pandas as pd

try:
    connection = sqlite3.connect('Data Engineer_ETL Assignment.db')

    sales_df = pd.read_sql_query("select * from Sales", connection)
    customer_df = pd.read_sql_query("select * from Customers", connection)
    orders_df = pd.read_sql_query("select * from Orders", connection)
    items_df = pd.read_sql_query("select * from Items", connection)

    join_df = pd.merge(sales_df, customer_df, on='customer_id')
    join_df = pd.merge(join_df, orders_df, on='sales_id')
    join_df = pd.merge(join_df, items_df, on='item_id')

    final_df = join_df[(join_df['age'] >= 18) & (join_df['age'] <= 35)]

    final_df = final_df.groupby(['customer_id', 'age', 'item_name']).agg({'quantity': 'sum'}).reset_index()
    final_df = final_df[final_df['quantity'] > 0]
    final_df.quantity = final_df.quantity.astype('int64')

    final_df.rename(columns={'customer_id': 'Customer',
                             'item_name': 'Item',
                             'age': 'Age',
                             'quantity': 'Quantity'
                             }, inplace=True)

    final_df.to_csv('output_pandas.csv', index=False)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    connection.close()
