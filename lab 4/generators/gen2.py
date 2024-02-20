n = int(input("enter num: "))
def even():
    for even in range (0, 1 + n, 2):
        yield even
list = []
for i in even():
    list.append(str(i))
print(",".join(list))    
