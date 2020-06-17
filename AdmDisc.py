import matplotlib.pyplot as plt

xaxis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
heights = [1, 2, 1, 3, 11, 7, 5, 8, 4]
labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

plt.bar(xaxis, heights, tick_label = labels, color = ['#48f032', '#f032c7'])

plt.title('Qtd de alunos por nota')
plt.xlabel('Notas')
plt.ylabel('Qtd de alunos')

plt.show()