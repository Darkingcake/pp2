import datetime as d
tod = d.datetime.now()
res = tod - d.timedelta(days=5)
print("Today: ", tod.strftime("%d/%m/%Y"))
print("Before five days: ", res.strftime("%d/%m/%Y"))