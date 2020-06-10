import numpy as np
from ImageProcessing import open


def fill(img):
    y, x = img.shape[:2]
    res = np.zeros((y + 2, x + 2))
    yn, xn = res.shape[:2]
    for i in range(0, yn):
        if i == 0 or i == yn - 1:
            for j in range(0, xn):
                res[i][j] = 1
        else:
            res[i][0] = 1
            res[i][xn - 1] = 1
    res2 = np.copy(res)
    mask = open.create_mask(1)
    while True:
        res2 = open.dilatation(xn, yn, 1, mask, res2)
        for i in range(1, yn-1):
            for j in range(1, xn - 1):
                if res2[i][j]:
                    if img[i-1][j-1]:
                        res2[i][j] = 0
        if np.array_equal(res, res2):
            break
        else:
            res = np.copy(res2)

    res = res2[1:y+1, 1:x+1]
    for i in range(0, y):
        for j in range(0, x):
            if res[i][j]:
                res[i][j] = 0
            else:
                res[i][j] = 1

    return res
