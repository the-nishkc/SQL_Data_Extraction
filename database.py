import sqlite3
import pandas as pd

# Load CSV dataset
df = pd.read_csv("marketsales.csv")

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("%", "")
)

# Create SQLite database
conn = sqlite3.connect("supermarket.db")

# Store data in SQL table
df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

# Verify import
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM sales")

total_records = cursor.fetchone()[0]

print("=" * 50)
print("DATABASE CREATED SUCCESSFULLY")
print("=" * 50)
print(f"Total Records Imported : {total_records}")

conn.commit()
conn.close()