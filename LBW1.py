def number_1(line, low_b, high_b):
    for num in line:
        if type(num) is not int and type(num) is not float:
            return 'Элемент последовательности "' + str(num) + '" не является числом.'
    if type(low_b) is not int and type(low_b) is not float:
        return 'Нижняя граница задана не числом'
    if type(high_b) is not int and type(high_b) is not float:
        return 'Верхняя граница задана не числом'
    for i in range(len(line)):
        try:
            if line[i] <= low_b:
                line[i] = low_b
            elif line[i] >= high_b:
                line[i] = high_b
        except TypeError:
            return print('Один из элементов входных данных не явлется числом. Проверьте последовательность и пороги.')
    return print('Новая последовательность: ' + str(line))

print(number_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3.3, 7))
