# stat_processor.py
# Скрипт для обработки статистики по уголовным делам (ИСХОДНАЯ ВЕРСИЯ)

import csv
import json
import sys
import time

# Загрузка данных из CSV файла
def load_data(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)
    f.close()
    return data

# Подсчёт количества дел по категориям
def calc_stats(d):
    stats = {}
    for i in range(len(d)):
        cat = d[i][3]
        if cat not in stats:
            stats[cat] = 0
        stats[cat] = stats[cat] + 1
    return stats

# Поиск дубликатов (НЕЭФФЕКТИВНО - вложенные циклы)
def find_duplicates(data):
    dup = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i][0] == data[j][0]:
                if data[i] not in dup:
                    dup.append(data[i])
    return dup

# Формирование отчёта
def make_report(stats, filename):
    f = open(filename, 'w')
    f.write("Отчёт по уголовным делам\n")
    f.write("========================\n")
    for cat in stats:
        f.write(cat + ": " + str(stats[cat]) + "\n")
    f.close()

# Создание тестовых данных (если файла нет)
def create_test_data(filename, rows=1000):
    import random
    categories = ['Кража', 'Мошенничество', 'Грабёж', 'Разбой', 'Хулиганство']
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['case_number', 'date', 'region', 'category', 'status'])
        for i in range(rows):
            writer.writerow([
                f"{random.randint(100,999)}-{random.randint(1,99)}/{random.randint(2020,2024)}",
                f"{random.randint(1,28)}.{random.randint(1,12)}.{random.randint(2020,2024)}",
                random.choice(['Салават', 'Стерлитамак', 'Ишимбай', 'Уфа']),
                random.choice(categories),
                random.choice(['Расследуется', 'В суде', 'Решено'])
            ])
    print(f"Создан тестовый файл {filename} с {rows} записями")

# Главная часть
if __name__ == "__main__":
    input_file = "test_cases.csv"
    
    # Создаём тестовые данные
    create_test_data(input_file, 500)
    
    print("Загрузка данных...")
    start = time.time()
    data = load_data(input_file)
    print(f"Загружено {len(data)} записей за {time.time() - start:.2f}с")
    
    print("Подсчёт статистики...")
    start = time.time()
    stats = calc_stats(data)
    print(f"Статистика подсчитана за {time.time() - start:.2f}с")
    
    print("Поиск дубликатов...")
    start = time.time()
    duplicates = find_duplicates(data)
    print(f"Найдено дубликатов: {len(duplicates)} за {time.time() - start:.2f}с")
    
    print("Сохранение отчёта...")
    make_report(stats, "report.txt")
    
    print("Готово!")