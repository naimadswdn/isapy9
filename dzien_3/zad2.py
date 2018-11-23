# Program to calculate remainder from money in PLN

coins = [5, 2, 1, 0.5, 0.2, 0.1]

money = input('Please provide amount of money to calculate remainder: ')
money = float(money)

# for i in coins:
#     check_modulo = lambda x : x % i
#
#     if check_modulo(money) == 0:
#         amount = money / i
#         print(f'{i}: {amount}')
#         if amount * i == money:
#             break
#         else:
#             continue
#     else:
#         continue

for i in coins:
    check_modulo = lambda x : x % i
    check_dev = lambda  x : x / i
    if check_modulo(money) == 0 and check_dev(money) !=0:
        print(f'{i}: {check_dev(money)}')
        money = money - i*check_dev(money)
    elif check_modulo(money) != 0 and check_dev(money) !=0:
        pass


