import numpy as np


def formula_terrain(x, y):
    z = 30 - \
        3 * (np.sin(0.1 * x + 0.1 * y) + np.cos(0.1 * x - 0.1 * y)) - \
        3 * np.exp(0.05 * (0.1 * x) ** 2 + 0.03 * (0.1 * y) ** 2)
    return z


if __name__ == '__main__':
    x = np.linspace(-50, 50, 101)
    y = np.linspace(-50, 50, 101)
    x, y = np.meshgrid(x, y)

    z = formula_terrain(x, y)

    terrain = np.stack([x, y, z])

    np.save('terrain.npy', terrain)
