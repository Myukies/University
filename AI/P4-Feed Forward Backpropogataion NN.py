import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
#SIDDHANT ATHAWALE T071
print("Siddhant Athawale T071")
# Step 1: Load and Prepare the Data
iris = load_iris()
X = iris.data
y = iris.target

# Convert to DataFrame for visualization
data = pd.DataFrame(X, columns=iris.feature_names)
data['target'] = y
print(data.describe())
print()
print("Shape of the dataset is:", data.shape)
print()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 2: Build and Train the Feed Forward Neural Network
# Activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network parameters
input_layer_size = X_train.shape[1]
hidden_layer_size = 10  # Number of neurons in hidden layer
output_layer_size = 3   # Three classes in the Iris dataset
learning_rate = 0.01
epochs = 10000

# Initialize weights
np.random.seed(42)
weights_input_hidden = np.random.rand(input_layer_size, hidden_layer_size)
weights_hidden_output = np.random.rand(hidden_layer_size, output_layer_size)

# Training the Neural Network
mse_values = []
for epoch in range(epochs):
    # Feedforward
    hidden_layer_input = np.dot(X_train, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)

    final_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    final_output = sigmoid(final_layer_input)

    # One-hot encode the output
    y_train_onehot = np.zeros((y_train.size, y_train.max() + 1))
    y_train_onehot[np.arange(y_train.size), y_train] = 1

    # Compute the error
    error = y_train_onehot - final_output

    # Backpropagation
    d_final_output = error * sigmoid_derivative(final_output)
    error_hidden_layer = np.dot(d_final_output, weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update weights
    weights_hidden_output += np.dot(hidden_layer_output.T, d_final_output) * learning_rate
    weights_input_hidden += np.dot(X_train.T, d_hidden_layer) * learning_rate

    mse = np.mean(error**2)
    mse_values.append(mse)
    if epoch % 1000 == 0:
        print(f'Epoch {epoch}/{epochs}, MSE: {mse}')

# Visualize the training process
plt.figure(figsize=(10, 6))
plt.plot(mse_values, label="MSE during Training")
plt.xlabel("Epochs")
plt.ylabel("Mean Squared Error")
plt.title("Training Progress of the Neural Network")
plt.legend()
plt.show()

# Step 3: Evaluate the Neural Network
hidden_layer_input_test = np.dot(X_test, weights_input_hidden)
hidden_layer_output_test = sigmoid(hidden_layer_input_test)
final_layer_input_test = np.dot(hidden_layer_output_test, weights_hidden_output)
final_output_test = sigmoid(final_layer_input_test)

# Convert final output to class predictions
predictions = np.argmax(final_output_test, axis=1)

# Evaluate performance
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy * 100:.2f}%')
conf_matrix = confusion_matrix(y_test, predictions)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix of the Neural Network Predictions")
plt.show()
