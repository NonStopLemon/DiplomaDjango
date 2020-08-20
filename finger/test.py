import jwt

t = {0: 1, 1: 2}

r = jwt.encode(t, 'secret', algorithm='HS512')
print(type(r))
r = str(r)
r = bytes(r, encoding='utf8')
print(r)
