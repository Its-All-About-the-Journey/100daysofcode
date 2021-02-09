
# DAY 30

Enhanced Password Manager

# Description

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

Core
Pyperclip

# How to run script
Call the script.

Enter a website you believe you've saved a password for, and press search.
Password will be copied to your clipboard for 30 seconds if it's found.

Enter websites, emails, and passwords for those you know, and press add.
If you can't think of a secure password, press generate password.
The password will be copied to your clipboard for 30 seconds to help you paste it in.

# Sample output
![Sample of App](https://raw.githubusercontent.com/Its-All-About-the-Journey/100daysofcode/hypermanganate/source_code/hypermanganate/day030/app.png)

I did not have search appear in a popup.
I don't see that being particularly useful, and you can have it loaded so you can click the button to generate a new password if you want.

She also loaded the file on every click for .... no reason?

# Other Excercises
## Fruit Selector

She used an else block on the print statement but I don't know why there was any need to bother.

```
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):

    try:
        fruit = fruits[index]
        print(fruit + " pie")

    except IndexError:
        print("Fruit PIe")


make_pie(4)
```

## Facebook Like Examiner
```
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)
```
