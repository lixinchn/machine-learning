import numpy as np


def fitSLR(x, y):
    n = len(x)
    denominator = 0
    numerator = 0

    for i in range(n):
        numerator += (x[i] - np.mean(x)) * (y[i] - np.mean(y))
        denominator += (x[i] - np.mean(x)) ** 2

    print 'numerator: ', numerator
    print 'denominator: ', denominator

    b1 = numerator / float(denominator)
    b0 = np.mean(y) / float(np.mean(x))
    return b0, b1

def predict(x, b0, b1):
    return b0 + b1 * x

x = [1, 3, 2, 1, 3]
y = [14, 24, 18, 17, 27]

b0, b1 = fitSLR(x, y)
print 'intercept: ', b0, ' slope: ', b1

x_test = 6
y_test = predict(x_test, b0, b1)
print 'y_test: ', y_test
