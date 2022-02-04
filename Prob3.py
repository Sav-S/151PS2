#######################################
# Name:Savanna Starks
# Collaborators:
# Estimated time spent (hr):1
#######################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. You can change these if you want. They are in number of pixels.
WIDTH = 450
HEIGHT = 600

# Creating the window
gw = GWindow(WIDTH, HEIGHT)

# And you can take it from here! I'm excited to see what you create
gw = GWindow(450,500)
"""the sky"""
#upper sky
upper_sky = GRect(0, 0, 450, 500)
upper_sky.set_color("navy")
upper_sky.set_filled(True)
gw.add(upper_sky)
#middle sky
middle_sky = GRect(0, 150, 450, 300)
middle_sky.set_color("darkblue")
middle_sky.set_filled(True)
gw.add(middle_sky)
#lower sky section
lower_sky = GRect(0, 250, 450, 300)
lower_sky.set_color("mediumblue")
lower_sky.set_filled(True)
gw.add(lower_sky)
#bottom sky section
bottom_sky = GRect(0, 350, 450, 300)
bottom_sky.set_color("blue")
bottom_sky.set_filled(True)
gw.add(bottom_sky)

"""the stars
#base formula
base_star = GOval(10, 15, 3, 3)
base_star.set_color("lightcyan")
base_star.set_filled(True)xs
gw.add(base_star)"""

"""the moon"""
#base yellow circle
yellow_circle = GOval(325, 20, 100, 100)
yellow_circle.set_color("gold")
yellow_circle.set_filled(True)
gw.add(yellow_circle)
#to make the cresent
blue_circle = GOval(275, 20, 100, 100)
blue_circle.set_color("navy")
blue_circle.set_filled(True)
gw.add(blue_circle)
    
"""the sidewalk"""
#base layer sidewalk
sidewalk = GRect(0, 428, 450, 500)
sidewalk.set_color("Slategray")
sidewalk.set_filled(True)
gw.add(sidewalk)
#sidewalk lines
left_most_sidewalk_line = GLine(100, 428, 100, 500)
gw.add(left_most_sidewalk_line)
second_left_most_sidewalk_line = GLine(200, 428, 200, 500)
gw.add(second_left_most_sidewalk_line)
middle_sidewalk_line = GLine(300, 428, 300, 500)
gw.add(middle_sidewalk_line)
right_sidewalk_line = GLine(400, 428, 400, 500)
gw.add(right_sidewalk_line)

"""the skateboard"""
#left skateboard wheel
left_wheel = GOval(260, 405, 25,25)
left_wheel.set_color("Black")
left_wheel.set_filled(True)
gw.add(left_wheel)

#right skateboard wheel
right_wheel = GOval(390, 405, 25,25)
right_wheel.set_color("Black")
right_wheel.set_filled(True)
gw.add(right_wheel)

#skateboard body
skateboard = GRect(250, 400, 180, 10)
skateboard.set_color("Darkred")
skateboard.set_filled (True)
gw.add(skateboard)

"""the streelamp"""
#the pole
pole = GRect(50, 150, 10, 278)
pole.set_color("color.darkgray")
pole.set_filled(True)
gw.add(pole)
#the light bulb
bulb = GOval(60, 160, 50, 20)
bulb.set_color("color.orange")
bulb.set_filled(True)
gw.add(bulb)
#the lamp shade
lamp_shade = GRect(50, 150, 60, 25)
lamp_shade.set_color("color.darkgray")
lamp_shade.set_filled(True)
gw.add(lamp_shade)



