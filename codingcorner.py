import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("supermarket_sales - Sheet1.csv")
print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

df["date"] = pd.to_datetime(df["date"])

df["month"] = df["date"].dt.month_name()
df["day"] = df["date"].dt.day_name()

df["time"] = pd.to_datetime(df["time"], format="%H:%M")
df["hour"] = df["time"].dt.hour

df.to_csv("supermarket_sales_cleaned.csv", index=False)

print("\nCleaned Dataset Saved!")

plt.figure(figsize=(8,5))
plt.hist(df["total"], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

product_sales = df.groupby("product_line")["total"].sum()

plt.figure(figsize=(10,5))
plt.bar(product_sales.index, product_sales.values)
plt.xticks(rotation=30)
plt.title("Revenue by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

branch_sales = df.groupby("branch")["total"].sum()

plt.figure(figsize=(6,4))
plt.bar(branch_sales.index, branch_sales.values)
plt.title("Revenue by Branch")
plt.xlabel("Branch")
plt.ylabel("Revenue")
plt.show()

city_sales = df.groupby("city")["total"].sum()

plt.figure(figsize=(6,4))
plt.bar(city_sales.index, city_sales.values)
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()

payment_counts = df["payment"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(payment_counts.index, payment_counts.values)
plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.show()

gender_counts = df["gender"].value_counts()

plt.figure(figsize=(5,4))
plt.bar(gender_counts.index, gender_counts.values)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

customer_counts = df["customer_type"].value_counts()

plt.figure(figsize=(5,4))
plt.bar(customer_counts.index, customer_counts.values)
plt.title("Customer Type Distribution")
plt.xlabel("Customer Type")
plt.ylabel("Count")
plt.show()

daily_sales = df.groupby("date")["total"].sum()

plt.figure(figsize=(12,5))
plt.plot(daily_sales.index, daily_sales.values)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

hourly_sales = df.groupby("hour")["total"].sum()

plt.figure(figsize=(8,4))
plt.bar(hourly_sales.index, hourly_sales.values)
plt.title("Hourly Sales")
plt.xlabel("Hour")
plt.ylabel("Revenue")
plt.show()

numeric_df = df.select_dtypes(include=np.number)

corr = numeric_df.corr()

plt.figure(figsize=(10,6))
plt.imshow(corr, aspect='auto')
plt.colorbar()

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=90
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("BUSINESS INSIGHTS")
print("=" * 50)

print("\nHighest Revenue Branch:")
print(df.groupby("branch")["total"].sum().sort_values(ascending=False).head(1))

print("\nTop Revenue City:")
print(df.groupby("city")["total"].sum().sort_values(ascending=False).head(1))

print("\nBest Product Line:")
print(df.groupby("product_line")["total"].sum().sort_values(ascending=False).head(1))

print("\nMost Used Payment Method:")
print(df["payment"].value_counts().head(1))

print("\nPeak Sales Hour:")
print(df.groupby("hour")["total"].sum().sort_values(ascending=False).head(1))

print("\nEDA Completed Successfully!")
