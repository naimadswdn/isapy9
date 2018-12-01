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
        count_signs = len(whole_file)

        for i in alphabet:
            count = whole_file.count(i)
            print(f'{i}: {count}')

        numbers = list(range(0, 10))
        for i in numbers:
            count = whole_file.count(str(i))
            print(f'{i}: {count}')

        count_numbers = sum(number.isdigit() for number in whole_file)

        words_number = len(whole_file.split())
        print(f'Number of words in document: {words_number}.')

        # sentences_number = whole_file.count('. ')
        sentences_split = re.split(r'[.!?]+', whole_file)
        sentences_number = len(sentences_split)
        print(f'Number of sentences in document: {sentences_number}.')

    with open(r'C:\Users\Damian\Documents\isapy9\isapy9-Damian\dzien_5\dane.txt', "r+") as data_file:
        lines = data_file.readlines()

    opens_count = lines[1]
    opens_count = int(opens_count)
    opens_count += 1
    lines[1] = str(opens_count) + '\n'

    signs_count = lines[3]
    signs_count = int(signs_count)
    signs_count += int(count_signs)
    # print(signs_count)
    lines[3] = str(signs_count) + '\n'

    words_count = lines[5]
    words_count = int(words_count)
    words_count += words_number
    # print(words_count)
    lines[5] = str(words_count) + '\n'

    sentences_count = lines[7]
    sentences_count = int (sentences_count)
    sentences_count += sentences_number
    # print(sentences_count)
    lines[7] = str(sentences_count) + '\n'

    numbers_count = lines[9]
    numbers_count = int(numbers_count)
    numbers_count += count_numbers
    # print(numbers_count)
    lines[9] = str(numbers_count) + '\n'

    with open(r'C:\Users\Damian\Documents\isapy9\isapy9-Damian\dzien_5\dane.txt', 'w') as data_file_to_write:
        data_file_to_write.writelines(lines)


def main():
    text_stat_creator()


if __name__ == "__main__":
    main()
