def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):  # выполняем проверки на целочисленность и неотрицательность
        raise TypeError('Введено не целочилсеное число')
    if n < 0:
        raise ValueError('Введено отрицательное число')

    factorial = 1  # определяем базовое значение 0! = 1
    for i in range(1, n + 1):  # формируме итеративную последовтальность 
        factorial *= i
    return factorial
# пустая строка
