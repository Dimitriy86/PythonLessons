# Створення стеку
def create_stack():
    return[]

# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0

# Додавання елементу до стеку
def push(stack, item):
    stack.append(item)

# Вилучення елементу із стека
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Stack is empty")

# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Stack is empty")

stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')

# print(peek(stack))

print(pop(stack))

print(peek(stack))