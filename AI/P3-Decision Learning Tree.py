import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import tree  # Import the tree module for visualizing the decision tree
#SIDDHANT ATHAWALE T071
print("Siddhant Athawale T071")
print("Libraries imported")

# Load the Iris dataset from sklearn
iris = load_iris()
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])
print("Dataframe of dataset created")

# Rename columns for easier access
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Check for any missing values
print("Null values in each column:\n", df.isnull().sum())

# Encode the target labels as integers (setosa=0, versicolor=1, virginica=2)
le = LabelEncoder()
df['species'] = le.fit_transform(df['species'])

# View the first few rows of the dataframe
print(df.head())

# X - Features, y - Label
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Initialize and train the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=0, criterion='gini')
clf.fit(X_train, y_train)

# Make predictions on the test set before pruning
predictions_test_before = clf.predict(X_test)
print("Accuracy on test set before pruning: {:.4f}".format(accuracy_score(y_test, predictions_test_before)))
print("Accuracy on training set before pruning: {:.4f}".format(accuracy_score(y_train, clf.predict(X_train))))

# Visualize the Decision Tree before pruning
plt.figure(figsize=(15, 10))
tree.plot_tree(clf, filled=True, feature_names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], class_names=iris.target_names)
plt.title("Decision Tree Before Pruning")
plt.show()

# Pruning
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

# Ensure impurities has the correct length
if len(impurities) > len(ccp_alphas):
    impurities = impurities[:-1]

# Train pruned decision trees for different alpha values
clfs = []
for ccp_alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)

# Evaluate accuracy for the pruned trees and find the best alpha
best_alpha = ccp_alphas[0]
best_accuracy = 0
for clf in clfs:
    predictions_test_pruned = clf.predict(X_test)
    accuracy = accuracy_score(y_test, predictions_test_pruned)
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_alpha = clf.get_params()['ccp_alpha']

# Print best alpha and accuracy after pruning
print("Best alpha after pruning: {:.4f}".format(best_alpha))
print("Accuracy on test set after pruning: {:.4f}".format(best_accuracy))

# Train the best pruned decision tree
best_clf = DecisionTreeClassifier(random_state=0, ccp_alpha=best_alpha)
best_clf.fit(X_train, y_train)
print("Accuracy on training set after pruning: {:.4f}".format(accuracy_score(y_train, best_clf.predict(X_train))))

# Visualize the Decision Tree after pruning
plt.figure(figsize=(15, 10))
tree.plot_tree(best_clf, filled=True, feature_names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], class_names=iris.target_names)
plt.title("Decision Tree After Pruning")
plt.show()

# Print classification report and confusion matrix for the final pruned decision tree
final_predictions_test = best_clf.predict(X_test)
print("Final Classification Report (Test Set):\n", classification_report(y_test, final_predictions_test))
