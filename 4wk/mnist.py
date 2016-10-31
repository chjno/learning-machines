import cPickle
import gzip
import numpy as np


def encodeOneHot(index, count):
    a = np.zeros(count)
    a[index] = 1
    return a


def load():
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()

    tr = np.zeros((len(train_set[1]), 10))

    for i in range(len(train_set[1])):
        tr[i][train_set[1][i]] = 1.0


    va = np.zeros((len(valid_set[1]), 10))

    for i in range(len(valid_set[1])):
        va[i][valid_set[1][i]] = 1.0


    te = np.zeros((len(test_set[1]), 10))

    for i in range(len(test_set[1])):
        te[i][test_set[1][i]] = 1.0

    return tuple([train_set[0], tr]), tuple([valid_set[0], va]), tuple([test_set[0], te])
