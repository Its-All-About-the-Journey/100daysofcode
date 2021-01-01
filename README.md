# 100daysofcode
A group of us will be following https://www.udemy.com/course/100-days-of-code and meet up once a week to have open discussions.  Day/Time TBD.

If you want to join us visit: https://artofneteng.com/iaatj and let us know in the #100daysofcode channel.

# First Time Setup
```
c:\>git clone https://github.com/Its-All-About-the-Journey/100daysofcode.git
c:\>cd 100daysofcode
c:\100daysofcode>git checkout -b avholloway
c:\100daysofcode>git push --set-upstream origin avholloway
```

# Day to Day Setup
Enter the day folder:
```
c:\>cd 100daysofcode\source_code\day001
```
Setup the Python virtual environment for the day:
```
c:\100daysofcode\source_code\day001>python -m venv venv
c:\100daysofcode\source_code\day001>.\venv\Scripts\activate
(venv) c:\100daysofcode\source_code\day001>
```
Install the required Python packages:
```
(venv) c:\100daysofcode\source_code\day001>pip install rich
```
Open VS Code and start coding:
```
(venv) c:\100daysofcode\source_code\day001>code
```
Commit often:
```
(venv) c:\100daysofcode\source_code\day001>git add .
(venv) c:\100daysofcode\source_code\day001>git commit -m "i made something work!"
```
Freeze your pip packages into the requirements file:
```
(venv) c:\100daysofcode\source_code\day001>pip freeze > requirements.txt
```
Deactivate the Python virtual environment:
```
(venv) c:\100daysofcode\source_code\day001>deactivate
c:\100daysofcode\source_code\day001>
```
Push to github:
```
git push
```