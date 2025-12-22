def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

# Виконання next()
print(next(gen))
print(next(gen))
print(next(gen))

# -----------------------------------------------------------------------------

def count_down(start):
    while start > 0:
        yield start
        start -= 1
for number in count_down(5):
    print(number)

# -----------------------------------------------------------------------------

def read_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

# Виккористання генератора для читання рядків з файлу
for line in read_lines('my_file.txt'):
    print(line)
