import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
print("Siddhant Athawale T071")
# Load Dataset (using Iris dataset as an example)
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['TARGET CLASS'] = iris.target

# Data Preprocessing (Scaling)
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(scaled_features, df['TARGET CLASS'], test_size=0.30)

# List of K values to evaluate
k_values = [1, 5, 10, 23]

# Loop through different K values and evaluate
for k in k_values:
    print(f"\n### Evaluating for K = {k} ###")
    # KNN Model with current K
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    # Predictions
    pred = knn.predict(X_test)
    # Confusion Matrix
    conf_matrix = confusion_matrix(y_test, pred)
    # Visualizing the Confusion Matrix
    plt.figure(figsize=(6,4))
    sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt='g')
    plt.title(f'Confusion Matrix for K={k}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()
    # Classification Report
    print(f'Classification Report for K={k}:')
    print(classification_report(y_test, pred))
# Choosing the Best K Value using Error Rate (Elbow Method)
error_rate = []
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))
# Plotting Error Rate vs K Value
plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()
