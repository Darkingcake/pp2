import datetime as d
tod = d.datetime.now()
yes = tod - d.timedelta(days=1)
tom = tod + d.timedelta(days=1)

print("Yesterday: ", yes.strftime("%d/%m/%Y"))
print("Today: ", tod.strftime("%d/%m/%Y"))
print("Tomorow: ", tom.strftime("%d/%m/%Y"))