def text_stat_creator():
    """Program to collect statistics of text tile. It allow to collect following information:
    - number of each alphabet sign in text file,
    - number of each numeric sign (0-9) in text file,
    - number of words in text file,
    - number of sentences in text file.
    Program saves usage statistics in dane.txt file - it can be found in the same directory as Python file.
    """
    import string
    import re
    import pickle
#
#     try:
#         open('dane.txt', 'r')
#     except:
#         stats_pattern = """Program was executed below number of times:
# 0
# Number of analysed signs:
# 0
# Number of found words:
# 0
# Number of found sentences:
# 0
# Number of analysed numbers:
# 0"""
#         with open('dane.txt', 'w') as stats_pattern_to_write:
#             stats_pattern_to_write.writelines(stats_pattern)

    while True:
        file_directory = input('Please provide absolute directory of file that you want to statistics see: '
                               'If file is located in program folder then you can type only file name. ')
        try:
            fh = open(file_directory, 'r')
            break
        except FileNotFoundError:
            print('File do not exist!')
            continue

    with open(file_directory, 'r') as file:
        whole_file = file.read()
        whole_file = whole_file.casefold()

        alphabet = list(string.ascii_lowercase)
        #count_signs = len(whole_file)

        list_to_write = {}

        for i in alphabet:
            count = whole_file.count(i)
            #print(f'{i}: {count}')
            list_to_write[i] = count



        numbers = list(range(0, 10))
        for i in numbers:
            count = whole_file.count(str(i))
            #print(f'{i}: {count}')
            list_to_write[i] = count

        #print(list_to_write)

        words_number = len(whole_file.split())
        #print(f'Number of words in document: {words_number}.')
        list_to_write['words_number'] = words_number

        #sentences_number = whole_file.count('. ')
        sentences_split = re.split(r'[.!?]+', whole_file)
        sentences_number = len(sentences_split)
        list_to_write['Sentences_numbers'] = sentences_number

        print(list_to_write)

    with open('dane.txt', "rb+") as pickle_file:
        pickle_content = pickle.load(pickle_file)
        pickle.dump(list_to_write, pickle_file)
        #print(pickle_content)
        for i, j in pickle_content.items():
            print(f'{i}: {j}')
        print(type(pickle_content))



        #count_numbers = sum(number.isdigit() for number in whole_file)

        # words_number = len(whole_file.split())
        # print(f'Number of words in document: {words_number}.')
        #
        # # sentences_number = whole_file.count('. ')
        # sentences_split = re.split(r'[.!?]+', whole_file)
        # sentences_number = len(sentences_split)
        # print(f'Number of sentences in document: {sentences_number}.')



def main():
    text_stat_creator()


if __name__ == "__main__":
    main()
