def main():
    FILE = open("private_leaderboard.txt").readline().strip()
    print(FILE.split('-'))

if __name__ == '__main__':
    main()

