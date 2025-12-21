from decimal import Decimal, ROUND_DOWN, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_UP
from decimal import getcontext

# --------------------------------------------------------------

print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))
print(Decimal('0.1') + Decimal('0.2'))

# --------------------------------------------------------------

getcontext().prec = 6
print(Decimal('1')/Decimal('7'))

getcontext().prec = 8
print(Decimal('1')/Decimal('7'))

# --------------------------------------------------------------

getcontext().prec = 6
print(Decimal('223')/Decimal('7'))

# --------------------------------------------------------------

# Вхідне число Decimal
number = Decimal('3.14159')

# Встановлення точності до двох знаків після коми
rounder_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)

print(rounder_number)

# --------------------------------------------------------------

number = Decimal('1.45')

# Округлення за замовчуванням до одного десяткового знаку
print(f"Округлення за замовчуванням ROUND_HALF_EVEN: ", number.quantize(Decimal('0.0')))

# Округлення вверх при ничії (ROUND_HALF_UP)
print(f"Округлення вгору ROUND_HALF_UP: ", number.quantize(Decimal('0.0'),
                                                           rounding=ROUND_HALF_UP))

# Округлення вниз (ROUND_FLOOR)
print(f"Округлення вниз ROUND_FLOOR: ", number.quantize(Decimal('0.0'),
                                                        rounding=ROUND_FLOOR))

# Округлення вгору (ROUND_CEILING)
print(f"Округлення вгору ROUND_CEILING: ", number.quantize(Decimal('0.0'),
                                                          rounding=ROUND_CEILING))

# Округлення до трьох десяткових знаків за замовчуванням
print(f"Округлення до трьох десяткових знаків: ",
      Decimal('3.14159').quantize(Decimal('0.000')))
