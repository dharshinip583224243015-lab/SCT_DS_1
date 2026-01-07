import matplotlib.pyplot as plt

ages = [18, 19, 20, 21, 22, 22, 23, 24, 25, 25, 26, 28, 30, 35, 40]

plt.hist(ages, bins=5)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")

plt.show()
