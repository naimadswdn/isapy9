# Program to show list content in format like:
#   +------+------+------+
#   | col1 | col2 | col3 |
#   +------+------+------+
# where list is ['col1','col2','col3']

# pack all code to the function
# add condition to max_len >30 - second function, called by if?
# add table view if more lists in the list

meats = ['all_rest_meats_from_the_whole_world','chicken', 'beef', 'pork','turkey','all_rest_meats_from_the_whole_world']
table_elements = ['+', '-', '|']

# print(meats)


def table_print(t):
    max_len = max([len(i) for i in t])
    if max_len > 30:
        max_len = 30
    else:
        pass

    # print(max_len)

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


table_print(meats)