# вызов процедуры скелетизации, на входе список списков(после бинаризации)
def tmpDelete(img):
    w = len(img)
    h = len(img[0])
    count = 1
    while count != 0:  # повторять пок удалялся хотя бы один пиксель
        count = delete(img, w, h)
        if count:
            delete2(img, w, h)


# удаление пикселя по основному набору, возврат кол-ва удаленных
def delete(img, w, h):
    count = 0
    for i in range(1, h-1):
        for j in range(1, w-1):
            if img[j][i] == 0:
                if deletable(img, j, i):
                    img[j][i] = 1
                    count += 1
    return count
# удаление пикселя по шумовому набору


def delete2(img, w, h):
    for i in range(1, h-1):
        for j in range(1, w-1):
            if img[j][i] == 0:
                if deletable2(img, j, i):
                    img[j][i] = 1

# определение принадлежности 3*3 к шумам


def fringe(a):
    t = [[1, 1, 1, 1, 0, 1, 1, 1, 1],

         [1, 1, 1, 1, 0, 1, 1, 0, 0],
         [1, 1, 1, 0, 0, 1, 0, 1, 1],
         [0, 0, 1, 1, 0, 1, 1, 1, 1],
         [1, 1, 0, 1, 0, 0, 1, 1, 1],

         [1, 1, 1, 1, 0, 1, 0, 0, 1],
         [0, 1, 1, 0, 0, 1, 1, 1, 1],
         [1, 0, 0, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 1, 0],

         [1, 1, 1, 1, 0, 1, 0, 0, 0],
         [0, 1, 1, 0, 0, 1, 0, 1, 1],
         [0, 0, 0, 1, 0, 1, 1, 1, 1],
         [1, 1, 0, 1, 0, 0, 1, 1, 0]]
    for i in t:
        if a == i:
            return True


def check(a):
    t123457 = [1, 1, 0, 0, 1, 0]
    t013457 = [1, 1, 1, 0, 0, 0]
    t134567 = [0, 1, 0, 0, 1, 1]
    t134578 = [0, 0, 0, 1, 1, 1]
    t0123457 = [1, 1, 1, 0, 0, 0, 0]
    t0134567 = [1, 0, 1, 0, 0, 1, 0]
    t1345678 = [0, 0, 0, 0, 1, 1, 1]
    t1234578 = [0, 1, 0, 0, 1, 0, 1]

    t = [a[1], a[2], a[3], a[4], a[5], a[7]]
    if t == t123457:
        return True
    t = [a[0], a[1], a[3], a[4], a[5], a[7]]
    if t == t013457:
        return True
    t = [a[1], a[3], a[4], a[5], a[6], a[7]]
    if t == t134567:
        return True
    t = [a[1], a[3], a[4], a[5], a[7], a[8]]
    if t == t134578:
        return True
    t = [a[0], a[1], a[2], a[3], a[4], a[5], a[7]]
    if t == t0123457:
        return True
    t = [a[1], a[3], a[4], a[5], a[6], a[7], a[8]]
    if t == t1345678:
        return True
    t = [a[0], a[1], a[3], a[4], a[5], a[6], a[7]]
    if t == t0134567:
        return True
    t = [a[1], a[2], a[3], a[4], a[5], a[7], a[8]]
    if t == t1234578:
        return True
 # получение 3*3, передача на проверку для осн.


def deletable(img, x, y):
    a = []
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            a.append(img[j][i])
    return check(a)
 # получение 3*3, передача на проверку для шумов.


def deletable2(img, x, y):
    a = []
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            a.append(img[j][i])
    return fringe(a)
