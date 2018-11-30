
def remainder_of_cash():
    """Program to calculate remainder from money in PLN"""
    from time import sleep
    from dzien_2.repeat_y_or_n import repeat_y_or_n
    from dzien_2.check_if_good import check_if_good

    print('Hello! This program is calculating remainder from your money (PLN).')
    sleep(1.5)

    coins = [5, 2, 1, 0.5, 0.2, 0.1]

    money = None
    money = check_if_good(money, float, 'Please provide amount of money to calculate remainder: ')
    # while True:
    #     money = input('Please provide amount of money to calculate remainder: ')
    #     try:
    #         money = float(money)
    #         break
    #     except:
    #         print('Wrong cash amount. Please correct it! ')
    #         continue

    for i in coins:
        check_modulo = lambda x : round(x % i, 1)
        check_div = lambda  x : x / i
        if check_modulo(money) == 0 and check_div(money) != 0:
            # print('ahoj') just to show if the if block was used
            print(f'{i:>3} PLN: {check_div(money)}')
            money = money - i*check_div(money)
            if money == 0:
                break
        elif check_modulo(money) != 0 and check_div(money) != 0:
            div_floor = lambda  x : x //i
            print(f'{i:>3} PLN: {div_floor(money)}')
            # print(check_modulo(money)) #just to check current number
            money = check_modulo(money)
            if money == 0:
                break
        elif check_modulo(money) == 0 and check_div(money) == 0:
            print('You have typed 0 as cash amount!')
            break
        elif check_modulo(money) != 0 and check_div(money) == 0:
            print('Impossible condition. How did you call it?!')
            break

    sleep(1)
    repeat_y_or_n(repeat_y_or_n)


remainder_of_cash()


