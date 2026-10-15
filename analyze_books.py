import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Read the Excel file
df = pd.read_excel('books_data.xlsx')

# 2. Clean data (Remove currency symbol '£' and convert price to float)
df['Price_Clean'] = (
    df['Price'].astype(str).str.replace('£', '', regex=True).astype(float)
)

# 3. Print Summary Statistics
print('--- Books Dataset Summary ---')
print(f'Total Books: {len(df)}')
print(f'Average Price: £{df["Price_Clean"].mean():.2f}')
print(f'Highest Price: £{df["Price_Clean"].max():.2f}')
print(f'Lowest Price: £{df["Price_Clean"].min():.2f}')

# 4. Rating Distribution
print('\n--- Rating Distribution ---')
print(df['Rating'].value_counts())

# 5. Generate and save price distribution plot
plt.figure(figsize=(10, 6))
sns.histplot(df['Price_Clean'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Count')
plt.savefig('price_distribution.png')
plt.close()

print(
    '\nData analysis completed successfully and the chart was saved as price_distribution.png 🟢'
)