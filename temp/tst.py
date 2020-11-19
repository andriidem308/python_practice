import numpy as np
import matplotlib.pyplot as plt


def f1(x): return -x*x
def f2(x, a, b): return a*x + b


if __name__ == "__main__":
    a = float(input())
    b = float(input())

    x0 = np.linspace(-5.0, 5.0)
    xs = np.linspace((-a-(a*a - 4*b)**(1/2))/2, (-a+(a*a - 4*b)**(1/2))/2)
    y1 = f1(x0)
    y2 = f2(x0, a, b)

    s = np.trapz(xs, f2(xs, a, b)-f1(xs))
    print(s)

    plt.plot(x0, y1)
    plt.plot(x0, y2)
    plt.show()
