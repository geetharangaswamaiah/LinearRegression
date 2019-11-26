import numpy as np

# Feature Normalization
def featureNormalization(X):
	[m, n] = np.shape(X)
	X_norm = X
	mu = np.zeros((1, n))
	sigma = np.zeros((1, n))
	mu = np.mean(X)
	sigma = np.std(X)
	for i in range(n):
		X_norm[:, i:] = (X[:, i:] - mu) /sigma
	return X_norm

# Hypothesis Function
def hypothesis(X, theta):
	# [m, n] = np.shape(X)
	# theta = theta.reshape(1, n)
	h = X @ (theta.T) # Matrix multiplication
	return h

# Cost Function
def costFunction(theta, X, y):
	J = 0
	[m, n] = np.shape(X)
	theta = theta.reshape(1, n)
	J = (hypothesis(X, theta) - y).T.dot(hypothesis(X, theta) - y) * (1 / (2 * m))
	return J

# Gradient Descent
def gradientDescent(theta, X, y, alpha, num_iters):
	[m, n] = np.shape(X)
	theta = theta.reshape(1, n)
	grad = theta
	J_hist = np.zeros((num_iters, 1))
	for iterations in range(1, num_iters):
		for i in range(n):
			grad[:, i:] = grad[:, i:] - (alpha / m) * ((hypothesis(X, theta) - y).T.dot(X[:,i:]))
		J_hist[:, i:] = costFunction(grad, X, y)
	return grad, J_hist # plot J to check if it converges

# Accuracy
def accuracy(theta, X, y):
	[m, n] = np.shape(X)
	theta = model[0]
	X = np.insert(X,0,1,axis=1)
	h = hypothesis(X, theta)
	cost = (np.sum(h - y)) / m
	accuracy = 100 - cost
	return accuracy

# Prediction
def predict(X, theta):
	X = np.insert(X,0,1,axis=1)
	pred = hypothesis(X, theta[0])
	return pred

# Train model
def train(X, y, num_iters, alpha):
	print("             --------------------------------------------------")
	print("             |                                                |")
	print("             |                Linear  Regression              |")
	print("             |                                                |")
	print("             --------------------------------------------------")
	print()
	print("Training the model ...")
	print()
	[m,n] = np.shape(X)
	X = np.insert(X,0,1,axis=1)
	initial_theta = np.zeros((X.shape[1],1))
	model = gradientDescent(initial_theta, X, y, alpha, num_iters)
	return model
  
