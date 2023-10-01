# درس 20 تمرین اول - محاسبه میانگین اعداد از پیش نامشخص

c = 0
s = 0

while True:
    
    a = int(input('Enter a number: '))

    if a <= 0:
        break
    c += 1    
    s += a
    
print(s/c)