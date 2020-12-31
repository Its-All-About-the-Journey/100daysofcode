import os


root_path = './source_code'
directory_prefix = 'day'
days = 100

readme_filename = "README.md"

readme_contents = '''
# DAY {}

# Description

# Environment
OS:

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
    # Create directory if does not exist
    if not os.path.isdir(dir):
        os.mkdir(directory)

def create_file(filename, content):

    if not os.path.isfile(filename):
        mode = 'w+' # Non existing file
    else:
        mode = 'w' # Exists
    
    with open(filename, mode) as file:
        file.write(content)


def build():
    # Create root path if does not exist
    create_directory(root_path)

    for day in range(days):
        # Create directory
        directory = f'{root_path}/{directory_prefix}{day}'       
        create_directory(directory)
        
        # Create README.md file
        filename = f'{directory}/{readme_filename}'
        create_file(filename, readme_contents.format(day))   

if __name__ == '__main__':
    build()