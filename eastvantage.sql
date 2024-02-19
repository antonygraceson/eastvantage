SELECT c.customer_id AS Customer,c.age AS Age,i.item_name AS Item,sum(o.quantity) AS Quantity FROM orders as o
JOIN customers c on c.customer_id = s.customer_id
JOIN sales s on s.sales_id = o.sales_id
JOIN items i on i.item_id = o.item_id
WHERE o.quantity IS NOT NULL AND c.age BETWEEN 18 AND 35
GROUP BY c.customer_id, c.age, i.item_name
HAVING Quantity > 0
ORDER BY c.customer_id, i.item_name;
