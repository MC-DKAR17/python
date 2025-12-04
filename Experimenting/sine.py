import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Setup the figure and axes
fig, ax = plt.subplots()
# Set limits to make sure the oscillation fits and is centered
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.1, 1.1)
ax.set_title("Oscillating Sine Wave")
ax.set_xlabel("Position (x)")
ax.set_ylabel("Amplitude (y)")

# Initialize the line plot (line,) is needed for blitting
line, = ax.plot([], [], lw=2)

# Data for the wave
x = np.linspace(0, 2 * np.pi, 100)

# 2. Initialization function (returns the line object)
def init():
    line.set_data([], [])
    return line,

# 3. Animation function (updates the line object for each frame)
def animate(frame):
    # Create an oscillating wave by shifting the phase based on the frame number
    # frame / 10.0 controls the speed of the oscillation
    y = np.sin(x + frame / 10.0)
    line.set_data(x, y)
    return line,

# 4. Create the animation
# frames=100 sets the number of frames
# interval=50 means 50ms per frame (20 frames per second)
ani = FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=100,
    interval=50,
    blit=True
)

# 5. Save the animation as a GIF
ani.save('oscillating_wave.gif', writer='pillow', fps=20, dpi=100)

# The figure is closed to prevent it from displaying during execution
plt.close(fig)