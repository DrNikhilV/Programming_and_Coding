CREATE DATABASE inventory_system;

USE inventory_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL
);

CREATE TABLE inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    cost DECIMAL(10, 2),
    quantity INT,
    date_bought DATE
);

CREATE TABLE sales_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    cost DECIMAL(10, 2),
    quantity INT,
    date_sold DATE
);

INSERT INTO inventory (product_name, cost, quantity, date_bought)
VALUES ('biscuit', 20.00, 50, '2024-10-11');

SELECT *
FROM users;





