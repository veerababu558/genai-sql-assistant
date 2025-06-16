INSERT INTO products (product_id, name, price) VALUES
(1, 'Laptop', 1200.00),
(2, 'Smartphone', 800.00),
(3, 'Headphones', 150.00),
(4, 'Keyboard', 70.00),
(5, 'Monitor', 300.00);


INSERT INTO orders (order_id, customer_id, order_date) VALUES
(101, 1, '2024-06-01'),
(102, 2, '2024-06-02'),
(103, 3, '2024-06-03'),
(104, 1, '2024-06-04'),
(105, 4, '2024-06-05');


INSERT INTO order_items (item_id, order_id, product_id, quantity) VALUES
(1, 101, 1, 1),
(2, 101, 3, 2),
(3, 102, 2, 1),
(4, 103, 3, 1),
(5, 104, 4, 3),
(6, 104, 5, 1),
(7, 105, 1, 1);


INSERT INTO products_data (id, category, brand, stock) VALUES
(1, 'Electronics', 'Dell', 10),
(2, 'Electronics', 'Apple', 20),
(3, 'Accessories', 'Sony', 50),
(4, 'Accessories', 'Logitech', 30),
(5, 'Electronics', 'Samsung', 25);

