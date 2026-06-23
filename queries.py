import pandas as pd
from database_utils import connect_db

# Connect to the database
conn = connect_db()

print("=" * 60)
print("SUPERMARKET SALES SQL ANALYSIS")
print("=" * 60)


def run_query(title, query):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    df = pd.read_sql(query, conn)

    print(df)
    return df


# ----------------------------------------------------
# 1. Show first 10 records
# ----------------------------------------------------
run_query(
    "FIRST 10 RECORDS",
    """
    SELECT *
    FROM sales
    LIMIT 10;
    """
)

# ----------------------------------------------------
# 2. Sales in Yangon
# ----------------------------------------------------
run_query(
    "SALES IN YANGON",
    """
    SELECT *
    FROM sales
    WHERE city='Yangon';
    """
)

# ----------------------------------------------------
# 3. Revenue by City
# ----------------------------------------------------
run_query(
    "REVENUE BY CITY",
    """
    SELECT
        city,
        ROUND(SUM(total),2) AS revenue
    FROM sales
    GROUP BY city
    ORDER BY revenue DESC;
    """
)

# ----------------------------------------------------
# 4. Revenue by Branch
# ----------------------------------------------------
run_query(
    "REVENUE BY BRANCH",
    """
    SELECT
        branch,
        ROUND(SUM(total),2) AS revenue
    FROM sales
    GROUP BY branch
    ORDER BY revenue DESC;
    """
)

# ----------------------------------------------------
# 5. Average Rating
# ----------------------------------------------------
run_query(
    "AVERAGE RATING BY PRODUCT LINE",
    """
    SELECT
        product_line,
        ROUND(AVG(rating),2) AS average_rating
    FROM sales
    GROUP BY product_line
    ORDER BY average_rating DESC;
    """
)

# ----------------------------------------------------
# 6. Top 10 Highest Revenue Transactions
# ----------------------------------------------------
run_query(
    "TOP 10 TRANSACTIONS",
    """
    SELECT
        invoice_id,
        city,
        product_line,
        total
    FROM sales
    ORDER BY total DESC
    LIMIT 10;
    """
)

# ----------------------------------------------------
# 7. Payment Methods
# ----------------------------------------------------
run_query(
    "PAYMENT METHODS",
    """
    SELECT
        payment,
        COUNT(*) AS transactions
    FROM sales
    GROUP BY payment
    ORDER BY transactions DESC;
    """
)

# ----------------------------------------------------
# 8. Customer Type Revenue
# ----------------------------------------------------
run_query(
    "CUSTOMER TYPE REVENUE",
    """
    SELECT
        customer_type,
        ROUND(SUM(total),2) AS revenue
    FROM sales
    GROUP BY customer_type;
    """
)

# ----------------------------------------------------
# 9. Gender Revenue
# ----------------------------------------------------
run_query(
    "GENDER REVENUE",
    """
    SELECT
        gender,
        ROUND(SUM(total),2) AS revenue
    FROM sales
    GROUP BY gender;
    """
)

# ----------------------------------------------------
# 10. Product Line Performance
# ----------------------------------------------------
run_query(
    "PRODUCT LINE PERFORMANCE",
    """
    SELECT
        product_line,
        ROUND(SUM(total),2) AS revenue
    FROM sales
    GROUP BY product_line
    ORDER BY revenue DESC;
    """
)

# Close connection
conn.close()

print("\n" + "=" * 60)
print("ALL QUERIES EXECUTED SUCCESSFULLY")
print("=" * 60)