import pandas as pd

# 1. Зчитування даних із файлу
with open('mas.txt', 'r') as file:
    data = [list(map(int, line.split())) for line in file.readlines()]

# Перетворення у Series
data_series = pd.Series([item for sublist in data for item in sublist])

# 2. Видалення повторів
unique_data = data_series.drop_duplicates()

# 3. Збереження у JSON-файл
unique_data.to_json('unique_data.json', orient='values')

print("Унікальні значення збережено у файл 'unique_data.json'")

