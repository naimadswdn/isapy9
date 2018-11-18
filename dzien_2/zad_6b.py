
while True:
    try:
        binary = input('Please provide binary number: ')
        decimal = int(binary, 2)
        print(f'Your {binary} number is equal to {decimal}.')
        break
    except:
        print('Wrong binary number! Please correct it by using only 0 or 1.')
        continue
