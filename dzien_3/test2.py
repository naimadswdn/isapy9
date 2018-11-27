meats = ['all_rest_meats_from_the_whole_world','chicken', 'beef', 'pork','turkey','all_rest_meats_from_the_whole_world']
table_elements = ['+', '-', '|']

fish = ['tuna', 'salmon']

#meats.append(fish)
print(meats)

for i in range((len(meats))):
    print(f'{meats[i]}: {len(meats[i])}')


print(any(isinstance(i, list) for i in meats))
