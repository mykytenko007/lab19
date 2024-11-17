import pandas as pd
import numpy as np

# 1. Генерація масиву
rows, cols = 10, 4
array = np.zeros((rows, cols))

# Заповнюємо перший стовпчик випадковими числами [1, 20]
array[:, 0] = np.random.randint(1, 21, size=rows)

# 2. Замінюємо повтори на випадкові числа [-10, -1]
unique, counts = np.unique(array[:, 0], return_counts=True)
repeated = unique[counts > 1]

for value in repeated:
    indices = np.where(array[:, 0] == value)[0][1:]
    array[indices, 0] = np.random.randint(-10, -1, size=len(indices))

# 3. Заповнення 2-го, 3-го і 4-го стовпчиків степенями значень першого стовпчика
array[:, 1] = array[:, 0]**2  # Другий степінь
array[:, 2] = array[:, 0]**3  # Третій степінь
array[:, 3] = array[:, 0]**4  # Четвертий степінь

# 4. Збереження у файл
df = pd.DataFrame(array, columns=["Col1", "Col2", "Col3", "Col4"])
df.to_csv('array.csv', index=False)

print("Масив збережено у файл 'array.csv'")
