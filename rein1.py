def number():
    x = int(input())
    if x == 1:
        print('1st')
    elif x == 2:
        print('2nd')
    elif x == 3:
        print('3rd')
    elif x > 3:
        print(f'{x}th')

number()
