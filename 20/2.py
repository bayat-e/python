# درس 20 تمرین دوم - تشخیص اعداد مربع کامل

l = []

for i in range(1,1000):
    m = i ** 2
    l.append(m)

a = int(input('Enter a number: '))

if a in l:
    print('True')
else:
    print('False')

