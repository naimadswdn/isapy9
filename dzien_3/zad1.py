
# pack all code to the function
# add condition to max_len >30 - second function, called by if?
# add table view if more lists in the list

meats = ['all_rest_meats_from_the_whole_world','chicken', 'beef', 'pork','turkey','all_rest_meats_from_the_whole_world']

fish = ['tuna', 'salmon']

# meats.append(fish)
# print(meats)


def create_list():
    """Function that allow user to create his own list."""
    from time import sleep

    print('Hello! This program is showing list content in some fancy format.\nFirst we need to create your own list. ')
    sleep(1.5)

    elements = input('How long your list is? Please provide number of list elements. ')
    while True:
        try:
            elements = int(elements)
            break
        except:
            print('Please provide integer number!')
            continue

    user_list = []

    for i in range (0, elements):
        args = input(f'Please provide list element ({i+1} of {elements}): ')
        user_list.append(args)

    #print(user_list)
    return user_list


def table_print(t):
    """ Program to show list content in format like:
   +------+------+------+
   | col1 | col2 | col3 |
   +------+------+------+
 where list is ['col1','col2','col3']
 :param t: list that is going to be print
"""
    from dzien_2.repeat_y_or_n import repeat_y_or_n

    table_elements = ['+', '-', '|']

    max_len = max([len(i) for i in t])
    if max_len > 30:
        max_len = 30
    else:
        pass

    print('Your list looks like:')

    for i in range(len(t)):
        if i == 0:
            print(table_elements[0] + table_elements[1] * max_len + table_elements[0], end='')
        else:
            print(table_elements[1] * max_len + table_elements[0], end='')

    print('')

    for i in range(len(t)):
        if i == 0:
            if len(t[i]) > 30:
                print(f'{table_elements[2]}{t[i][:27]:<{max_len-3}}...{table_elements[2]}', end='')
            else:
                print(f'{table_elements[2]}{t[i]:<{max_len}}{table_elements[2]}', end='')
        else:
            if len(t[i]) > 30:
                print(f'{t[i][:27]:<{max_len-3}}...{table_elements[2]}', end='')
            else:
                print(f'{t[i]:<{max_len}}{table_elements[2]}', end='')

    print('')

    for i in range(len(t)):
        if i == 0:
            print(table_elements[0] + table_elements[1] * max_len + table_elements[0], end='')
        else:
            print(table_elements[1] * max_len + table_elements[0], end='')

    print('')
    repeat_y_or_n(table_print)


def main():
    table_print(create_list())


if __name__ == "__main__":
    main()


