## Introduction

This module is designed to implement the linear regression in a generalized form usable with both univariate & multivariate datasets. [Numpy](https://www.numpy.org) has been used for the designing and optimization purposes.
The aim is to provide a very simple & strightforward way to use this algorithm for larger projects, and keep the functionality for every part separated.

## Usage

Import this module and call the ```calculate_weights()``` function while passing your dataset(must be in integer or float format) as the argument to update your weights according to the data. This function returns the weights in a numpy.ndarray format
The ```normalize()``` function may be used in case of multiple features, when their ranges differ by a huge margin ex. If x1 ranges between (-100, 100) and x2 between (-1, 1) then it is advised to normalize your data before proceeding. For very small differences in range, there should't be a need to perform this operation. This function returns the normalized feature vector in numpy.ndarray format with datatype float.
Call the ```calculate_biases()``` function only after the weights have been calculated, since this makes use of the weights in order to determine the bias vector. Returns a numpy.ndarray.
The function to fit the line requires only one line of calculation(```y = mx+b```), thus has been implemented as a [python lambda](https://docs.python.org/3/reference/expressions.html#lambda), simply call it as ```predict()``` and pass the dataset, weights & biases(in the order dataset, weight, bias). Returns the vector that gives the best fit line for the provided data.

Pending: Add weight/bias calculation with gradient descent for extremely large datasets & parallelization.

## Results

Running this module over the [Graduate Admissions 2](https://www.kaggle.com/mohansacharya/graduate-admissions) dataset from Kaggle, the following results were produced(visualized with matplotlib):

![Best Fit Visualization](https://drive.google.com/uc?id=1dKDSlvs1FLoUZ_MLsAUpMGurKMKARmjo)