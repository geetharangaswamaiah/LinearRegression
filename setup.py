from setuptools import setup

setup(
	name = 'LinearRegression',
	version = '1.0',
	description = 'Python Library for Supervised Learning Algorithm, Linear Regression',
	author = 'Geetha Rangaswamaiah',
	author_email = 'rgeetha2010@gmail.com',
	packages = ['LinearRegression'],
	install_requires = [
		'numpy'
		],
	classifiers = [
		'License :: MIT License',
		'Programming Language :: Python :: 3.0',
		'Topic :: Regression :: Linear Regression'
		],
	include_package_data = True
)
