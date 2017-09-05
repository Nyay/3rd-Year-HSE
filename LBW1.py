def number_1(line, low_b, high_b):
    for i in range(len(line)):
        try:
            if line[i] <= low_b:
                line[i] = low_b
            elif line[i] >= high_b:
                line[i] = high_b
        except TypeError:
            return 'Один из элементов входных данных не явлется числом. Проверьте последовательность и пороги.'
    return 'Новая последовательность: ' + str(line)

print(number_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3.3, 7))
