

def dog_years():
    """Program to calculate how old is dog in their age's scale."""
    scale = [10.5, 4]

    while True:
        age = input('Please provide number of dog years in human scale: ')
        try:
            age = float(age)
            break
        except:
            print('It is not a number! Please provide correct number.')
            continue

    if age <= 2:
        dog_age = age * scale[0]
        print (f"Your dog's age in dog scale is {dog_age} years.")
    else:
        dog_age = 2 * scale[0] + (age-2)*scale[1]
        print (f"Your dog's age in dog scale is {dog_age} years.")


dog_years()
