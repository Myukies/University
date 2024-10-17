import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import seaborn as sns

# Define the URL to a small sample dataset
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv'  # Example dataset URL

# Load dataset directly from the URL
data = pd.read_csv(url)

print("Siddhant Athawale T071")

# Display the first few rows of the dataset to understand its structure
print("Dataset Preview:")
print(data.head())

# Display the columns of the dataset to identify correct names
print("\nColumns in Dataset:")
print(data.columns)

# Assuming we need to modify these column names based on actual data structure
# For demonstration purposes, let's create a mock example:
data = pd.DataFrame({
    'Transaction': ['T1', 'T1', 'T2', 'T2', 'T3', 'T3'],
    'Item': ['Milk', 'Bread', 'Milk', 'Diaper', 'Bread', 'Eggs']
})

# Preprocess data into a one-hot encoded DataFrame
basket = (data.groupby(['Transaction', 'Item'])['Item']
          .count().unstack(fill_value=0).reset_index()  # Use fill_value=0 to avoid NaN
          .set_index('Transaction'))
basket = basket.astype(bool).astype(int)  # Convert to boolean and then to int

# Generate frequent itemsets
frequent_itemsets = apriori(basket, min_support=0.01, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Plotting support vs confidence
plt.figure(figsize=(10, 6))
sns.scatterplot(data=rules, x='support', y='confidence', size='lift', sizes=(20, 200), alpha=0.5)
plt.title('Support vs Confidence')
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.grid()
plt.show()

# Visualizing Evaluation Metrics: Support, Confidence, and Lift
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Support Bar Plot
sns.barplot(ax=axes[0], x='antecedents', y='support', data=rules)
axes[0].set_title('Support of Rules')
axes[0].set_ylabel('Support')

# Confidence Bar Plot
sns.barplot(ax=axes[1], x='antecedents', y='confidence', data=rules)
axes[1].set_title('Confidence of Rules')
axes[1].set_ylabel('Confidence')

# Lift Bar Plot
sns.barplot(ax=axes[2], x='antecedents', y='lift', data=rules)
axes[2].set_title('Lift of Rules')
axes[2].set_ylabel('Lift')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Display rules in a well-formatted manner
print("\nAssociation Rules:")
for index, row in rules.iterrows():
    antecedents = ', '.join(list(row['antecedents']))
    consequents = ', '.join(list(row['consequents']))
    print(f"Rule: If you buy {antecedents}, you are likely to also buy {consequents}.")
    print(f"Support: {row['support']:.4f}, Confidence: {row['confidence']:.4f}, Lift: {row['lift']:.4f}\n")
