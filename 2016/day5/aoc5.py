from hashlib import md5
init = 'ffykfhsq'
password = ['_', '_', '_', '_', '_', '_', '_', '_']
for i in range(100000000):
    h = md5((init + str(i)).encode()).hexdigest()
    if h[:5] == '00000':
        if h[5] in '01234567' and password[int(h[5])] == '_':
            password[int(h[5])] = h[6]
            print("decrypting: ", ''.join(password), "at iter: ", i, "hash: ", h, end="\r", flush = True)
    if '_' not in password:
        break
print('\n')
print("pass: ", ''.join(password))
