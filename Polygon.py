import numpy as np
import math

num = 1

def RegularPolygon(n=3, side=1, x=0, y=0):
    # 填寫預設值
    global num
    getPerimeter(n, side)
    getArea(n, side)
    num = num + 1

def RegularPolygon2(number, newSide):
    # 填寫有邊數及邊長
    global num
    n = number
    side = newSide
    getPerimeter(n, side)
    getArea(n, side)
    num = num + 1


def RegularPolygon3(number, newSide, newX, newY):
    # 填寫有邊數及邊長，新的中心X及Y位置
    global num
    n = number
    x = newX
    y = newY
    side = newSide
    getPerimeter(n, side)
    getArea(n, side)
    getPoint(n, side, x, y)
    num = num + 1

def getPerimeter(n, side):
    # 得到周長
    answer = n * side
    print("Polygon ", end="")
    print(n, end="")
    print(" ", end="")
    print("perimeter: ", end="")
    print(answer)


def getArea(n, side):
    # 得到面積
    answer = n * side * side / (np.tan(np.pi / n) * 4)

    print("Polygon ", end="")
    print(n, end="")
    print(" ", end="")
    print("area: ", end="")
    print(answer)

def getPoint(n, side, x, y):
    # 得到
    l = (side * side / (2 - 2 * (np.cos((2 * np.pi) / n)))) ** (0.5)
    answer_x = l
    answer_y = 0
    point = [[x + l, y]]
    print(point[0])

    for i in range(1, n):
        a = x
        b = y
        a = (np.cos(i * (2 * np.pi / n)) * a - np.sin(i * (2 * np.pi / n)) * b) + x
        b = (np.sin(i * (2 * np.pi / n)) * a + np.cos(i * (2 * np.pi / n)) * b) + y
        new = [a, b]
        point.append(new)
        print(new)

r1 = RegularPolygon()
r2 = RegularPolygon2(6, 4)
r3 = RegularPolygon3(10, 4, 5.6, 7.8)
