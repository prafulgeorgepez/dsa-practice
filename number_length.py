n = int(input('enter a number: '))
if n < 0:
    n = -n

if n == 0:
    print('length is 1')    
else:
    count = 0
    while n > 0:
        n //= 10
        count += 1
    print(f'length is {count}')
