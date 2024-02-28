import re 
a = input()
sss = "^a(b)*$"
if re.search(sss, a):
    print('True')
else:
    print('False')