import matplotlib.pyplot as plt

genders = ['male', 'female']
slices = [5, 5]
colors = ['blue', 'pink']

plt.pie(slices, labels = genders, colors = colors, startangle = 90)

plt.show()