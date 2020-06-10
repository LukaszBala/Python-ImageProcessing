import numpy as np


def centroid(img):
    y, x = img.shape[:2]
    res = np.zeros((256, 2))
    count = np.zeros((256, 1))
    for i in range(0, y):
        for j in range(0, x):
            value = int(img[i][j])
            res[value, 0] += j + 1
            res[value, 1] += i + 1
            count[value] += 1
    for i in range(0, 256):
        if count[i] != 0:
            res[i, 0] /= count[i]
            res[i, 1] /= count[i]
        else:
            res[i, 0] = 0
            res[i, 1] = 0
    return res


def equiv(img):
    y, x = img.shape[:2]
    count = np.zeros((256, 1))
    for i in range(0, y):
        for j in range(0, x):
            value = int(img[i][j])
            count[value] += 1
    for i in range(0, 256):
        count[i] = np.math.sqrt(count[i] / np.math.pi)
    return count * 2
