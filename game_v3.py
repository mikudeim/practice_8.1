import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 1
    interval = 50
    check_point = 50

    while check_point != number:
        interval = (interval + 1) // 2
        if check_point > number:
            # check_point = (check_point + 1) // 2
            check_point = check_point - interval
            count += 1
        else:
            check_point = check_point + interval
            count += 1

    return count
    # Ваш код заканчивается здесь


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
