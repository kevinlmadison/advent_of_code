from collections import defaultdict
from hashlib import md5 

def get_rep(string, length):
    for idx in range(len(string) - (length - 1)):
        if len({string[idx + i] for i in range(length)}) == 1:
            return string[idx]
    return None

init = 'ihaygndm'
index = 0
hashes = []
prospects = defaultdict(list)

while not (len(hashes) > 64):
    h = md5((init + str(index)).encode()).hexdigest()
    for _ in range(2016):
        h = md5((h).encode()).hexdigest()
    five = get_rep(h, 5)
    if five is not None:
        for (p_idx, h) in prospects[five]:
            if(index - p_idx) <= 1000:
                hashes.append((p_idx, h))
                print("Hash " + str(index) + " : " + str(p_idx))
            hashes.sort()
            prospects[five] = []

    three = get_rep(h, 3)
    if three is not None:
        prospects[three].append((index, h))
    index += 1

print('last hash: ' + str(hashes[63]))
