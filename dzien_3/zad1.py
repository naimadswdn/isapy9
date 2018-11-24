# Program to show list content in format like:
#   +------+------+------+
#   | col1 | col2 | col3 |
#   +------+------+------+
# where list is ['col1','col2','col3']

# pack all code to the function
# add condition to max_len >30 - second function, called by if?
# add table view if more lists in the list

meats = ['chicken', 'beef', 'pork','turkey','all_rest_meats_from_the_world']
table_elements = ['+', '-', '|']

print(meats)

max_len = max([len(i) for i in meats])
print(max_len)

for i in range(len(meats)):
    if i == 0:
        print(table_elements[0] + table_elements[1] * max_len + table_elements[0], end='')
    else:
        print(table_elements[1] * max_len + table_elements[0], end='')

print('')
for i in range(len(meats)):
    if i == 0:
        print(f'{table_elements[2]}{meats[i]:<{max_len}}{table_elements[2]}', end='')
    else:
        print(f'{meats[i]:<{max_len}}{table_elements[2]}', end='')

print('')

for i in range(len(meats)):
    if i == 0:
        print(table_elements[0] + table_elements[1] * max_len + table_elements[0], end='')
    else:
        print(table_elements[1] * max_len + table_elements[0], end='')

