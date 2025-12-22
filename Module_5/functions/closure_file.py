from typing import Callable, Dict

# -----------------------------------------------------------------------------------

def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    
    return inner_function

# Створення замикання
my_func = outer_function('Hello world!')
my_func()

# -----------------------------------------------------------------------------------

def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # Використовуємо nonlocal, щоб змінити змінну в звмиканні
        nonlocal count
        count += 1
        return count
    
    return increment

# Створення лічильника
count_calls = counter()

# Виклики личильника
print(count_calls())
print(count_calls())
print(count_calls())

# -----------------------------------------------------------------------------------

# Каррінг (currying)

def add(a):
    def add_b(b):
        return a + b
    return add_b

# Використання:
add_5 = add(5)
result = add_5(10)
print(result)

# -----------------------------------------------------------------------------------

def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)

# Використання
discounted_price = apply_discount(500, 10)
print(discounted_price)

discounted_price = apply_discount(500, 20)
print(discounted_price)

# -----------------------------------------------------------------------------------

def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: int) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount

# Каррінг в дії
ten_percent_dicount = discount(10)
twenty_persant_discount = discount(20)

# Застосування знижок
discounted_price = ten_percent_dicount(500)
print(discounted_price)

discounted_price = twenty_persant_discount(500)
print(discounted_price)

# -----------------------------------------------------------------------------------

def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount

# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    '10%': discount(10),
    '20%': discount(20),
    '30%': discount(30)
}

# Використання функції зі словника
price = 500
discount_type = '20%'

discounted_price = discount_functions[discount_type](price)
print(f'Ціна зі знижкою {discount_type}: {discounted_price}')
