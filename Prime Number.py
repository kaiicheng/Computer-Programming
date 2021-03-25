num1 = int(input('Input a number: '))  # input 1
num2 = int(input('Input b number: '))  # input 2


def prime(n):
    for i in range(2, n):
        if n % i == 0:  # 整除，i 是 n 的因數，所以 n 不是質數。
            return False
    return True     # 都沒有人能整除，所以 n 是質數。

count = 0
for i in range(num1, num2 + 1):   # 產生 2 到 n 的數字。
    is_prime = prime(i)    # 判斷 i 是否為質數。
    if is_prime:              # 如果是，印出來。
        count += 1
        if count == 10:
            print(i)
            count = 0
        else:
            print(i, end= " ")
