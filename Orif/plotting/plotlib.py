import matplotlib.pyplot as plt

squares = []
for i in range(0,11):
    i=i*i
    squares.append(i)

plt.plot(squares)
plt.show()