import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(start_point, end_point, amplitude=1, frequency=1, num_points=100):
    x = np.linspace(start_point[0], end_point[0], num_points)
    y_baseline = np.linspace(start_point[1], end_point[1], num_points)
    y = amplitude * np.sin(2 * np.pi * frequency * (x - start_point[0]) / (end_point[0] - start_point[0])) + y_baseline
    return x, y

# Define the start and end points of the straight line
start_point = (0, 0)
end_point = (5, 10)

# Generate the sine wave oscillating about the straight line
amplitude = 2  # Adjust the amplitude as needed
frequency = 1  # Adjust the frequency as needed
x, y = generate_sine_wave(start_point, end_point, amplitude, frequency)

# Plot the sine wave
plt.plot(x, y)
plt.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], linestyle='--', color='gray')  # Plot the straight line
plt.scatter([start_point[0], end_point[0]], [start_point[1], end_point[1]], color='red')  # Mark start and end points
plt.title('Sine Wave Oscillating About the Straight Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(0,10)
plt.grid(True)
plt.show()
