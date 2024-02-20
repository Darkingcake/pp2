n = int(input("enter a num: "))
def sqr():
    for i in range (1, 1 + n):
        yield pow(i, 2)
for i in sqr():
    print(i)