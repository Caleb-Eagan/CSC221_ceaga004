import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making walks, as long as the program is active.
#while True:
    # Make a random walk.
rw = RandomWalk(5000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1, c=(0.5, 0.5, 0.5))
ax.set_aspect('equal')

# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
#plt.savefig('15-3 molecular_motion.png', bbox_inches='tight')

#keep_running = input("Make another walk? (y/n): ")
#if keep_running == 'n':
#    break