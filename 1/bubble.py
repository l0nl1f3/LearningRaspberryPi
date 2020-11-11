from random import randint
data = [randint(0,99) for i in range(10)]
print(data)
n = len(data)
for i in range(n):
    for j in range(i + 1, n):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
print(data)
