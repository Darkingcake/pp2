n = int(input("enter num: "))
def dvsbl():
    for i in range (1, n + 1):
        if  i % 3 == 0 and i % 4 == 0:
            yield i
list = []
for i in dvsbl():
    list.append(str(i))
print(",".join(list))