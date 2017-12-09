'''Ideally we would be able to do everything without augmenting the input stream but I've
    got studying to do so this was my first solution.
'''

def solve(stream):
    stream = list(stream)
    '''First we clear out all values that get cancelled by the ! character'''
    i = 0
    while i < len(stream) - 1:
        if stream[i] == '!':
            del stream[i + 1]
        i += 1

    '''Next we remove all the garbage'''
    i = 0
    garbage_total = 0
    while i < len(stream) - 1:
        if stream[i] == '<':
            while stream[i] != '>':
                garbage_total += 1 if stream[i] != '!' else 0
                del stream[i]

            '''Accounting for off by one error.'''
            garbage_total -= 1
            del stream[i]
        i += 1

    '''Now it should be easy to just add our groups with a stack.'''
    val = 0
    total = 0
    stack = []
    for i in stream:
        if i == '{': 
            stack.append(i)
            val += 1
        elif i == '}':
            total += val
            stack.pop()
            val -= 1

    print("Part 1: {}".format(total))
    print("Part 2: {}".format(garbage_total))


def main():
    f = open('input.txt').readline()
    solve(f)


if __name__ == '__main__':
    main()
