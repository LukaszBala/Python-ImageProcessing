import getopt
import sys


def acquire_values():
    file = input("File path: ")
    output = input("Output name, without extension: ")
    action = input("Choose action:\n1.Regionprops\n2.Ordfilt2\n3.Opening, with circle element\n4.Hole filling\nAction: ")
    if file is None or file == "":
        sys.exit("No File Name")
    opening = False
    filling = False
    odfil = False
    center = False
    radius = 0
    x_dim = 0
    num = 0
    if action == "1":
        center = True
    elif action == "2":
        odfil = True
        radius = int(input("Mask Dimension y: "))
        x_dim = int(input("Mask Dimension x: "))
        num = int(input("Order Num: "))
    elif action == "3":
        opening = True
        radius = int(input("Radius: "))
    elif action == "4":
        filling = True
    else:
        sys.exit("Unknown Option")

    if radius is None or radius == 0:
        radius = 1
    if x_dim is None or x_dim == 0:
        x_dim = 1
    if num is None or num == 0:
        num = 1

    return radius, x_dim, num, file, output, opening, filling, odfil, center


def arguments():
    radius = 0
    num = 0
    x_dim = 0
    file = None
    output = "res"
    opening = False
    filling = False
    odfil = False
    center = False
    opts, args = getopt.getopt(sys.argv[1:], "r:f:o:n:x:1234")
    for o, a in opts:
        if o == "-r":
            radius = int(a)
        elif o == "-f":
            file = a
        elif o == "-o":
            output = a
        elif o == "x":
            x_dim = a
        elif o == "n":
            num = a
        elif o == "-3":
            opening = True
        elif o == "-4":
            filling = True
        elif o == "-2":
            odfil = True
        elif o == "-1":
            center = True
        else:
            assert False, "unhandled option"

    if file is None or file == "":
        sys.exit("No File Name")
    if radius is None or radius == 0:
        radius = 1
    if x_dim is None or x_dim == 0:
        x_dim = 1
    if num is None or num == 0:
        num = 1
    return radius, x_dim, num, file, output, opening, filling, odfil, center
