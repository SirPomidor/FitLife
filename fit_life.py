
"""Фитнес-трекер FitLife - сбор данных пользователя и расчёт ИМТ и нормы воды."""

# Константы
MAX_AGE = 120
MIN_AGE = 1

MAX_WEIGHT = 300
MIN_WEIGHT = 1

MAX_HEIGHT = 5.0
MIN_HEIGHT = 0.5

WATER_PER_KG = 0.030  


def get_valid_age():
    """Запрашивает возраст, проверяет корректность и возвращает int."""
    while True:
        try:
            age = int(input())
            if MIN_AGE <= age <= MAX_AGE:
                return age
            print(f"Пожалуйста, введите возраст от {MIN_AGE} до {MAX_AGE} лет.\nПопробуй ещё раз:")
        except ValueError:
            print("Нужно ввести целое число (например, 22). Попробуй ещё раз:")


def get_valid_name():
    """Запрашивает имя, не допускает цифр и пустых строк."""
    while True:
        name = input().strip().title()  
        if any(ch.isdigit() for ch in name):
            print("Имя не должно содержать цифр. Введи имя буквами (русскими или английскими).")
        elif len(name) == 0:
            print("Имя не может быть пустым. Попробуй ещё раз:")
        else:
            return name


def get_valid_weight():
    """Запрашивает вес, проверяет допустимый диапазон (1–300 кг)."""
    while True:
        try:
            weight_input = input().replace(',', '.')  
            weight = float(weight_input)
            if MIN_WEIGHT <= weight <= MAX_WEIGHT:
                return weight
            print(f"Пожалуйста, введи реальный вес (от {MIN_WEIGHT} до {MAX_WEIGHT} кг).\nПопробуй ещё раз:")
        except ValueError:
            print("Ошибка! Нужно ввести число (например, 70.5). Попробуй ещё раз:")


def get_valid_height():
    """Запрашивает рост в метрах, проверяет диапазон 0.5–5 м."""
    while True:
        try:
            height_input = input().replace(',', '.')  
            height = float(height_input)
            if MIN_HEIGHT <= height <= MAX_HEIGHT:
                return height
            print(f"Пожалуйста, введи рост в метрах (от {MIN_HEIGHT} до {MAX_HEIGHT}).\nНапример, 1.75. Попробуй ещё раз:")
        except ValueError:
            print("Ошибка! Нужно ввести число (например, 1.75). Попробуй ещё раз:")


def get_age_comment(age):
    """Возвращает комментарий к возрасту пользователя."""
    if age < 20:
        return "Ты молодой! Вперёд к рекордам!"
    if age < 40:
        return "Отличный возраст для тренировок!"
    if age < 55:
        return "Ого, держи форму!"
    return "Ты большой(ая) молодец, аккуратнее с нагрузками!"


# main
if __name__ == "__main__":
    print("Привет! Я твой личный фитнес-трекер - FitLife!\n- а как зовут тебя?")
    user_name = get_valid_name()

    print(f"{user_name}, очень приятно!\nТеперь подскажи, сколько тебе лет?")
    user_age = get_valid_age()

    print(get_age_comment(user_age))

    print("\nТеперь введи свой вес в кг:")
    user_weight = get_valid_weight()

    print("Прекрасно! Осталось узнать твой рост. Укажи его в метрах (например, 1.75):")
    user_height = get_valid_height()

    # Расчёты
    bmi = user_weight / (user_height ** 2)
    water_needed = user_weight * WATER_PER_KG

    # Вывод результата
    print(f"\nПривет, {user_name}!")
    print(f"Твой возраст: {user_age} лет")
    print(f"Твой ИМТ: {bmi:.1f}")
    print(f"Норма воды в день: {water_needed:.1f} литра")
    print("Расчёт окончен. Будьте здоровы!")





