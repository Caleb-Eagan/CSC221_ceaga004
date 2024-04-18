import matplotlib.pyplot as plt
import random

from random_walk import RandomWalk

colors = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

# Keep making walks, as long as the program is active.
while True:
    # Make a random walk.
    random_walks = []

    for i in range(100):
        rw = RandomWalk(5_000)
        random_walks.append(rw)

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)

    for rw in random_walks:
        rw.fill_walk()
        point_numbers = range(rw.num_points)
        color = colors[random.randint(0,len(colors)-1)]
        ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=color, edgecolors='none', s=1)
        ax.set_aspect('equal')

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break