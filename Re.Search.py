import re
name = 'My name is Vinh , I am fine '
if re.search('\Afine',name):
    print('Fine o dau cau')
else:
    print('Fine khong o cuoi cau')