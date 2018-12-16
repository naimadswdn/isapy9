import sys
import os
import send2trash

path = sys.path
print('------------')
for i in path:
    print(i) #it shows all the pathes were Python is looking for modules
print('------------')
print(os.getcwd())

send2trash.send2trash('blabla')



