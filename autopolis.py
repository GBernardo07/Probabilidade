import matplotlib.pyplot as plt

brands = ['General Motors', 'Ford', 'VolksWagen', 'Toyota', 
    'Renault-Nissan', 'Daimler-Chrysler', 'Outros']

slices = [22.8, 16.8, 9.4, 9.2, 8.7, 8.3, 24.8]

plt.pie(slices, labels = brands, startangle = 90, autopct='%1.1f%%')

plt.title("Distribuicao do controle do mercado automotivo")

plt.show()