# © Ashok-777
# GitHub: https://github.com/Ashok-777
# Part 2/4: Feature Engineering & Visualization

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import holidays

# Assuming df is already loaded
df['date'] = pd.to_datetime(df['date'])

# Extract date parts
df["year"] = df['date'].dt.year
df["month"] = df['date'].dt.month
df["day"] = df['date'].dt.day

# Weekend Feature
df['weekday'] = df['date'].dt.weekday
df['weekend'] = df['weekday'].apply(lambda x: 1 if x > 4 else 0)

# Holiday Feature (Indian holidays)
india_holidays = holidays.country_holidays('IN')
df['holidays'] = df['date'].dt.strftime('%Y-%m-%d').apply(lambda x: 1 if x in india_holidays else 0)

# Cyclical encoding for months
df['m1'] = np.sin(df['month'] * (2 * np.pi / 12))
df['m2'] = np.cos(df['month'] * (2 * np.pi / 12))

# Drop redundant 'date' and 'year'
df.drop(['date', 'year'], axis=1, inplace=True)

# Visualization
features = ['store', 'month', 'day', 'weekday', 'weekend', 'holidays']

plt.figure(figsize=(20, 10))
for i, col in enumerate(features):
    plt.subplot(2, 3, i + 1)
    df.groupby(col).mean()['sales'].plot.bar()
    plt.title(f"Avg Sales by {col}")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
df.groupby('day').mean()['sales'].plot(title="Average Sales by Day")
plt.show()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sb.histplot(df['sales'], kde=True)
plt.title("Sales Distribution")

plt.subplot(1, 2, 2)
sb.boxplot(x=df['sales'])
plt.title("Sales Outliers")
plt.show()

plt.figure(figsize=(10, 10))
numeric_df = df.select_dtypes(include=np.number)
if not numeric_df.empty:
    sb.heatmap(numeric_df.corr() > 0.8, annot=True, cbar=False)
    plt.title("Correlation Heatmap (> 0.8)")
    plt.show()

# Outlier Removal
df = df[df['sales'] < 140].reset_index(drop=True)
print(f"Shape after outlier removal: {df.shape}")
# © Ashok-777
# GitHub: https://github.com/Ashok-777
