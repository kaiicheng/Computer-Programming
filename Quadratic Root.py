print("Enter a, b, c: ")
a = int(input())
b = int(input())
c = int(input())
x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
y = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
if 2*a == 0 or (b**2-4*a*c) < 0:
    print("The equation has no real roots")
elif x == y:
    print("The roots is ", end="")
    print(x)
else:
    print("The roots are ", end="")
    print(x, end="")
    print(" and ", end="")
    print(y)