def base_change_to_decimal(number, base):
    factor = 1
    temp = 0
    while number > 0:
        temp += number % 10 * factor
        factor *= base
        number = number // 10
    return temp
