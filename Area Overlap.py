print("Enter r1's center x-, y-coordinates, width, and height: ")
x1 = float(input())
y1 = float(input())
w1 = float(input())
h1 = float(input())
print("Enter r2's center x-, y-coordinates, width, and height: ")
x2 = float(input())
y2 = float(input())
w2 = float(input())
h2 = float(input())

if x1 - x2 >= 0:
    x_distance = x1 - x2
else:
    x_distance = x2 - x1
if y1 - y2 >= 0:
    y_distance = y1 - y2
else:
    y_distance = y2 - y1

if x_distance <= (w1-w2)/2 and y_distance <= (h1-h2)/2:
    print("r2 is inside r1")
elif x_distance <= (w1+w2)/2 and y_distance <= (h1+h2)/2:
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")


