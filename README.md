# 📊 Salary Report

Приложение для генерации отчётов по зарплате сотрудников из CSV-файлов. Поддерживается отчёт `payout`, рассчитывающий итоговую зарплату по отработанным часам и ставке.


## 🚀 Установка

1. Клонируй репозиторий:
   git clone https://github.com/yourusername/salary_report.git
   cd salary_report

2. Установи зависимости:
   pip install -r requirements.txt

## 📁 Структура проекта

salary_report/
│
├── main.py                  # Точка входа

├── reports/                 # Отчёты (реализован payout)

├── utils/                   # Утилиты (в т.ч. csv_parser)

├── data/                    # CSV-файлы с данными

├── tests/                   # тесты

└── requirements.txt         # зависимости


## 📌 Использование

### ✅ Генерация отчёта `payout`:

python3 -m main data1.csv data2.csv data3.csv --report payout

Если все файлы находятся в папке `data/`, нужно использовать:

python3 -m main data/data1.csv data/data2.csv data/data3.csv --report payout


### 🧠 Пример вывода:

```
                 name                hours  rate   payout
Marketing
---------------  Alice Johnson       160    50     $8000
---------------  Henry Martin        150    35     $5250
                                     310           $13250

Design
---------------  Bob Smith           150    40     $6000
---------------  Carol Williams      170    60     $10200
                                     320           $16200
```


## ⚙️ Настройка (опционально)

Чтобы не указывать `data/` каждый раз, можно:

Добавить симлинки:
   ln -s data/data1.csv data1.csv
   
   ln -s data/data2.csv data2.csv
   
   ln -s data/data3.csv data2.csv

   python3 -m main data1.csv data2.csv data3.csv --report payout

## 🧪 Тесты

Для запуска тестов:

pytest
