import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
height = [1, 2, 1, 3, 11, 7, 5, 8, 4]
labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

plt.bar(left, height, tick_label = labels)

plt.xlabel('Notas')
plt.ylabel('Qtd. de alunos')
plt.title('Qtd. de alunos por nota')

plt.show()