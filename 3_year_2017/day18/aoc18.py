from collections import *
from functools import reduce
import itertools
import string
import multiprocessing.pool

def solve(ins):
    f = None
    rcv = None
    r = defaultdict(int)
    pc = 0
    while pc >= 0 and pc < len(ins):
        i = ins[pc]
        do, rd, rs= i[0], i[1], i[2] if len(i) > 2 else None
        if rs is not None:
            if rs in string.ascii_lowercase:
                rs = r[rs]
            else:
                rs = int(rs)
        if do == 'snd':
            f = r[rd]
        if do == 'set':
            r[rd] = rs
        if do == 'add':
            r[rd] += rs
        if do == 'mul':
            r[rd] *= rs
        if do == 'mod':
            if rs != 0:
                r[rd] %= rs
        if do == 'rcv':
            if r[rd] != 0:
                rcv = f
                print('part 1: {}'.format(rcv))
                break
        if do == 'jgz':
            if r[rd] > 0:
                pc += rs
                continue
        pc += 1


def solve2(ins):

    def gen(ID, rq, sq):
        r = defaultdict(int)
        r['p'] = ID
        send_count = 0
        pc = 0
        freq = None

        while 0 <= pc < len(ins):
            i = ins[pc]
            do, rd, rs= i[0], i[1], i[2] if len(i) > 2 else None
            if rs is not None:
                if rs in string.ascii_lowercase:
                    rs = r[rs]
                else:
                    rs = int(rs)
            if do == 'snd':
                if sq:
                    sq.put(r[rd])
                freq = r[rd]
                send_count += 1
            if do == 'set':
                r[rd] = rs
            if do == 'add':
                r[rd] += rs
            if do == 'mul':
                r[rd] *= rs
            if do == 'mod':
                if rs != 0:
                    r[rd] %= rs
            if do == 'rcv':
                #if r[rd] != 0:
                if rq:
                    try:
                        r[rd] = rq.get(timeout=5)
                    except queue.Empty:
                        return send_count
                elif r[rd] != 0:
                    return freq
            if do == 'jgz':
                if r[rd] > 0:
                    pc += rs
                    continue
            pc += 1
        
            if ID == 1:
                print('Thread {} send count: {}'.format(ID, send_count))
        
        return send_count

    print('part 1: ', gen(0, None, None))

    #new to multiprocessing in python, this is from reddit
    pool = multiprocessing.pool.ThreadPool(processes=2)
    q0 = multiprocessing.Queue()
    q1 = multiprocessing.Queue()

    res0 = pool.apply_async(gen, (0, q0, q1))
    res1 = pool.apply_async(gen, (1, q1, q0))

    #res0.get()
    print('part 2', res1.get())

def main():
    f = open('input.txt').readlines()
    solve2([i.split() for i in f])

if __name__ == '__main__':
    main()
