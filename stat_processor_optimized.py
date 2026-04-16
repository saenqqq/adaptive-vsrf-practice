# stat_processor_optimized.py
# Скрипт для обработки статистики по уголовным делам (ОПТИМИЗИРОВАННАЯ ВЕРСИЯ)

import csv
import json
import sys
import time
from collections import defaultdict

def load_data(filename):
    """
    Загружает данные из CSV файла.
    
    Args:
        filename (str): Путь к CSV файлу
        
    Returns:
        list: Список строк данных
        
    Raises:
        FileNotFoundError: Если файл не найден
    """
    data = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Пропускаем заголовок
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        sys.exit(1)
    return data

def calc_stats(data):
    """
    Подсчитывает количество дел по категориям.
    
    Args:
        data (list): Список данных
        
    Returns:
        dict: Статистика по категориям
    """
    stats = defaultdict(int)  # Более эффективно, чем обычный dict
    for row in data:
        if len(row) > 3:
            category = row[3]
            stats[category] += 1
    return dict(stats)

def find_duplicates_optimized(data):
    """
    Находит дубликаты по номеру дела (ОПТИМИЗИРОВАННАЯ ВЕРСИЯ).
    Сложность O(n) вместо O(n²).
    
    Args:
        data (list): Список данных
        
    Returns:
        list: Список дубликатов
    """
    seen = set()
    duplicates = set()
    
    for row in data:
        if len(row) > 0:
            case_number = row[0]
            if case_number in seen:
                duplicates.add(tuple(row))
            else:
                seen.add(case_number)
    
    return [list(item) for item in duplicates]

def make_report(stats, duplicates, filename):
    """
    Формирует отчёт в формате JSON.
    
    Args:
        stats (dict): Статистика по категориям
        duplicates (list): Список дубликатов
        filename (str): Имя выходного файла
    """
    report = {
        "statistics": stats,
        "duplicates_count": len(duplicates),
        "duplicates": duplicates[:10],  # Только первые 10 для отчёта
        "total_cases": sum(stats.values())
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"Отчёт сохранён в {filename}")

def create_test_data(filename, rows=1000):
    """
    Создаёт тестовые данные для проверки скрипта.
    
    Args:
        filename (str): Имя выходного файла
        rows (int): Количество строк
    """
    import random
    
    categories = ['Кража', 'Мошенничество', 'Грабёж', 'Разбой', 'Хулиганство']
    regions = ['Салават', 'Стерлитамак', 'Ишимбай', 'Уфа']
    statuses = ['Расследуется', 'В суде', 'Решено']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['case_number', 'date', 'region', 'category', 'status'])
        
        for i in range(rows):
            writer.writerow([
                f"{random.randint(100,999)}-{random.randint(1,99)}/{random.randint(2020,2024)}",
                f"{random.randint(1,28)}.{random.randint(1,12)}.{random.randint(2020,2024)}",
                random.choice(regions),
                random.choice(categories),
                random.choice(statuses)
            ])
    
    print(f"Создан тестовый файл {filename} с {rows} записями")

def main():
    """Главная функция скрипта"""
    input_file = "test_cases.csv"
    
    # Создаём тестовые данные
    create_test_data(input_file, 1000)
    
    print("=" * 50)
    print("ОПТИМИЗИРОВАННЫЙ СКРИПТ ОБРАБОТКИ СТАТИСТИКИ")
    print("=" * 50)
    
    # Загрузка данных
    print("\n[1/4] Загрузка данных...")
    start = time.time()
    data = load_data(input_file)
    print(f"      Загружено {len(data)} записей за {time.time() - start:.3f}с")
    
    # Подсчёт статистики
    print("\n[2/4] Подсчёт статистики...")
    start = time.time()
    stats = calc_stats(data)
    print(f"      Статистика подсчитана за {time.time() - start:.3f}с")
    for category, count in stats.items():
        print(f"      - {category}: {count}")
    
    # Поиск дубликатов (оптимизированный)
    print("\n[3/4] Поиск дубликатов...")
    start = time.time()
    duplicates = find_duplicates_optimized(data)
    print(f"      Найдено дубликатов: {len(duplicates)} за {time.time() - start:.3f}с")
    
    # Сохранение отчёта
    print("\n[4/4] Сохранение отчёта...")
    start = time.time()
    make_report(stats, duplicates, "report_optimized.json")
    print(f"      Отчёт сохранён за {time.time() - start:.3f}с")
    
    print("\n" + "=" * 50)
    print("ГОТОВО! Скрипт успешно выполнен.")
    print("=" * 50)

if __name__ == "__main__":
    main()