import pytest
from utils.csv_parser import parse_csv_content  


@pytest.mark.parametrize("csv_content,expected", [
    # 1. Стандартный случай
    (
        "id,email,name,department,hours_worked,hourly_rate\n"
        "1,alice@example.com,Alice Johnson,Marketing,160,50\n",
        [
            {
                "id": "1",
                "email": "alice@example.com",
                "name": "Alice Johnson",
                "department": "Marketing",
                "hours_worked": "160",
                "hourly_rate": "50",
            }
        ]
    ),
    # 2. Синоним "salary"
    (
        "name,department,hours_worked,salary,email,id\n"
        "Bob Smith,Design,150,40,bob@example.com,2\n",
        [
            {
                "name": "Bob Smith",
                "department": "Design",
                "hours_worked": "150",
                "hourly_rate": "40",
                "email": "bob@example.com",
                "id": "2",
            }
        ]
    ),
    # 3. Синоним "rate"
    (
        "name,rate,hours_worked\n"
        "Charlie,55,100\n",
        [
            {
                "name": "Charlie",
                "hourly_rate": "55",
                "hours_worked": "100",
            }
        ]
    ),
    # 4. Пробелы в значениях
    (
        "name , rate , hours_worked \n"
        "  Dana , 60 , 90 \n",
        [
            {
                "name": "Dana",
                "hourly_rate": "60",
                "hours_worked": "90",
            }
        ]
    ),
    # 5. Пустой CSV
    (
        "",
        []
    ),
    # 6. Заголовки есть, но нет строк
    (
        "name,rate,hours_worked\n",
        []
    ),
    # 7. Неполная строка (меньше столбцов, чем заголовков)
    (
        "name,rate,hours_worked\n"
        "Eve,70\n",
        [
            {
                "name": "Eve",
                "hourly_rate": "70",
                "hours_worked": "",
            }
        ]
    ),
    # 8. Неполная строка (больше значений, чем заголовков)
    (
        "name,rate\n"
        "Frank,80,extra\n",
        [
            {
                "name": "Frank",
                "hourly_rate": "80"
                # 'extra' игнорируется
            }
        ]
    ),
])
def test_parse_csv(csv_content, expected):
    result = parse_csv_content(csv_content)  # используем функцию для разбора из строки
    cleaned = [
        {k: v for k, v in row.items() if k in expected[0]} if expected else {}
        for row in result
    ]
    assert cleaned == expected
