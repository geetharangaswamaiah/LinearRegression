## Python Library for Linear Regression

* Linear Regression is the Supervised Learning Algorithm that is used to find a linear relationship between input and output variables.
	- Simple Linear Regression: Single input variable, single output variable
	- Multiple Linear Regression: Multiple input variables, single output variable

* Install the library using the command pip3 install git+https://github.com/rgeetha2010/LinearRegression.git
  
* An example application is provided for reference. 

* model = train(X, y, num_iters, alpha):
  	- X: features of training set
  	- y: corresponding labels of training set
  	- num_iters: Number of iterations to run Gradient Descent
  	- alpha: Learning rate
  
* prediction = predict(X, model):
  	- model: trained model
  	- X: features of training set

* accuracy = accuracy(model, X, y):
  	- model: trained model
  	- X: features of training set
  	- y: corresponding labels of training set

* For multivariable Linear Regression, X_norm = featureNormalization(X):
	- X_norm: Normalized features
	- X: Original features
