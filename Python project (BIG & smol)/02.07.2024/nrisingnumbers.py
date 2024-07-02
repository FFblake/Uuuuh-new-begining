if __name__ == '__main__':
    n = int(input())
    for i in range(n): #Should really remember, that range() is a function
        print(i+1, end='')
    n = int(input())
    for i in range(n):
        print(3600+i)