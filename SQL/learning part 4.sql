USE prime;

SELECT * FROM orders
WHERE amount > (
SELECT AVG(amount) FROM orders
);

SELECT name, 
    (
        SELECT COUNT(*)
		FROM orders o
		WHERE o.customer_id = c.customer_id
	) AS order_count
FROM customers c;


-- Views in SQL
CREATE VIEW v1 AS
SELECT order_id, amount FROM orders;

SELECT * FROM v1;

CREATE VIEW v2 AS
SELECT c.customer_id, c.name, o.order_id
FROM customers c
INNER JOIN orders o
WHERE c.customer_id = o.customer_id;

SELECT * FROM v2;

DROP VIEW v1;


-- Index
CREATE INDEX idx_name ON customers(name);
SHOW INDEX FROM customers;

DROP INDEX idx_name ON customers;


DELIMITER $$
CREATE PROCEDURE check_amount(IN od_id INT, OUT amt DECIMAL(10, 2))
BEGIN
SELECT amount INTO amt
FROM orders 
WHERE order_id = od_id;
END $$

DELIMITER ;

CALL check_amount(101, @amount);
SELECT @amount;

DROP PROCEDURE check_amount;