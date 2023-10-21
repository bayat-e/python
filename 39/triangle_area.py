

# مساحت مثلث از روی اضلاع

from math import sqrt

while True:
    try :
        s1 = int(input('Enter the first side of the triangle: '))
        s2 = 1
        s3 = 1
        if s1 == 0:
            print('You must not enter 0.')
        else:
            s2 = int(input('Enter the second side of the triangle: '))
            if s2 == 0:
                    print('You must not enter 0.')
            else:
                s3 = int(input('Enter the third side of the triangle: '))
                if s3 == 0:
                    print('You must not enter 0.')
        if s1 + s2 <= s3:
            raise Exception('The entered values ​​cannot form a triangle. Please try again.')
        elif s1 + s3 <= s2:
            raise Exception('The entered values ​​cannot form a triangle. Please try again.')
        elif s2 + s3 <= s1:
            raise Exception('The entered values ​​cannot form a triangle. Please try again.')
        else:
            p = (s1 + s2 + s3)/2
            a = sqrt(p * (p - s1) * (p - s2) * (p - s3))
        print(a)
        break

    except ValueError:
        print('You should enter a number.')
    except ZeroDivisionError:
        print('You must not enter 0.')
    except Exception as e:
        print(e)
