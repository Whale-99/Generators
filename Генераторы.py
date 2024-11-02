def all_variants(text):
    # Перебираем длины под последовательностей от 1 до длины строки
    for length in range(1, len(text) + 1):
        # Для каждой длины генерируем последовательности, начиная с каждой позиции
        for start in range(len(text) - length + 1):
            yield text[start:start + length]

# Пример использования функции
a = all_variants("abc")
for i in a:
    print(i)
