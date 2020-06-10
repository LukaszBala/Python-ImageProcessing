import numpy as np


def ordfilt_func(img, index, mask):
    dimension = img.shape
    y, x = dimension[:2]
    ym, xm = mask.shape[:2]
    if index > ym*xm:
        index = ym*xm
    res = np.zeros((y, x))
    res = np.uint8(res)

    for i in range(0, y):
        for j in range(0, x):
            li = list()
            for o in range(0, ym):
                for p in range(0, xm):
                    if not mask[o][p]:
                        continue
                    if i + o < y and j + p < x:
                        li.append(img[i + o][j + p])
                    # else:
                    #     li.append(0)
            li.sort()
            if len(li) >= index:
                res[i][j] = li[index - 1]
            else:
                res[i][j] = li[len(li) - 1]
    return res


def ordfilt2(img, index, mask):
    dimension = img.shape

    if len(dimension) >= 3:
        res = np.zeros(dimension)
        res[:, :, 0] = ordfilt_func(img[:, :, 0], index, mask)
        res[:, :, 1] = ordfilt_func(img[:, :, 1], index, mask)
        res[:, :, 2] = ordfilt_func(img[:, :, 2], index, mask)
    else:
        res = ordfilt_func(img, index, mask)
    return res
