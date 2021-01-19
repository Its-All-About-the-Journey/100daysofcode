# 🚨 Reeborg's World Hurdle 3 👇

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# 🚨 Reeborg's World Hurdle 3, Negated Conditions Example #1 👇
# while not at_goal():
#     if not wall_in_front():
#         move()
#     elif not front_is_clear():
#         jump()

# 🚨 Reeborg's World Hurdle 3, Non-Negated Conditions Example #1 👇
# while not at_goal():
#     if wall_in_front():
#         jump()
#     elif front_is_clear():
#         move()

# 🚨 Reeborg's World Hurdle 3, Non-Negated Conditions Example #2 👇
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()