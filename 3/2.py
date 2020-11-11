import numpy as np
import matplotlib.pyplot as plt

u1 = 22
u2 = 26
s1 = 1.5
s2 = 1.5
n = 7200

t1 = u1 + s1 * np.random.randn(n)
t2 = u2 + s2 * np.random.randn(n)
T = np.concatenate((t1, t2), axis = 0)
np.random.shuffle(T)


su = np.sum(T)

try:
    cluster = np.empty(2 * n)
    center1 = T[np.random.randint(n)]
    center2 = T[np.random.randint(n)]
    print(center1, center2, "!!")
    EPOCH = 0
    while EPOCH <= 50:
        print('Epoch = ', EPOCH)
        EPOCH += 1
        su1 = 0
        su2 = 0
        n1 = 0
        n2 = 0
        
        for i in range(2 * n):
            if abs(center1 - T[i]) < abs(center2 - T[i]):
                su1 += T[i]
                n1 += 1
                cluster[i] = 1
            else:
                su2 += T[i]
                n2 += 1
                cluster[i] = 0
    
        [pc1, pc2] = [center1, center2]
        center1 = su1 / n1
        center2 = su2 / n2 
        print(center1, center2)
    print('expected value = ', [u1, u2])
    print('predicted value = ', [center1, center2])
    plt.hist(T, 500, histtype = 'bar')
    plt.show()
except KeyboardInterrupt:
    pass
