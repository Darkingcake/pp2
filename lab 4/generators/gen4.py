a = int (input("enter the start: "))
b = int (input("enter the end: "))
def sqrt():
    for i in range(a,b + 1):
        yield i ** 2
list = []
for i in sqrt():
    list.append(str(i))
print(",".join(list))