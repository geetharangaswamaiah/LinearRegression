import numpy as np

# Read data
datafile = 'ex1data1.txt'
cols = np.loadtxt(datafile,delimiter=',',usecols=(0,1),unpack=True) 
X = np.transpose(np.array(cols[:-1]))
y = np.transpose(np.array(cols[-1:]))

# Number of iterations for Gradient Descent
iterations = 1500

# Learning rate
alpha = 0.01

model = train(X, y, iterations, alpha)

accuracy = accuracy(model, X, y)

P = np.matrix([35000])
prediction = predict(P, model)

print("Accuracy -->" ,accuracy)
print("For population of" ,float(P),", profit prediction is " ,float(prediction))