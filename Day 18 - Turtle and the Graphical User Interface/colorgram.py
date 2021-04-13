# Extract colors from image and create list of tuples
# #############################

import colorgram

color_count = 8

rgb_colors = []

colors = colorgram.extract(
    "Day 18 - Turtle and the Graphical User Interface/spots.jpg", color_count
)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color_tuple = (r, g, b)
    rgb_colors.append(new_color_tuple)

print(rgb_colors)

Extracted colours minus the white
(54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171), (143, 180, 206)]
