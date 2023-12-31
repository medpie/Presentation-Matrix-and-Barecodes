import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import Slider
from matplotlib.widgets import Line2D
from ipywidgets import interact

lines = []

def update_radius(val):
    #global current_radius
    # Update the radius of all balls
    for ball in balls:
        ball.set_radius(radius_slider.val)
    
    for line in lines:
        line.remove()
    lines.clear()
    
    for i in range(num_balls - 1):
        for j in range(i+1, num_balls):
            distance = np.linalg.norm(np.array(balls[i].center) - np.array(balls[j].center))
            if 0.5*distance < radius_slider.val:
                line = draw_line(ax, balls[i].center, balls[j].center)
                lines.append(line)
    #current_radius = radius_slider.val
    # Redraw the plot
    plt.draw()

def draw_line(ax,center1, center2):
    line = Line2D([center1[0], center2[0]], [center1[1], center2[1]], color='blue')
    ax.add_line(line)
    return line

# Create a figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust the bottom margin to make room for the slider

# Number of balls
num_balls = 10

# Initial radius value
initial_radius = 0.001
x = np.array([np.random.rand(1) for _ in range(num_balls)])
y = np.array([np.random.rand(1) for _ in range(num_balls)])
# Create a list to store the Circle patches (balls)
balls = [Circle((x[_], y[_]), initial_radius, color='green', alpha=0.3) for _ in range(num_balls)]
plt.scatter(x,y, color='black' )
# Add all balls to the axis using add_patch
for ball in balls:
    ax.add_patch(ball)

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Create a slider axes
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')

# Create a slider
radius_slider = Slider(ax_slider, 'Radius', 0.05, 0.5, valinit=initial_radius)

# Attach the update_radius function to the slider
radius_slider.on_changed(update_radius)

# Show the plot
plt.show()