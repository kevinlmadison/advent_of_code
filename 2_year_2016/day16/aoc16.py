def flip_n_switch(in_str):
    b = in_str[::-1]
    c = []
    for i in range(len(b)):
        if b[i] == '1':
            c.append('0')
        else:
            c.append('1')
    ret = in_str + '0' + ''.join(c)
    return ret

def bstr_to_int(in_str):
    t, k = 0, 1
    for i in range(len(in_str) - 1, -1, -1):
        if in_str[i] == '1':
            t += k
        k *= 2
    return t

def check_sum(in_str):
    t = []
    for i in range(0, len(in_str) - 1, 2):
        if in_str[i] == in_str[i + 1]:
            t.append('1')
        else:
            t.append('0')
    t = ''.join(t)
    return t

if __name__ == '__main__':

    a = '10001110011110000'
    #d = 272  part 1
    d = 35651584 # part 2
    while len(a) < d:
        a = flip_n_switch(a)

    a = a[0:d]

    print(a)

    c = check_sum(a)
    while len(c) % 2 == 0:
        c = check_sum(c)

    print('checksum: ' + c)
