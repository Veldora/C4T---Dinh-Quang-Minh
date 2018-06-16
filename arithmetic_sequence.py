def arithmetic(n):
    arithmetic_list = []

    for i in range(n):
        if i % 2 == 0:
            number = 2 - (i / 2) * 0.5
            arithmetic_list.append(number)
        else:
            arithmetic_list.append(-1)

    return arithmetic_list
