import datetime

FORMAT = '%H:%M:%S'  # Формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    return len(data) == 2 and all(data)


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    return not (storage_data and time <= max(storage_data.keys(), key=lambda x: datetime.datetime.strptime(x, FORMAT)))


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    return sum([value[1] for value in storage_data.values()]) + steps


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    return steps * STEP_M / 1000


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    duration_hours = datetime.datetime.strptime(current_time, FORMAT).hour
    return (K_1 * WEIGHT + K_2 * HEIGHT + 0.9) * dist * duration_hours


def show_message(time, steps, dist, calories, achievement):
    """Отобразить информационное сообщение."""
    print(f"Время: {time}")
    print(f"Количество шагов за сегодня: {steps}")
    print(f"Дистанция составила {dist:.2f} км.")
    print(f"Вы сожгли {calories:.2f} ккал.")
    print(achievement)


# Пример использования:
def determine_achievement(steps):
    """Определить достижение в зависимости от количества шагов."""
    if steps < 5000:
        return "Поднажмите! Вы еще не в достаточной форме."
    elif 5000 <= steps < 10000:
        return "Хороший результат! Продолжайте двигаться."
    elif 10000 <= steps < 15000:
        return "Отличная работа! Вы на правильном пути."
    else:
        return "Невероятно! Вы превзошли все ожидания. Так держать!"


# Пример использования:
package = ('9:36:02', 15000)

if check_correct_data(package):
    time, steps = package
    if check_correct_time(time):
        storage_data[time] = (get_step_day(int(steps)), steps)
        distance = get_distance(int(steps))
        calories = get_spent_calories(distance, time)

        achievement = determine_achievement(get_step_day(int(steps)))

        show_message(time, get_step_day(int(steps)), distance, calories, achievement)
    else:
        print("Ошибка: Некорректное время.")
else:
    print("Ошибка: Некорректные данные пакета.")
