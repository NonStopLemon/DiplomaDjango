import jwt


def convertDict(tupleVar):
    result = dict()
    count = 0
    for j in range(2):
        toresult = dict()
        for i in tupleVar[j]:
            toresult[count] = i[0]
            toresult[count+1] = i[1]
            count += 2
        result[j] = toresult
        del toresult
        count = 0
    return jwt.encode(result, 'secret', algorithm='HS512')
