from helper_functions import *
from classes import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import arcade
from vars import *

#Read data
global vehicle_map
global stoplight_map
vehicle_map = dict()
stoplight_map = dict()

readStoplights(stoplight_map, "stoplight.csv")
readVehicles(vehicle_map, "trajectories-0400pm-0415pm_editted.csv")

# fig, ax = plt.subplots()
# line, = ax.plot(vehicle_map[2].Global_Y, vehicle_map[2].Global_X)
# ani = animation.FuncAnimation(
#     fig, animate, init_func=init, interval=2, blit=True, save_count=50)
#
# plt.show()

time = 0
#moving rectangle animation

def on_draw(delta_time):
    global time
    # print(on_draw.center_x)
    """
    Use this function to draw everything to the screen.
    """

    # Start the render. This must happen before any drawing
    # commands. We do NOT need a stop render command.
    arcade.start_render()

    #here it should be len(on_draw.center_x) instead of 10 for all vehicles
    for i in range(10):
        arcade.draw_rectangle_filled(on_draw.center_x[i], on_draw.center_y[i],
                                     RECT_WIDTH, RECT_HEIGHT,
                                     arcade.color.ALIZARIN_CRIMSON)


    # Modify rectangles position based on the delta
    # vector. (Delta means change. You can also think
    # of this as our speed and direction.)

    for i in range(len(vehicle_map)):
        if time < len(vehicle_map[i].Global_X):
            on_draw.center_x[i] = Xfac * (vehicle_map[i].Global_X[time] - GLOBAL_X_MIN)
            on_draw.center_y[i] = Yfac * (vehicle_map[i].Global_Y[time] - GLOBAL_Y_MIN)
    # on_draw.center_x = Xfac * (vehicle_map[2].Global_X[time] - GLOBAL_X_MIN)
    # on_draw.center_y = Yfac * (vehicle_map[2].Global_Y[time] - GLOBAL_Y_MIN)
    # print(on_draw.center_x[0])
    time += 1

    # Figure out if we hit the edge and need to reverse.
    # if on_draw.center_x < RECT_WIDTH // 2 \
    #         or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:
    #     on_draw.delta_x *= -1
    # if on_draw.center_y < RECT_HEIGHT // 2 \
    #         or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // 2:
    #     on_draw.delta_y *= -1

# Below are function-specific variables. Before we use them
# in our function, we need to give them initial values. Then
# the values will persist between function calls.
#
# In other languages, we'd declare the variables as 'static' inside the
# function to get that same functionality.
#
# Later on, we'll use 'classes' to track position and velocity for multiple
# objects.

on_draw.center_x = []      # Initial x position
on_draw.center_y = []       # Initial y position

for i in range(len(vehicle_map)):
    on_draw.center_x.append(0.0)
    on_draw.center_y.append(0.0)

print(len(vehicle_map[0].Global_X))


# on_draw.delta_x = 115  # Initial change in x
# on_draw.delta_y = 130  # Initial change in y


def main():
    # Open up our window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1 / 80)


    # Run the program
    arcade.run()


if __name__ == "__main__":
    main()
