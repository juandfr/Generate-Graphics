from matplotlib import pyplot as plt
import numpy as np

python = [6, 7, 8, 4, 4]

javascript = [3, 12, 3, 4.1, 6]

x1 =  np.arange(len(python))
x2 = [x + 0.25 for x in x1]

plt.bar(x1, python, width=0.25, label = 'Python', color = 'deepskyblue')
plt.bar(x2, javascript, width=0.25, label = 'Javascript', color = 'mediumseagreen')

meses = ['Agosto','Setembro','Outubro','Novembro','Dezembro']
plt.xticks([x + 0.25 for x in range(len(python))], meses)

plt.legend()

plt.title("Uso das linguagens")
plt.show()