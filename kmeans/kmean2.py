from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import random

def Eucdis(a, b):    # calculate distence
    return np.sqrt(np.sum(np.square(np.matrix(a) - np.matrix(b))))

def mean(arr):
    return [np.mean(arr, axis=0),np.mean(arr, axis=1)]

def bw(file,threshold=150,):
    '''

    :param file: file path or PIL.Image.Image object
    :param threshold: color value, more big, more deep
    :return: PIL Image
    '''

    # judge input
    if not isinstance(file, str):
        img = file

    else:
        img = Image.open(file)
    Img = img.convert('L')
    Img = Img.point([0] * (threshold - 1) + [1] * (257 - threshold), '1')
    return np.array(Img).tolist()

def kmeans(data,k):

    # init

    h,w = len(data),len(data[0])
    c, l = [[]]*k,[[]]*k
    for x in range(k):
        l[x] = [np.random.randint(h),np.random.randint(w)]
    # for x in range(10):
    d = []
    for x in range(h):
        for y in range(w):
            if data[x][y] == False:

                for z in l:
                    d.append(Eucdis([x,y],z))
                    break
                c[np.argmin(d)].append([x,y])
        # for x in range(k):
        #     c[x] = np.mean(l[x])
    plt.figure()
    print(c)
    for x in c:
        print(x)
        plt.scatter(np.array(x)[:,0],np.array(x)[:,1])
    plt.show()



kmeans(bw("test.png"),4)




