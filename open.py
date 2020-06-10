from PIL import Image
import numpy as np


def create_mask(radius):
    y, x = np.ogrid[:2 * radius + 1, :2 * radius + 1]
    center = (radius, radius)
    dist_from_center = np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
    mask = dist_from_center <= radius
    return mask


def erosion(x, y, radius, mask, img):
    res = np.zeros((y, x))
    res = np.uint8(res)

    minimum = 255

    for i in range(0, y):
        for j in range(0, x):
            for ry in range(-radius, radius + 1):
                for rx in range(-radius, radius + 1):
                    if mask[radius + ry][radius + rx]:
                        if y > i + ry >= 0:
                            if x > j + rx >= 0:
                                minimum = min(img[i + ry][j + rx], minimum)
            res[i][j] = minimum
            minimum = 255

    return res


def dilatation(x, y, radius, mask, img):
    res = np.zeros((y, x))
    res = np.uint8(res)

    maximum = 0

    for i in range(0, y):
        for j in range(0, x):
            for ry in range(-radius, radius + 1):
                for rx in range(-radius, radius + 1):
                    if mask[radius + ry][radius + rx]:
                        if y > i + ry >= 0:
                            if x > j + rx >= 0:
                                maximum = max(img[i + ry][j + rx], maximum)
            res[i][j] = maximum
            maximum = 0

    return res


def open_circle(radius, img):
    y, x = img.shape[:2]
    mask = create_mask(radius)
    res = erosion(x, y, radius, mask, img)
    res = dilatation(x, y, radius, mask, res)
    return res


def img_to_logical(data):
    return Image.fromarray(data * 255, mode='L').convert('1')


