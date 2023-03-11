from pathlib import Path
import os, time, sys, csv
# importing the required modules

def options():
    # this function prompts the user to choose the operation that they want
    # it also works after the operation is finished, in the case the user
    # wants to select again an operation
    while True:
        print('''I am searching for:

1) The location of a certain file.
2) The files of a specific type.
-----------------------------------''')
        option = input('Enter:')
        if option == '1':
            file_directory() 
            # calling the function of the choosen operation
            print('#'*80)
            if input('View options (y/n):') == 'y':
                continue
                # the user reopens the options
            else:
                print('#'*80)
                print('Have a great day...')
                time.sleep(5)
                sys.exit()
                break
                # the user exits the program
        elif option == '2':
            # an analogy of the first if statement
            files_of_type()
            print('#'*80)
            if input('View options (y/n):') == 'y':
                continue
            else:
                print('#'*80)
                print('Have a great day...')
                time.sleep(5)
                sys.exit()
                break
        else:
            print('Please choose one of the options')
            continue

def directory():
    global path
    print('''Choose a directory category:

1) Desktop
2) Home (the whole computer)
3) Type a more specific directory location:
    ''')
    while  True:
        directory = input('Enter:')
        # the user chooses a directory or creates his own
        if directory == '1':
            path = Path.home()/'desktop'
            break
        if directory == '2':
            path = Path.home()
            break
        if directory == '3':
            print('-'*20)
            specific_dir =  input('C:\\Users\\user:')
            path = Path.home() / specific_dir
            break
        # the directory is registered as the user's choice
        else:
            print('''
Please choose one of the three options''')
            continue
        # if the user chooses something outside the given options
        # the program asks for a valid directory path choice 
        
def file_directory(): # the first operation

    directory()
    # calling the directory() function to assing the file path
    
    count = 0 # will be used as a count index for the files/direcories returned 
    print('*'*80)
    file_name = input("Enter the file's name:")
    # asking for the file's nameto, search with
    print('*'*80)
    print(f'File locations of files including "{file_name}":')
    print('-'*80)
    
    for location in path.glob('**/*'):
        # lookinng inside the given dir and it's subdirectories
        # and searching each possible files that includes the given name
        if file_name in str(os.path.basename(location)):
            print(f'{count}) {location}')
            # if it matches the stated criteria
            # it gets printed, with an index
            count+=1
            # incrementing the index to be ready for the next possible match
    print('='*80)
    print('='*80)
    print('-'*30,'PROCCESS TERMINATED', '-'*29)
    print('='*80)
    print('='*80)

def files_of_type(): # the second operation

    directory()
    # calling the directory() function to assing the file path
    count = 0
    #  will be used as a count index for the files/direcories returned
    print('*'*80)
    file_type = input("Enter the type of the file(s):")
    # asking for the type of the file (for example: txt)
    print('*'*80)
    print(f'Files of the ".{file_type}" type on {path}:')
    print('-'*80)
    for file in path.glob(f'**/*.{file_type}'):
        # lookinng inside the given dir and it's subdirectories
        # and searching each possible files of the requested type
        print(f'{count}) {os.path.basename(file)}')
        # if it matches the stated criteria
        # it gets printed, with an index
        count += 1
        # incrementing the index to be ready for the next possible match
    print('='*80)
    print('='*80)
    print('-'*30,'PROCCESS TERMINATED', '-'*29)
    print('='*80)
    print('='*80)

options()
