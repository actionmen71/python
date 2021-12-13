import matplotlib as mlp
import numpy as np
from sklearn import datasets, linear_model
# since sklearn is a large library we import only what we need and use
from sklearn.metrics import mean_sqaured_error


diabet = datasets.load_diabetes()
# here we have loaded Diabetes data set in variable diabet
# now we will use diabet as a dataset

# print(diabet.keys())
# below are the resultant keys
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])

# print(diabet.DESCR )
# above statement will print descriptions about datasets



diabet_x =diabet.data[:,np.newaxis,2]
# here we loading 2nd index from diabet and loading it in diabet_x
print(diabet_x)

diabet_x_train = diabet_x[:-30]
 # for training purposes we are taking last 30 values from diabet_x
diabet_x_test = diabet_x[-30:]
 # for testing purposes we are taking first 20 values from diabet_x
diabet_y_train = diabet.target[:-30]
diabet_y_test = diabet.target[-30:]




model = linear_model.LinearRegression()
# we are using linearregression function from linear model

model.fit( )

