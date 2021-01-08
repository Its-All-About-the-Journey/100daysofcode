#Write your code below this line 👇

def paint_calc(height: float, width: float, cover: float) -> None:
    result = height * width / cover
    
    # Round fraction up -- After watching solution, math.ceil(v)
    if result % 1:
        result = int(result)
        result += 1
    else:
        result = int(result)

    print(result)


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)