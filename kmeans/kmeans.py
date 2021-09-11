"""
featurns:
1. if the array has empty array, it will error
2. Only-2d, need more function
3. code refactoring
"""



from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from numba import jit

def Eucdis(a, b):    # calculate distence
    return np.sqrt(np.sum(np.square(a - b)))

def getdata():    # get data from image
    global img
    img = Image.open('test.png')
    text_img = np.array(img.convert('RGB')).tolist() # convert to RGB
    data = []

    for x in range(img.size[1]):
        for y in range(img.size[0]):
            if text_img[x][y] != [255,255,255]:     # if not white
                data.append([x,y])    # data append
    return np.array(data)
data = getdata()

@jit()
def init(w, h, k):
    # random 2 array, and splicing。
    return np.append(np.random.randint(0,w,size=(k,1)),np.random.randint(0,h,size=(k,1)),axis=1)


def focus(data):
    return [np.mean(data[:,0]),np.mean(data[:,1])]       # calculate focus


def kmean(data,k,c=None,lastNum=None):
    def emptyList(k):
        a = []
        for x in range(k):
            a.append([])
        return a
    a = emptyList(k)
    # if "c" is none, init "c"
    if c==None:
        c = init(img.size[0],img.size[1],k)
    if lastNum==None:
        lastNum=[]

    for x in data:
        q = np.array(list(map(Eucdis,c,[x]*k)))
        #print(q)
        a[np.argmin(q)].append(x)
    print(a)
    def nowNum():
        nowNum=[]
        for o in range(k):
            nowNum.append(len(a[o]))
        return nowNum
    def show():
        for x in range(len(a)):
            ax = np.array(a[x])
            #print(c[x])
            plt.scatter(ax[:,0],ax[:,1])
            #plt.scatter(c[x][0],c[x][1],marker='*')
        plt.show()
    # print(nowNum())
    # print(lastNum)
    if nowNum()==lastNum:
        show()
    else:
        thisnum = nowNum()
        cc = []
        for x in range(k):
            cc.append(focus(np.array(a[x])))
        kmean(data,k,c=cc,lastNum=thisnum)


#print(data)
kmean(data,4)


#plt.scatter(data[:,0], data[:,1],s=10)
#plt.show()