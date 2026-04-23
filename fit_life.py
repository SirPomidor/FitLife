# Проект FitLife - MVP версия 1.0

##################
# Копилка функций проверки
def get_valid_age():
    """Запрашивает возраст, проверяет корректность и возвращает int."""
    while True:
        try:
            age = int(input())
            if 0 < age <= 120:
                return age
            else:
                print(
                    "Пожалуйста, введите возраст от 1 до 120 лет.\n"
                    "Попробуй ещё раз:",
                )
        except ValueError:
            print("Нужно ввести целое число (например, 22). Попробуй ещё раз:")


def get_valid_name():
    """Запрашивает имя, не допускает цифр и пустых строк."""
    while True:
        name = input().strip()
        if any(ch.isdigit() for ch in name):
            print(
                "Имя не должно содержать цифр. "
                "Введи имя буквами (русскими или английскими).",
            )
        elif len(name) == 0:
            print("Имя не может быть пустым. Попробуй ещё раз:")
        else:
            return name


def get_valid_weight():
    """Запрашивает вес, проверяет допустимый диапазон (1–300 кг)."""
    while True:
        try:
            weight = float(input())
            if 1 <= weight <= 300:
                return weight
            else:
                print(
                    "Пожалуйста, введи реальный вес (от 1 до 300 кг). "
                    "Попробуй ещё раз:",
                )
        except ValueError:
            print("Ошибка! Нужно ввести число (например, 70.5). "
                  "Попробуй ещё раз:")


def get_valid_height():
    """Запрашивает рост в метрах, проверяет диапазон 0.5–5 м."""
    while True:
        try:
            height = float(input())
            if 0.5 <= height <= 5:
                return height
            else:
                print(
                    "Пожалуйста, введи рост в метрах (от 0.5 до 5). "
                    "Например, 1.75. Попробуй ещё раз:",
                )
        except ValueError:
            print("Ошибка! Нужно ввести число (например, 1.75). "
                  "Попробуй ещё раз:")


#######################

# 1. Знакомство
print("Привет! Я твой личный фитнес-трекер - FitLife!\n- а как зовут тебя?")
user_name = get_valid_name()

print(f"{user_name}, очень приятно!\nТеперь подскажи, сколько тебе лет?")
user_age = get_valid_age()

# Бонус: комментарий к возрасту
if user_age < 20:
    print("Ты молодой! Вперёд к рекордам!")
elif user_age < 40:
    print("Отличный возраст для тренировок!")
elif user_age < 55:
    print("Ого, держи форму!")
else:
    print("Ты большой(ая) молодец, аккуратнее с нагрузками!")

# 2. Сбор данных
print("Теперь, введи свой вес в кг:")
user_weight = get_valid_weight()

print("Прекрасно! Осталось узнать твой рост. "
      "Укажи его в метрах (например, 1.75):")
user_height = get_valid_height()

# 3. Логика расчётов
bmi = user_weight / (user_height ** 2)          # Индекс массы тела
water_needed = user_weight * 0.030              # 30 мл на кг = 0.030 литра

# 4. Вывод результата
print(f"\nПривет, {user_name}!")
print(f"Твой возраст: {user_age} лет")
print(f"Твой ИМТ: {bmi:.1f}")                   # округление до 1 знака
print(f"Норма воды в день: {water_needed:.1f} литра")
print("Расчёт окончен. Будьте здоровы!")