import datetime as d
def withoutmicro(data):
    return data.replace(microsecond = 0)
data = d.datetime.now()
muew = withoutmicro(data)
print("With microseconds: ", data)
print("Without microseonds: ", withoutmicro(muew))