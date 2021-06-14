# 100daysofcode
A group of us will be following https://www.udemy.com/course/100-days-of-code and meet up once a week to have open discussions.  Day/Time TBD.

If you want to join us visit: https://artofneteng.com/iaatj and let us know in the #100daysofcode channel.

# Setting up environment
```
git clone https://github.com/Its-All-About-the-Journey/100daysofcode.git

cd 100daysofcode

python3 -m venv venv

source venv/bin/activate
```

Each of us will build our own branch by executing the following git command:

```
git checkout -b your_discord_name
```

You can use build_source_code_structure.py to update README.md file specific to your environment.  In particular you should edit the readme_contents variable in the script.

````markdown
readme_contents = '''
# DAY {1}

# Description
Mkutka's Attempt at #100daysofcode
Doubt i'll consistently make it, but will try to do as much as possible
# Environment
OS: Mac OSX

Python version: 3.9.0

# Dependencies

# How to run script

# Sample output
```
paste output here
```
'''
````

Afterwards, you can edit README.md specifics for the day such as description,
howto, and sample output.  It is not mandatory.  The purpose of the script is
to standarize our structure.  Improvements are welcomed.

```
python build_source_code_structure.py
```

