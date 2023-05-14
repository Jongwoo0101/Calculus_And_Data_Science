import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return x ** 2 - 2 * x  # x^2 - 2x


def differential(f, x):
    h = 0.001
    return (f(x + h) - f(x)) / h


x = np.arange(-100, 100, 1)  # -100 부터 100까지 1씩늘어나는 숫자
plt.plot(x, function(x))
plt.show()

diff = differential(function, 75)  # 75일 때 기울기
print(diff)
