a = input('Expression: ')
b= int(a.split()[0])
c = a.split()[1]
d = int(a.split()[2])
if c == '+':
    print(float(b + d))

if c == '-':
    print(float(b - d))

if c == '*':
    print(float(b * d))

if c == '/':
    print(float(b/d))
