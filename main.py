def corresponding_parenthesis(string: str):
    left = string.count('(')
    rigth = string.count(')')
    difference = left - rigth

    if difference > 0:
        return '(' * difference
    elif difference < 0:
        return ')' * abs(difference)

    return ''


# Exemplo 1
result = corresponding_parenthesis("()()")
print(result)

# Exemplo 2
result = corresponding_parenthesis("()))")
print(result)

# Exemplo 3
result = corresponding_parenthesis(")))(((((")
print(result)


def remove_more_than_two_repetitions(string: str):
    response = []
    response.append(string[0])
    response.append(string[1])

    for index, char in enumerate(string[2:], 2):
        if string[index - 1] != char or string[index - 2] != char:
            response.append(char)

    return "".join(response)


text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
text = remove_more_than_two_repetitions(text)
print(text)
