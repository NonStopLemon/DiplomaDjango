from . import templateSkeletize2 as sk
from . import toDict
from PIL import Image as im


# бинаризация изображения


def binary(img):
    bImg = []
    for i in range(img.size[0]):
        tmp = []
        for j in range(img.size[1]):
            t = img.getpixel((i, j))
            p = t[0]*0.3+t[1]*0.59+t[2]*0.11
            if p > 128:
                p = 1
            else:
                p = 0
            tmp.append(p)
        bImg.append(tmp)
    return bImg

 # возвращает список элементов, у которых нет одинакового в другом  списке 10*10


def __removeDouble(x, y):
    z = []
    for i in x:
        c = True
        for j in y:
            if i == j:
                c = False
        if c:
            z.append(i)
    for i in y:
        c = True
        for j in x:
            if i == j:
                c = False
        if c:
            z.append(i)
    return z


# на входе кортеж (ветвление, конечные)
def delNoisePoint(r):
    tmp = []
    tmp2 = []
    for i in r[1]:
        x = range(i[0]-5, i[0]+5)
        y = range(i[1]-5, i[1]+5)
        for j in r[0]:
            if j[0] in x and j[1] in y:
                tmp.append(i)
                tmp2.append(j)
    return (__removeDouble(r[0], tmp2), __removeDouble(r[1], tmp))


# подсчет количества черных в окрестности
def checkThisPoint(img, x, y):
    c = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if img[i][j] == 0:
                c += 1
    return c-1


# формирование списков точек ветвления и конечных
def findCheckPoint(img):
    x = len(img)
    y = len(img[0])
    branchPoint = []
    endPoint = []
    for i in range(x-1):
        for j in range(y-1):
            if img[i][j] == 0:
                t = checkThisPoint(img, i, j)
                if t == 1:
                    endPoint.append((i, j))
                if t == 3:
                    branchPoint.append((i, j))
    return (branchPoint, endPoint)


def checkFinger(r):
    reference = im.open(r).convert('RGB')

    ref = binary(reference)

    sk.tmpDelete(ref)
    rp = findCheckPoint(ref)
    rp = delNoisePoint(rp)
    d = toDict.convertDict(rp)
    # res = matchingPoint("From DB", rp)
    # r = (res[0]/(res[1]*1.))*100

    return d
