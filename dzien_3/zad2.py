# Program to calculate remainder from money in PLN

coins = [5, 2, 1, 0.5, 0.2, 0.1]

money = input('Please provide amount of money to calculate remainder: ')
money = float(money)


#TO DO: not 0 ammount/ align/ def?

for i in coins:
    check_modulo = lambda x : round(x % i,1)
    check_div = lambda  x : x / i
    if check_modulo(money) == 0 and check_div(money) !=0:
        # print('ahoj') just to show if the if block was used
        print(f'{i}: {check_div(money)}')
        money = money - i*check_div(money)
    elif check_modulo(money) != 0 and check_div(money) !=0:
        div_floor = lambda  x : x //i
        print(f'{i}: {div_floor(money)}')
        # print(check_modulo(money)) #just to check current number
        money = check_modulo(money)
    elif check_modulo(money) == 0 and check_div(money) ==0:
        break
    elif check_modulo(money) != 0 and check_div(money) ==0:
        print('Impossible condition. How did you call it?!')
        break




