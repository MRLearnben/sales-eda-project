# ============================================
# Sales Data - Exploratory Data Analysis (EDA)
# Author: Thilak
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. CREATE SAMPLE DATASET ──────────────────────────────────────────────────
np.random.seed(42)
n = 500

data = {
    'order_id':    range(1, n + 1),
    'date':        pd.date_range(start='2023-01-01', periods=n, freq='D'),
    'category':    np.random.choice(['Electronics', 'Clothing', 'Groceries', 'Books'], n),
    'region':      np.random.choice(['North', 'South', 'East', 'West'], n),
    'sales':       np.random.randint(500, 10000, n),
    'quantity':    np.random.randint(1, 20, n),
    'discount':    np.random.uniform(0, 0.4, n).round(2),
    'profit':      np.random.randint(-500, 3000, n),
}

df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)
print("✅ Dataset created!\n")

# ── 2. BASIC INFO ──────────────────────────────────────────────────────────────
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Stats:\n", df.describe())

# ── 3. SALES BY CATEGORY ──────────────────────────────────────────────────────
plt.figure(figsize=(8, 5))
category_sales = df.groupby('category')['sales'].sum().sort_values(ascending=False)
sns.barplot(x=category_sales.index, y=category_sales.values, palette='Blues_d')
plt.title('Total Sales by Category', fontsize=14)
plt.ylabel('Total Sales (₹)')
plt.tight_layout()
plt.savefig('sales_by_category.png')
plt.show()
print("✅ Chart 1 saved!")

# ── 4. MONTHLY SALES TREND ────────────────────────────────────────────────────
df['month'] = df['date'].dt.to_period('M')
monthly = df.groupby('month')['sales'].sum()

plt.figure(figsize=(12, 5))
monthly.plot(kind='line', marker='o', color='teal')
plt.title('Monthly Sales Trend', fontsize=14)
plt.ylabel('Total Sales (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_trend.png')
plt.show()
print("✅ Chart 2 saved!")

# ── 5. PROFIT vs DISCOUNT CORRELATION ────────────────────────────────────────
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x='discount', y='profit', hue='category', alpha=0.6)
plt.title('Profit vs Discount', fontsize=14)
plt.tight_layout()
plt.savefig('profit_vs_discount.png')
plt.show()
print("✅ Chart 3 saved!")

# ── 6. REGION-WISE PERFORMANCE ────────────────────────────────────────────────
plt.figure(figsize=(8, 5))
region_data = df.groupby('region')[['sales', 'profit']].sum()
region_data.plot(kind='bar', figsize=(8, 5), color=['steelblue', 'salmon'])
plt.title('Sales & Profit by Region', fontsize=14)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('region_performance.png')
plt.show()
print("✅ Chart 4 saved!")

# ── 7. INSIGHTS SUMMARY ───────────────────────────────────────────────────────
print("\n===== KEY INSIGHTS =====")
print(f"📌 Top Category by Sales  : {category_sales.idxmax()}")
print(f"📌 Total Revenue          : ₹{df['sales'].sum():,}")
print(f"📌 Average Order Value    : ₹{df['sales'].mean():.2f}")
print(f"📌 Total Profit           : ₹{df['profit'].sum():,}")
print(f"📌 Highest Sales Region   : {df.groupby('region')['sales'].sum().idxmax()}")