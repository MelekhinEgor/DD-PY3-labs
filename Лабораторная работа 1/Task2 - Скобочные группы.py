def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    if not brackets_row:  # если строка пустая, то корректный ответ
        return True
    elif brackets_row[0] == ')':  # если строка начинается с закрывающей скобки, то проверять ее нет смысла
        return False

    score = brackets_row.count('(') - brackets_row.count(')')

    return score == 0  # проверяем равенство открывающих и закрывающих скобок


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
# пустая строка
