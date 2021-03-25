num = int(input("input a number: "))
# print(num)

def hanoi(num):
    if num == 1:
        return 1
    else:
        return 2*hanoi(num-1)+1

ans = hanoi(num)


print(ans)


