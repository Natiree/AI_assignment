from tensorflow.keras.datasets import mnist

# Download and load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("MNIST dataset downloaded successfully.")

print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape) 
