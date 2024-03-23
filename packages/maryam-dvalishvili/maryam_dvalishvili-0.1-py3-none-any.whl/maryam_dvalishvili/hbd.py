def hbd():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.offsetbox import AnchoredText
    def draw_star(ax, x, y, size, color='yellow'):
        ax.scatter(x, y, s=size, c=color, marker='*', zorder=10)  # Set higher z-order

    # Plot the heart shape and the star
    x = np.linspace(-2, 2, 200)
    y = np.linspace(-2.0, 2.0, 200)
    X, Y = np.meshgrid(x, y)
    eq = np.power(X, 2) + np.power(Y - np.cbrt(np.power(X, 2)), 2) - 1
    levels = [-1 + i * 0.001 for i in range(0, 1000)]

    fig, ax = plt.subplots()

    # Plot the heart with partial transparency
    ax.contour(X, Y, eq, levels, colors="r", alpha=0.5)

    # Draw the star at the center of the heart
    heart_center_x = 0
    heart_center_y = np.cbrt(np.power(heart_center_x, 2)) + 0.4
    draw_star(ax, heart_center_x, heart_center_y, 500, color='yellow')
    ax.arrow(-1, -0.5, 2.25, 2, width=0.05)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.axis('off')  # Turn off the axis frame
    ax.set_title('Cheers to the most radiant star in the galaxy on her special day! <3 ')
    ax.grid(False)

    plt.show()

    # Print the Happy Birthday message
    print("Happy Birthday!")