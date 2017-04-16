import numpy as np


# file = open('horse-colic.data.txt', 'r')
# f2 = open('train.txt', 'w')
#
# data = file.read()
# data = data.replace('?', '-100')
# f2.write(data)

a = np.loadtxt('train.txt')
print a, a.shape