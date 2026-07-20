# ================================================
# COMPANY SALES ANALYSIS 2024
# Analyst: (Muhammad Asad)
# Tools: Python, Pandas, Matplotlib
# ================================================

import pandas as pd
import matplotlib.pyplot as plt

# ── DATA ─────────────────────────────────────────
data = {
    "Order_ID": [1001,1002,1003,1004,1005,
                 1006,1007,1008,1009,1010],
    "Category": ["Furniture","Electronics","Stationery",
                  "Electronics","Furniture","Stationery",
                  "Electronics","Furniture","Stationery",
                  "Electronics"],
    "Product": ["Chair","Laptop","Pen","Mobile","Desk",
                "Notebook","Headphones","Sofa","Stapler","Tablet"],
    "City": ["Lahore","Karachi","Islamabad","Lahore","Karachi",
             "Islamabad","Lahore","Karachi","Islamabad","Lahore"],
    "Sales": [500,45000,30,25000,800,50,3500,12000,40,18000],
    "Profit": [150,4500,8,2500,200,12,700,1800,10,1800]
}

df = pd.DataFrame(data)

# ── BASIC ANALYSIS ────────────
print("=" * 40)
print("   COMPANY SALES ANALYSIS 2024")
print("=" * 40)

print("\n BASIC STATS:")
print("Total Sales:  $", df["Sales"].sum())
print("Total Profit: $", df["Profit"].sum())
print("Total Orders:  ", df.shape[0])
print("Average Sales: $", df["Sales"].mean())

# ── TOP PERFORMERS ─────────────
print("\n TOP PERFORMERS:")
max_sale = df["Sales"].max()
top_product = df[df["Sales"] == max_sale]["Product"].values[0]
top_city = df[df["Sales"] == max_sale]["City"].values[0]
max_profit = df["Profit"].max()
top_profit_product = df[df["Profit"] == max_profit]["Product"].values[0]

print("Top Product:", top_product)
print("Top City:   ", top_city)
print("Top Profit Product:", top_profit_product)

# ── CATEGORY ANALYSIS ────────────────────────────
print("\n CATEGORY WISE SALES:")
print(df.groupby("Category")["Sales"].sum())

print("\n CATEGORY WISE PROFIT:")
print(df.groupby("Category")["Profit"].sum())

# ── CITY ANALYSIS ────────────────────────────────
print("\n CITY WISE SALES:")
print(df.groupby("City")["Sales"].sum())

print("\n Analysis Complete!")
print("=" * 40)

# ── CHARTS ───────────────────────────────────────

# Chart 1 — Category wise Bar Chart
category_sales = df.groupby("Category")["Sales"].sum()
category_sales.plot(kind="bar", color=["steelblue","green","orange"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Chart 2 — Pie Chart
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.ylabel("")
plt.show()

# Chart 3 — City wise Bar Chart
city_sales = df.groupby("City")["Sales"].sum()
city_sales.plot(kind="bar", color=["red","blue","green"])
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Chart 4 — Profit Line Chart
df.plot(x="Product", y="Profit", kind="line",
        marker="o", color="purple")
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
