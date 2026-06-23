#==========================================
#SUPERMARKET SALES SQL ANALYSIS
#==========================================
#
#✓ Connect to database
#✓ Execute 20 SQL queries
#✓ Display results as DataFrames
#✓ Save outputs if needed
#✓ Close connection
#-- Show all records
SELECT * FROM sales;

-- Show first 10 records
SELECT * FROM sales
LIMIT 10;

-- Sales in Yangon
SELECT *
FROM sales
WHERE city = 'Yangon';

-- Revenue by City
SELECT city,
SUM(total) AS revenue
FROM sales
GROUP BY city;

-- Revenue by Branch
SELECT branch,
SUM(total) AS revenue
FROM sales
GROUP BY branch;

-- Average Rating
SELECT product_line,
AVG(rating) AS average_rating
FROM sales
GROUP BY product_line;

-- Highest Revenue Transactions
SELECT invoice_id,
city,
product_line,
total
FROM sales
ORDER BY total DESC
LIMIT 10;

-- Most Used Payment Method
SELECT payment,
COUNT(*) AS total_transactions
FROM sales
GROUP BY payment
ORDER BY total_transactions DESC;

-- Customer Type Analysis
SELECT customer_type,
SUM(total) AS revenue
FROM sales
GROUP BY customer_type;

-- Gender Revenue
SELECT gender,
SUM(total) AS revenue
FROM sales
GROUP BY gender;

-- Product Line Performance
SELECT product_line,
SUM(total) AS revenue
FROM sales
GROUP BY product_line
ORDER BY revenue DESC;

-- Daily Sales
SELECT date,
SUM(total) AS revenue
FROM sales
GROUP BY date;

-- Peak Hours
SELECT hour,
SUM(total) AS revenue
FROM sales
GROUP BY hour
ORDER BY revenue DESC;

-- Window Function
SELECT
invoice_id,
city,
total,
ROW_NUMBER() OVER(ORDER BY total DESC) AS ranking
FROM sales;

-- Running Revenue
SELECT
date,
total,
SUM(total) OVER(
ORDER BY date
) AS cumulative_revenue
FROM sales;

-- Top Revenue City
SELECT *
FROM sales
WHERE total >
(
SELECT AVG(total)
FROM sales
);

-- CTE Example
WITH city_sales AS
(
SELECT city,
SUM(total) revenue
FROM sales
GROUP BY city
)

SELECT *
FROM city_sales
ORDER BY revenue DESC;