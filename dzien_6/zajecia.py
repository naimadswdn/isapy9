import csv
import pickle #module that allow to save objects in Python, it is saved in BINARY FORMAT


# with open ("ksiazki.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=';')
#     for i in csv_reader:
#         #print(i)
#         #print(' '.join([format(element, '<10') for element in csv_reader]))
#         print(' '.join(i))


with open("file.pickle", "rb+") as pickle_file:
    data = pickle.load(pickle_file)
    list = [1, 2, 3]
    pickle.dump(list, pickle_file)
    print(data)
    print(type(data))

