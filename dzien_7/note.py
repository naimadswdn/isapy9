import pickle


def open_note(note_file):
    note = open(note_file, 'rb+')
    return note


def close_note(dz_file):
    dz_file.close()


def add_value():
    date = input('Please provide data for note: ')
    text = input('Please provide text for note: ')
    value = {'date': date, "text": text}
    list = []
    old_notes = display_note(dz_file)
    list.append(old_notes)
    list.append(value)
    pickle.dump(list, dz_file)
    print('Note saved.')


def menu():
    print('Hello in my diary:\n'
          'Options:\n'
          '1. Open note.\n'
          '2. Write new note.\n'
          '3. Delete note.\n'
          '4. Find note\n'
          '5. Exit.\n')


# def save_value(value):
#
#     return obj


def display_note(dz_file):
    try:
        data_to_display = pickle.load(dz_file)
        for i, j in data_to_display.items():
            print(f'{i}: {j}')
        print(type(data_to_display))
        return data_to_display
    except EOFError:
        print('File is empty!')


def ask():
    user_choice = input('What do you want to do? ')
    if user_choice == '5':
        exit()
    elif user_choice == '1':
        print('Your notes:')
        dz_file = open_note(note_file)
        display_note(dz_file)
        close_note(dz_file)
    elif user_choice == '2':
        print('Adding value notes:')
        dz_file = open_note(note_file)
        add_value()
        close_note(dz_file)


note_file = 'note.dz'

dz_file = open_note(note_file)
#value_to_save = add_value(1, 'Hello')
# save_value(value_to_save)
# print(value_to_save)

menu()
ask()


# with open("file.pickle", "rb+") as pickle_file:
#     data = pickle.load(pickle_file)
#     list = [1, 2, 3]
#     pickle.dump(list, pickle_file)
#     print(data)
#     print(type(data))


