
# درس 20 تمرین سوم - تشخیص اعداد توان دو (مربع)


l = []

for i in range(1,100):
    m = 2 ** i
    l.append(m)

a = int(input('Enter a number: '))

if a in l:
    print('True')
else:
    print('False')