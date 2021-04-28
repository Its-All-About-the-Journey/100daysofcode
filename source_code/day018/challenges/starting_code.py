import colorgram

colors = colorgram.extract('dots.png', 30)

rgb_colors = []

for extraction in range(0,len(colors)):
    current_color = colors[extraction]
    rgb = current_color.rgb
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    rgb_tup = (red, green, blue)
    rgb_colors.append(rgb_tup)
