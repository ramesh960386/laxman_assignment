def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2) == 0:
            # n is even
            n = n//2
        else:
            # n is odd
            n = 3*n + 1
    print(1, end='')
 

if __name__ == '__main__':
    n = int(input('Enter n: '))
    print('Sequence: ', end='')
    collatz(n)