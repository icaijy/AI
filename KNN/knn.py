import numpy as np
import warnings
import time
import random
warnings.filterwarnings('ignore')
d = open('knn.knn.data', 'r+')
data = d.readlines()
# data to list
tmp = []
for x in range(len(data)):
    data[x] = data[x].split(' ')
    tmp.append(data[x][-1].replace('\n',''))
    data[x].pop(-1)
data = np.array(data)
data = np.core.defchararray.strip(data, '').astype(int)

def KNN(w):
    w = np.array(w)
    distances = []
    def Bubble(arr):
        arr = list(arr)
        for n in range(len(arr) - 1):
            for x in range(0, len(arr) - 1 - n):
                a = arr[x][0]
                b = arr[x + 1][0]
                if a > b:
                    arr[x], arr[x + 1] = arr[x + 1], arr[x]
        return np.array(arr)

    def Eucdis(a,b):  # a is base data, b is new data
        return np.sqrt(np.sum(np.square(a - b)))
    for x in range(len(data)):
        distance = [Eucdis(a=np.array(data[x]), b=w), tmp[x]]
        distances.append(distance)

    sortDisd = Bubble(distances)[:3][:,1].tolist()
    d.write('\n')
    a = max(sortDisd,key=sortDisd.count)
    d.write(str(w[0])+' '+str(w[1])+' '+str(w[2])+' '+a)
    return a

if __name__ == '__main__':
    for x in range(10):
        a = random.randint(30,100)
        b = random.randint(30,100)
        c = random.randint(30,100)
        KNN([a,b,c])
