x, y, z = int(input('x=')), int(input('y=')), int(input('z='))

if x > 0 and y > 0 and z > 0:
    if x + y > z and x + z > y and y + z > x:
        print('True')