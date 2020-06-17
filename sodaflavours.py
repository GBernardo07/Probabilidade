import matplotlib.pyplot as plt

pieSlices = [51.1, 24.4, 10.9, 5.9, 3.2, 1.1, 0.7, 0.1, 0.5, 2.1]
flavours = ['Colas', 'Guarana', 'Laranja', 'Limao', 'Uva', 'Tutti Frutti', 'Tonica', 
    'Citrico', 'Maca', 'Outros sabores']
colors = ['#4DD66F', '#3586DE', '#AA4DC7', '#E0693F', '#D6BA33', '#6E69D6', '#DE52B6', 
    '#C78D68', '#E0CD5C', '#3DD69D']

plt.pie(pieSlices, colors = colors, startangle = 90)


plt.title('Consumo de refrigerantes no Brasil por sabor')
plt.legend(flavours)

plt.show()