import colorgram


max_colors = 30

img_colors = colorgram.extract("image.jpg", max_colors)

# Build list of tuples
colors = [ tuple(img_colors[i].rgb) for i in range( len(img_colors) ) ]

print(colors)