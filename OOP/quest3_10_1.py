# Импортируйте необходимые модули.
from datetime import datetime


def validate_record(name: str, birthdate: str) -> bool:
    # Напишите код, верните булево значение.
    parts = birthdate.split('.')
    if len(parts) == 3:
        for part in parts:
            if not part.isdigit():
                print(f'Некорректный формат даты в записи: {name}, {birthdate}')
                return False
        try:
            datetime.strptime(birthdate, "%d.%m.%Y")
            return True
        except ValueError:
            print(f"Некорректный формат даты в записи: {name}, {birthdate}")
            return False

def process_people(entries: list[tuple]) -> dict:
    # Объявите счётчики.
    good_count = 0
    bad_count = 0

    for name, birthdate in entries:
        if validate_record(name, birthdate):
            good_count += 1
        else:
            bad_count += 1
    # Распакуйте кортежи из полученного списка entries.
    # Каждую пару значений передайте в validate_record(),
    # чтобы проверить корректность формата даты рождения.
    # В зависимости от результата проверки увеличьте один из счётчиков.

    # Верните словарь.
    return {'good': good_count, 'bad': bad_count}


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]
statistics = process_people(data)
print(f'Корректных записей: {statistics["good"]}')
print(f'Некорректных записей: {statistics["bad"]}')