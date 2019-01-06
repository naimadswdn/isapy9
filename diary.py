import pickle
from dzien_2.check_if_good import check_if_good
import datetime
from send_email import send_email

diary_file = 'file'


class Diary(object):
    def __init__(self):
        self.open_diary = open(diary_file, 'rb+')
        self.all_entries = self.read_file()
        self.number_of_all_entries = len(self.all_entries)

    def __str__(self):
        return 'Diary powered by Python code.\n' \
               'It allows user to read, add, remove or search entries in whole diary content. '

    def __len__(self):
        return len(self.all_entries)

    @staticmethod
    def date_validation(date):
        try:
            datetime.datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            print('Incorrect data format, accepted: DD-MM-YYYY.\n'
                  'Please try once again.')
            exit()

    def add_entry(self):
        """
        Function for adding new entries into the diary.
        It takes two inputs from users: date and content. After that it save them into diary file using binary mode.
        :return:
        """
        date = input('Please provide data with format DD-MM-YYYY: ')
        self.date_validation(date)
        content = input('Provide content of diary entry: ')
        new_entry = {"date": date, "content": content}

        old_entries = self.all_entries
        new_entries = old_entries

        try:
            new_entries.append(new_entry)
        except:
            print('There was no entry in the diary so far. Adding first one.')
            new_entries = []
            new_entries.append(new_entry)

        self.open_diary.seek(0)
        pickle.dump(new_entries, self.open_diary)
        self.open_diary.close()
        print('Diary populated correctly.')

    def read_file(self):
        """
        Function to read data in the diary file.
        Entries are saved into the diary file using binary mode and to read them, function is using pickle module.
        :return:
        """
        try:
            data = pickle.load(self.open_diary)
            return data
        except EOFError:
            print('Your diary is empty!')

        #self.open_diary.close()

    @staticmethod
    def menu():
        """
        Simple function to print menu for user interaction.
        :return:
        """
        print("My diary v1.0\n"
              "1. Show all my entries.\n"
              "2. Add new entry.\n"
              "3. Remove entry.\n"
              "4. Search in diary...\n"
              "5. Exit.")

    def remove_entry(self):
        """
        Function responsible for removing entries from diary.
        :return:
        """
        print(f'Number of all entries in diary is equal to {self.number_of_all_entries}.')
        entry_number_to_remove = int(input('Provide number of entry to remove: '))

        if entry_number_to_remove <= self.number_of_all_entries and entry_number_to_remove > 0:
            index_to_remove = entry_number_to_remove -1
            del(self.all_entries[index_to_remove])
            self.open_diary.seek(0)

            topic = 'Someone remove entry from diary'
            content = f'Entry with index number {index_to_remove} has been removed\n' \
                      f'For user it was entry number {entry_number_to_remove}.'

            send_email(topic,content)
            pickle.dump(self.all_entries, self.open_diary)
            print('Entry has been removed successfully.')
        else:
            print('There is no such entry in the diary.')
        self.open_diary.close()

    def search(self):
        """
        Function responsible for searching for some keyword in the diary content.
        It search across whole diary entries.
        :return:
        """
        keyword = input('Please type keyword to search: ')
        keyword = keyword.lower()
        number_of_results = 0
        # for index, entry in enumerate(self.all_entries):
        #     if keyword in entry['content']:
        #         number_of_results += 1
        #         result_content = entry['content']
        #         print(f'Result {number_of_results}: {result_content}')
        #         print(f'Keyword found on {index} index, which means {index +1} entry in diary.\n')

        for i in range(self.number_of_all_entries):
            single = SingleEntry(i)
            if keyword in single.content.lower():
                number_of_results += 1
                print(f'Result {number_of_results}: {single}')
                print(f'Keyword found on {i} index, which means {i +1} entry in diary.\n')

        if number_of_results == 0:
            print('Keyword not found in the diary.')
        else:
            print(f'Number of results: {number_of_results}')
        self.open_diary.close()


class SingleEntry(Diary):
    def __init__(self, index, author='Me'):
        super(SingleEntry, self).__init__()
        # self.date = date
        # self.content = content
        self.index = index
        self.author = author
        self.entry = self.all_entries[self.index]
        self.content = self.entry['content']
        self.date = self.entry['date']

    def __str__(self):
        # count = 0
        # count += 1
        # print(f'Entry {count}:')
        return self.date + ': ' + self.content


def control():
    """
    Function to allow user interact with diary.
    :return:
    """
    diary = Diary()
    diary.menu()
    decision = None
    decision = check_if_good(decision, int, 'What is your choice? ')
    decision = int(decision)

    if decision == 1:
        print('Here are your diary entries:')
        if diary.all_entries is None:
            pass
        else:
            count = 0
            for i in range(diary.number_of_all_entries):
                count += 1
                print(f'Entry {count}:')
                single = SingleEntry(i)
                print(single)
                # for x, y in i.items():
                #     print(x + ': ' + y)
        diary.open_diary.close()
    elif decision == 2:
        print('Adding new entry...')
        diary.add_entry()
        diary.open_diary.close()
    elif decision == 3:
        print('Procedure of removing entries started.')
        diary.remove_entry()
        diary.open_diary.close()
    elif decision == 4:
        print('Search mode on.')
        diary.search()
        diary.open_diary.close()
    elif decision == 5:
        exit()


control()


#single = SingleEntry(0)

#print(single)




