

def dog_years():
    """Program to calculate how old is dog in their age's scale."""
    from time import sleep
    from dzien_2.repeat_y_or_n import repeat_y_or_n
    from dzien_2.check_if_good import check_if_good

    print('Hello! This program is calculating how old is dog in their age\'s scale.')
    sleep(1.5)

    scale = [10.5, 4]

    age = None
    age = check_if_good(age, float, 'Please provide number of dog years in human scale: ')
    # while True:
    #     age = input('Please provide number of dog years in human scale: ')
    #     try:
    #         age = float(age)
    #         break
    #     except:
    #         print('It is not a number! Please provide correct number.')
    #         continue

    if age <= 2:
        dog_age = age * scale[0]
        print (f"Your dog's age in dog scale is {dog_age} years.")
    else:
        dog_age = 2 * scale[0] + (age-2)*scale[1]
        print (f"Your dog's age in dog scale is {dog_age} years.")
    repeat_y_or_n(dog_years)


def main():
    dog_years()


if __name__ == "__main__":
    main()
