from hashlib import md5
init = 'ckczppom'
for i in range(10000000):
    h = md5((init + str(i)).encode()).hexdigest()
    if h[:6] == '000000':
        print(i)
        print(h)
        break
