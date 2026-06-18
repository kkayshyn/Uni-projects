import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- SIATKA ---
s = 200  #rozdzielczość (im więcej, tym ładniej i wolniej)
x = np.linspace(-2, 2, s)
y = np.linspace(-2, 2, s)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

def julia(z, c, max_iter=300):
    """
    Oblicza zbiór Julii dla danego parametru c
    """
    zz = z.copy()
    output = np.zeros(z.shape, dtype=int)
    mask = np.ones(z.shape, dtype=bool)

    for i in range(max_iter):
        zz[mask] = zz[mask] ** 2 + c
        escaped = np.abs(zz) > 2
        output[escaped & mask] = i
        mask &= ~escaped

    return np.clip(output, 0, 255)

c = np.cos(0) + 1j * np.sin(0)

def evolve(frame):
    a, b, d = 3, 2, np.pi / 2
    phi = 4 * np.pi * frame / 720
    re = np.sin(a * phi + d)
    im = np.sin(b * phi)
    c = re + 1j * im
    matrix.set_data(julia(Z, c))
    return [matrix]

fig, ax = plt.subplots()
matrix = ax.matshow(julia(Z, c), cmap='magma')
ani = animation.FuncAnimation(fig, evolve, frames=720, interval=20)
plt.show()