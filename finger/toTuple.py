import jwt


def toTuple(dictVar):
    dictVar = jwt.decode(dictVar, 'secret', algorithm=['HS512'])
    result1 = list()
    result2 = list()
    result = list()
    count = 0
    for i in range(2):
        i = str(i)
        for j in range(len(dictVar[i])):
            j = str(j)
            result2.append(dictVar[i][j])

            if len(result2) == 2:
                result1.append(tuple(result2))
                del result2
                result2 = list()

        count = 0
        result.append(result1)
        del result1
        result1 = list()
    return tuple(result)
