# вход: кортеж точек эталона и кортеж проверяемого; выход (совпало, всего)
def matchingPoint(r, v):
    all = 0
    match = 0
    for i in v[0]:
        x = range(i[0]-15, i[0]+15)
        y = range(i[1]-15, i[1]+15)
        all += 1
        for j in r[0]:
            if j[0] in x and j[1] in y:
                match += 1
                break
    for i in v[1]:
        x = range(i[0]-15, i[0]+15)
        y = range(i[1]-15, i[1]+15)
        all += 1
        for j in r[1]:
            if j[0] in x and j[1] in y:
                match += 1
                break

    return (match, all)
