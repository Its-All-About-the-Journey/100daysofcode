fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")

    except IndexError:
        print("Fruit pie")
    

make_pie(4)