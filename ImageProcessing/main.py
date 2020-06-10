#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
import sys
from ImageProcessing import filtr, arg, open, holes, regionprops
import os


def main():
    if len(sys.argv) > 1:
        radius, x_dim, num, file, output, opening, filling, odfil, center = arg.arguments()
        if opening is None and filling is None and odfil is None and center is None:
            radius, x_dim, num, file, output, opening, filling, odfil, center = arg.acquire_values()
    else:
        radius, x_dim, num, file, output, opening, filling, odfil, center = arg.acquire_values()

    try:
        img = Image.open(file)
    except IOError:
        sys.exit("File Does not Exist or corrupted, or format unknown")
    bits = img.mode
    img_np = np.array(img)
    dimension = len(img_np.shape)

    if not os.path.exists("results"):
        try:
            os.mkdir("results")
        except OSError:
            pass

    exist = os.path.exists("results")
    extension = None
    try:
        extension = file.split(".")[1]
    except ValueError:
        pass

    if exist:
        str_path = "saved in result"
    else:
        str_path = "saved in current directory"

    if opening:
        if dimension > 2:
            sys.exit("Opening can be done only with monochrome or bitmap")
        res = open.open_circle(radius, img_np)
        if bits == "1":
            img = open.img_to_logical(res)
            if exist:
                img.save("results/{}.bmp".format(output))
            else:
                img.save("{}.bmp".format(output))
        else:
            img = Image.fromarray(res)
            if extension is not None:
                if exist:
                    img.save("results/{}.{}".format(output, extension))
                else:
                    img.save("{}.{}".format(output, extension))
            else:
                if exist:
                    img.save("results/{}.jpg".format(output))
                else:
                    img.save("{}.jpg".format(output))
        print(str_path)

    if filling:
        if dimension > 2:
            sys.exit("Opening can be done only with bitmap")
        if bits != "1":
            sys.exit("Filling Holes only to logical images")
        res = holes.fill(img_np)

        img = open.img_to_logical(res)

        if exist:
            img.save("results/{}.bmp".format(output))
        else:
            img.save("{}.bmp".format(output))
        print(str_path)

    if odfil:
        mask = np.full((radius, x_dim), True, dtype=bool)
        res = filtr.ordfilt2(img_np, num, mask)
        img = Image.fromarray(res.astype(np.uint8))
        if extension is not None:
            if exist:
                img.save("results/{}.{}".format(output, extension))
            else:
                img.save("{}.{}".format(output, extension))
        else:
            if exist:
                img.save("results/{}.jpg".format(output))
            else:
                img.save("{}.jpg".format(output))
        print(str_path)

    if center:
        centroid = regionprops.centroid(img_np)
        equivalent = regionprops.equiv(img_np)
        res = np.zeros((256, 3))
        res[:, 0] = centroid[:, 0]
        res[:, 1] = centroid[:, 1]
        res[:, 2] = equivalent[:, 0]
        if exist:
            np.savetxt("results/{}_centroid.txt".format(output), centroid)
            np.savetxt("results/{}_equivalent.txt".format(output), equivalent)
            np.savetxt("results/{}.txt".format(output), res)
        else:
            np.savetxt("{}_centroid.txt".format(output), centroid)
            np.savetxt("{}_equivalent.txt".format(output), equivalent)
            np.savetxt("{}.txt".format(output), res)
        print(str_path)


if __name__ == "__main__":
    main()
