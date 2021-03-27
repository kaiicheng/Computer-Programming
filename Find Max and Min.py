number = input()
lst = list()
sentence = "Please enter " + str(number) + " number: "
for i in range(int(number)):
    key = input(sentence)
    lst.append(int(key))
print("MAX: ", end="")
print(max(lst), end=" ")
print("MIN: ", end="")
print(min(lst))