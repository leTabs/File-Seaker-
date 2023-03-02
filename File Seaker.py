from pathlib import Path

def file_direcory():
    count = 0
    file_name = input("Enter the file's name:")
    path = Path.home()/'desktop'
    print('*'*80)
    print(f'File locations including "{file_name}":')
    print('-'*80)
    for i in path.glob('**/*'):
        if file_name in str(i):
            print(f'{count}) {i}')
            count+=1
    print('-'*30,'Proccess terminated', '-'*29)
file_direcory()
