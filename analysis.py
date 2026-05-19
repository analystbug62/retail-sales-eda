# =========================
# IMPORT LIBRARIES
# =========================

import pandas as pd
import matplotlib.pyplot as plt


# =========================
# LOAD DATA
# =========================

df = pd.read_csv("data/retail_sales_dataset.csv")

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])


# =========================
# DATA INSPECTION
# =========================

# Display first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

# Unique categorical values
print(df["Gender"].unique())

print(df["Product Category"].unique())


# =========================
# SALES ANALYSIS
# =========================

# Total sales
total_sales = df["Total Amount"].sum()

# Average sales
average_sales = df["Total Amount"].mean()

print("Total Sales:", total_sales)

print("Average Sales:", average_sales)


# =========================
# CATEGORY ANALYSIS
# =========================

# Revenue by product category
top_category = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

print(top_category)

# Bar chart for category sales
top_category.plot(
    kind="bar",
    figsize=(7, 5)
)

plt.title("Sales by Product Category")

plt.xlabel("Category")

plt.ylabel("Total Sales")

plt.xticks(rotation=0)

plt.grid(axis="y")

# Save chart
plt.savefig("sales_by_category.png")

plt.show()


# =========================
# MONTHLY SALES ANALYSIS
# =========================

# Monthly revenue trend
monthly_sales = (
    df.groupby(df["Date"].dt.month)["Total Amount"]
    .sum()
)

print(monthly_sales)

# Line chart for monthly trend
monthly_sales.plot(
    kind="line",
    marker="o",
    figsize=(8, 5)
)

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Total Sales")

plt.grid(True)

plt.xticks(rotation=0)

# Save chart
plt.savefig("monthly_sales_trend.png")

plt.show()


# =========================
# CUSTOMER ANALYSIS
# =========================

# Gender-based sales analysis
gender_sales = (
    df.groupby("Gender")["Total Amount"]
    .sum()
)

print(gender_sales)

# Gender sales chart
gender_sales.plot(
    kind="bar",
    figsize=(6, 4)
)

plt.title("Sales by Gender")

plt.xlabel("Gender")

plt.ylabel("Total Sales")

plt.xticks(rotation=0)

plt.grid(axis="y")

# Save chart
plt.savefig("sales_by_gender.png")

plt.show()


# =========================
# AGE ANALYSIS
# =========================

# Top spending age groups
age_sales = (
    df.groupby("Age")["Total Amount"]
    .sum()
)

print(age_sales.sort_values(ascending=False).head())

