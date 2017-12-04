
def part1(f):
    print(str(sum((1 if len(w.split()) == len(set(w.split())) else 0) for w in f)))
    
def part2(f):
    w = [[''.join(sorted(i)) for i in line.split()] for line in f]
    print(str(sum((1 if len(x) == len(set(x)) else 0) for x in w)))

# Dat butter 

def main():
    f = open('input.txt')
    part1(f)
    f = open('input.txt')
    part2(f)

if __name__ == '__main__':
    main()
