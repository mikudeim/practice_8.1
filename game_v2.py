"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np


def random_predict(number: int = 1) -> int:
    """
    Guessing randomly
    :param number: original number, defaults to 1
    :return: number of tries
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    # print(f'Количество попыток: {count}')
    return count





def score_game(random_predict) -> int:
    """
    Calculates average number of tries it takes to guess number (1000 scale)
    :param random_predict: function that guesses a number until got it right
    :return: average number of tries until the number is guessed
    """

    count_ls = []
    np.random.seed(10)
    random_array = np.random.randint(1, 101, 1000)

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithms guesses the number in about {score} tries on average")
    return score

if __name__ == '__main__':
    score_game(random_predict)
