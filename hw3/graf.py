import matplotlib.pyplot as plt

file = open("money", "r")
dots1 = list(map(float, file.readline().split()))
dots2 = list(map(float, file.readline().split()))
dots3 = list(map(float, file.readline().split()))
y = [i for i in range(len(dots1))]
plt.plot(y, dots1)
plt.plot(y, dots2)
plt.plot(y, dots3)
plt.show()
