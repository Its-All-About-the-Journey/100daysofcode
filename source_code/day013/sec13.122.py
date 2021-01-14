# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, len(dice_imgs) - 1) 
print(dice_imgs[dice_num])
# Randint returns a value from 1-6. 6 causes index out of range.  
# Fix: Change range to 0,5 on line 4 or better: 0,len(dice_num)-1

# STARTING CODE - UNTOUCHED
############DEBUGGING#####################

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])