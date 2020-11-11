from random import randint
buf =[[i // 3 for i in range(9)] for j in range(3)]
W = 0
N = 0
prev = -1
while True:
    user = int(input())
    if user == 3:
        break
    if user > 3:
        print('illegal input')
        continue
    N += 1
    comp = (buf[max(prev, 0)][randint(0, len(buf[prev]) - 1)] + 1) % 3
    if prev != -1:
        buf[prev].append(user)
    prev = user
    print('computer = ', comp)
    if user == (comp + 1) % 3:
        print('You win')
    elif user == comp:
        print('Draw!')
    else:
        W += 1
        print('You lose')

print(W / N)
