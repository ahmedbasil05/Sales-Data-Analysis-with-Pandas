import pandas as pd

# Load the dataset
df = pd.read_csv("sales.csv")

# Check first few rows
print("\n--- First 5 Rows ---")
print(df.head())

# Dataset info
print("\n--- Data Info ---")
print(df.info())

# Summary stats
print("\n--- Summary Statistics ---")
print(df.describe())

# Missing values check
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Fill missing numeric values with mean
df['Price'].fillna(df['Price'].mean(), inplace=True)

# Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')

# Drop rows with invalid dates
df.dropna(subset=['OrderDate'], inplace=True)

# Add total value column
df['TotalValue'] = df['Quantity'] * df['Price']

# Extract month and year
df['Month'] = df['OrderDate'].dt.month_name()
df['Year'] = df['OrderDate'].dt.year

# Orders above $500
print("\n--- Orders Above $500 ---")
print(df[df['TotalValue'] > 500][['Customer', 'Product', 'TotalValue']])

# Electronics orders in 2024
print("\n--- Electronics Orders in 2024 ---")
print(df[(df['Category'] == 'Electronics') & (df['Year'] == 2024)])

# Total sales by product
print("\n--- Total Sales by Product ---")
print(df.groupby('Product')['TotalValue'].sum())

# Total sales by category
print("\n--- Total Sales by Category ---")
print(df.groupby('Category')['TotalValue'].sum())

# Total sales by month (sorted)
print("\n--- Total Sales by Month ---")
print(df.groupby('Month')['TotalValue'].sum().sort_values(ascending=False))

# Multiple aggregations by category
print("\n--- Quantity & Sales by Category ---")
print(df.groupby('Category').agg({'Quantity': 'sum', 'TotalValue': 'sum'}))

# Top-selling products
print("\n--- Top Selling Products by Revenue ---")
print(df.groupby('Product')['TotalValue'].sum().sort_values(ascending=False))

# Rank customers by spending per year
df['CustomerRank'] = df.groupby('Year')['TotalValue'].rank(ascending=False, method='dense')
print("\n--- Customer Ranking ---")
print(df[['Customer', 'Year', 'TotalValue', 'CustomerRank']])

# Pivot table: sales by category per month
print("\n--- Sales by Category per Month ---")
pivot = df.pivot_table(values='TotalValue', index='Category', columns='Month', aggfunc='sum', fill_value=0)
print(pivot)

# Cross-tab: order counts by category and month
print("\n--- Orders Count by Category and Month ---")
print(pd.crosstab(df['Category'], df['Month']))

# Orders per category
print("\n--- Orders per Category ---")
print(df['Category'].value_counts())

# Save cleaned data
df.to_csv("cleaned_sales.csv", index=False)
print("\n✅ Cleaned and processed data saved to cleaned_sales.csv")
