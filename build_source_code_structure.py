import os
import shutil

username = 'CHANGEME'  # <----------------------CHANGE THIS

root_path = './source_code'
directory_prefix = 'day'
days = 100
padding = '03' # Max 3 digits or padd with 0

readme_filename = "README.md"

# The readme_contents will be used a template and the 
# script will create a README.md for all day directory.  
# Change sections that will be repeated for each day
# such as OS, Python ver.
# You can also additional section of your choosing.

readme_contents = '''
# DAY {}

# Description

# Environment
OS: Yes

Python version:

# Dependencies

# How to run script
```
enter instructions here
```

# Sample output
```
paste output here
```
'''


def create_directory(dir):
    # Create directory if one does not exist
    if not os.path.isdir(dir):
        os.mkdir(dir)

def create_file(filename, content, overwrite=False):
    with open(filename, 'w') as file:
        file.write(content)


def build(overwrite_readme):

    # Create root path if does not exist
    create_directory(root_path)

    for day in range(1, days+1): # Start on 1
        # Create directory
        padded_day = f'{day:{padding}}'
        directory = f'{root_path}/{directory_prefix}{padded_day}'       
        create_directory(directory)
        
        # Update 1 - Adding username directory so there is no conflict when
        # each user merges thier branch to the main branch
        create_directory(f'{directory}/{username}')

        # Move all files in the day directory to the new username directory
        file_list = os.listdir(directory)

        for file in file_list:
            src = f'{directory}/{file}'
            dest = f'{directory}/{username}'
            shutil.move(src, dest, copy_function=shutil.copytree)

        # Create README.md file
        filename = f'{directory}/{username}/{readme_filename}'
        create_file(filename, readme_contents.format(day), overwrite_readme)

if __name__ == '__main__':
    
    # Exit if default username has not been changed
    if username == 'CHANGEME':
        print(f'You forgot to change the username variable in the python script.')
        print(f'It is currently set to {username}')
    
    else:
        print('*'*80)
        print(f'WARNING: It will overwrite all {readme_filename} file inside {root_path} directory')
        print('*'*80)
        print('Do you want overwrite each README.md?')
        print("Enter yes to overwrite or press enter to keep existing")
        overwrite_readme = input()
        print()

        if overwrite_readme == 'yes':
            print(f'Overwriting any existing README.md in the {root_path}')
            build(True)
        else:
            print('Keeping any existing README.md.')
            build(False)
        
        print('*'*80)