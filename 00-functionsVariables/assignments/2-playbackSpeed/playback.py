def main():
    n = input('').split(' ')
    slow(n)

def slow(n):
    for m in n :
        if m == n[-1]:
            print(m)
        else:
            print(m,end='...')


if __name__ == "__main__":
    main()
