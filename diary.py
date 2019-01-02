import pickle
import smtplib
import pprint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dzien_2.check_if_good import check_if_good
from collections import OrderedDict

diary_file = 'file'


class Diary(object):
    def __init__(self):
        self.open_diary = open(diary_file, 'rb+')

    def __str__(self):
        return 'Diary powered by Python code.\n' \
               'It allows user to read, add, remove or search entries in whole diary content. '

    def __len__(self):
        return len(self.read_file())

    def add_entry(self):
        """
        Function for adding new entries into the diary.
        It takes two inputs from users: date and content. After that it save them into diary file using binary mode.
        :return:
        """
        date = input('Please provide data with format DD-MM-YYYY: ')
        content = input('Provide content of diary entry: ')
        #new_entry = {"date": date, "content": content}
        new_entry = OrderedDict()
        new_entry['date'] = date
        new_entry['content'] = content

        old_entries = self.read_file()
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

    def menu(self):
        """
        Simple function to print menu for user interaction.
        :return:
        """
        print("My diary v1.0\n"
              "1. Show all my entries.\n"
              "2. Add new entry.\n"
              "3. Remove entry.\n"
              "4. Search in diary...\n"
              "5. Exit")

    def remove_entry(self):
        """
        Function responsible for removing entries from diary.
        :return:
        """
        all_entries = self.read_file()
        number_of_all_entries = len(all_entries)
        print(f'Number of all entries in diary is equal to {number_of_all_entries}.')
        entry_number_to_remove = int(input('Provide number of entry to remove: '))

        if entry_number_to_remove <= number_of_all_entries and entry_number_to_remove > 0:
            index_to_remove = entry_number_to_remove -1
            del(all_entries[index_to_remove])
            self.open_diary.seek(0)

            topic = 'Someone remove entry from diary'
            content = f'Entry with index number {index_to_remove} has been removed\n' \
                      f'For user it was entry number {entry_number_to_remove}.'

            self.send_email(topic,content)
            pickle.dump(all_entries, self.open_diary)
            print('Entry has been removed successfully.')
        else:
            print('There is no such entry in the diary.')
        self.open_diary.close()

    def send_email(self,topic, content):
        """
        Function that is sending an email.
        :param topic: it is a topic of an email
        :param content: it is a content of the message
        :return:
        """
        mail = MIMEMultipart()
        mail["Subject"] = topic
        mail["To"] = 'naimadswdn@gmail.com'
        mail["From"] = 'isapy@int.pl'

        body = MIMEText(content)
        mail.attach(body)

        server = smtplib.SMTP('poczta.int.pl')
        server.login('isapy@int.pl', 'isapython;')
        server.send_message(mail)
        server.quit()

        print('Email has been send successfully.')

    def search(self):
        """
        Function responsible for searching for some keyword in the diary content.
        It search across whole diary entries.
        :return:
        """
        all_entries = self.read_file()
        keyword = input('Please type keyword to search: ')

        number_of_results = 0
        for index, entry in enumerate(all_entries):
            if keyword in entry['content']:
                number_of_results += 1
                print(entry['content'])
                print(f'\nKeyword found on {index} index, which means {index +1} entry in diary.')

        if number_of_results == 0:
            print('Keyword not found in the diary.')
        else:
            print(f'Number of results: {number_of_results}')
        self.open_diary.close()


diary = Diary()


def control():
    """
    Function to allow user interact with diary.
    :return:
    """
    diary.menu()
    decision = None
    decision = check_if_good(decision, int, 'What is your choice? ')
    decision = int(decision)

    if decision == 1:
        print('Here are your diary entries:')
        all_entries = diary.read_file()
        pprint.pprint(all_entries)
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





