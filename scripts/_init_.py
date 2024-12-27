import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset (adjust the file path as necessary)
df = pd.read_csv('C:\Users\user\KaimTenx-week-3\scripts\Data-20241226T131628Z-001')

# Show the first few rows of the dataset to understand its structure
print(df.head())

# Step 2: Data Summarization

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Data Structure - Check dtypes of each column
print("\nData Types:")
print(df.dtypes)

# Step 3: Data Quality Assessment - Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Univariate Analysis
# Plot histograms for numerical columns
df[['TotalPremium', 'TotalClaim']].hist(bins=30, figsize=(12, 6))
plt.suptitle("Histogram of TotalPremium and TotalClaim")
plt.show()

# Plot bar chart for categorical columns (example: ZipCode)
plt.figure(figsize=(10, 6))
sns.countplot(x='ZipCode', data=df)
plt.title('Distribution of Insurance Policies by ZipCode')
plt.xticks(rotation=45)
plt.show()

# Step 5: Bivariate/Multivariate Analysis

# Scatter plot of TotalPremium vs TotalClaim colored by ZipCode
plt.figure(figsize=(12, 6))
sns.scatterplot(x='TotalPremium', y='TotalClaim', hue='ZipCode', data=df)
plt.title('TotalPremium vs TotalClaim by ZipCode')
plt.show()

# Correlation Matrix Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Step 6: Outlier Detection

# Boxplot to detect outliers in TotalPremium
plt.figure(figsize=(10, 6))
sns.boxplot(x='TotalPremium', data=df)
plt.title('Boxplot of TotalPremium')
plt.show()

# Step 7: Data Comparison and Trends
# Compare trends of insurance premiums by ZipCode
plt.figure(figsize=(12, 6))
sns.boxplot(x='ZipCode', y='TotalPremium', data=df)
plt.title('Insurance Premiums by ZipCode')
plt.xticks(rotation=45)
plt.show()

# Step 8: Creative Visualizations - Choose insights and create additional plots

# Example: Distribution of insurance claims based on coverage type (if applicable)
plt.figure(figsize=(10, 6))
sns.countplot(x='CoverType', data=df)
plt.title('Distribution of Claims by Coverage Type')
plt.show()

