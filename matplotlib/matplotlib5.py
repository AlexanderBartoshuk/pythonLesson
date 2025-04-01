import numpy as np
import matplotlib.pyplot as plt 


mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
n, bins , patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)


ax.set_xlabel('Length [cm]')
ax.set_ylabel('Probability')
ax.set_title('Aardvark lengths\n (not really)')
ax.text(75, .025,r'$\mu=115,\ \sigma=15$')
ax.axis([55,175,0,0.03])
ax.grid(True)

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']
ax.bar(categories, np.random.rand(len(categories)))
ax.set_facecolor('orange')









# Генерация тестовых данных
t = np.linspace(0, 10, 50)
s = np.sin(t)

# Создание фигуры и осей
fig, ((ax1, ax2)) = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')

# Первый график: синусоида и прямая линия
l1, = ax1.plot(t, s, label='Синусоида')
ax11 = ax1.twinx()  # Создаем вторую ось для прямой линии
l2, = ax11.plot(t, range(len(t)), 'C1', label='Прямая')

# Легенда для первого графика
ax1.legend(handles=[l1, l2], labels=['Синусоида (левая ось)', 'Прямая (правая ось)'])

# Второй график: синусоида с двумя осями (радианы и градусы)
ax2.plot(t, s)
ax2.set_xlabel('Угол [рад]')

# Вторичная ось сверху в градусах
ax21 = ax2.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
ax21.set_xlabel('Угол [°]')

# Отображение графиков
plt.show()
