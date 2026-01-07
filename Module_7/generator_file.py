def my_generator():
    received = yield "Ready"
    yield f"Recieved: {received}"

gen = my_generator()
print(next(gen))
print(gen.send("Hello"))

# ------------------------------------------------------------------------------------------------

def my_generator():
    try:
        yield "working"
    except GeneratorExit:
        print("Generator is being closed")

gen = my_generator()
print(next(gen))    # Отримуємо "working"
gen.close()         # Викликаємо закриття генератора

# ------------------------------------------------------------------------------------------------

def square_numbers():
    try:
        while True:                 # Безкінечний цикл для прийому чисел
            number = yield          # Отримання числа через send()
            square = number ** 2    # Піднесення до квадрата
            yield square            # Повернення результату
    except GeneratorExit:
        print("Generator closed")

# Створення і старт генератора
gen = square_numbers()

# Ініціалізація генератора
next(gen)       # Або gen.send(None), щоб стартувати

# Відправлення числа в генератор і отримання результату
result = gen.send(10)   # Повинно повернути 100
print(f"Square of 10: {result}")

# Перехід до наступного очцкування
next(gen)

# Відправлення іншого числа
result = gen.send(5)
print(f"Square of 5: {result}")

# Закриття генератора
gen.close()

# ------------------------------------------------------------------------------------------------

def filter_lines(keyword):
    print(f"Looking for {keyword}")
    try:
        while True:                 # Нескінченний цикл, де генератор чекає на вхідні дані
            line = yield            # Отримання рядка через send()
            if keyword in line:     # Перевірка на наявність ключового слова
                yield f"Line accepted: {line}"
            else:
                yield None
    except GeneratorExit:
        print("Generator closed")

if __name__ == "__main__":
    # Створення і старт генератора
    gen = filter_lines('hello')
    next(gen)       # Потрібно для старту генератора
    messages = ["this is a test", "hello world", "another hello world line", "hello again", "goodbuy"]
    hello_messages = []
    # Відправлення даних у генератор
    for message in messages:
        result = gen.send(message)  # Відправляємо поаавдрмлення у генератор
        if result:
            hello_messages.append(result)
        next(gen)   # Продовжуємо до наступного yield: інструкція Line = yield
    
    # Закриття генератора
    gen.close()
    print(hello_messages)
