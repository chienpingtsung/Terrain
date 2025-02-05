import numpy as np


def terrain_formula(x, y):
    z = 30 - \
        3 * (np.sin(0.1 * x + 0.1 * y) + np.cos(0.1 * x - 0.1 * y)) - \
        3 * np.exp(0.05 * (0.1 * x) ** 2 + 0.03 * (0.1 * y) ** 2)
    return z


if __name__ == '__main__':
    x = np.linspace(-50, 50)
    y = np.linspace(-50, 50)
    x, y = np.meshgrid(x, y)

    z = terrain_formula(x, y)

    terrain = np.stack([x, y, z])

    np.save('terrain.npy', terrain)
