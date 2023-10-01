#پروژه حدس زدن بازی اعداد با استفاده از حلقه  for_else.


from random import randint
n = randint(1, 100)
for c in range(1, 8):
    c += 1
    a = int(input('? '))
    if n == a:
        print('You Won!')
        exit()
    elif n > a:
        print('Greater')
    else:
        print('Smaller')
else:
    print('You lost')
