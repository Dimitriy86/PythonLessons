add = lambda x, y: x + y
print(add(5, 3))

# ----------------------------------------------------------------

nums = [1, 2, 3, 4 ,5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)

# ----------------------------------------------------------------

# Map function
numbers = [1, 2, 3, 4, 5]
for i in map(lambda x: x**2, numbers):
    print(i)

# ----------------------------------------------------------------

# Filter function
even_numbers = filter(lambda x: x % 2 == 0, range(1, 11))
print(list(even_numbers))

# ----------------------------------------------------------------

def is_positive(x):
    return x > 0

nums = [-2, -1, 0, 1, 2]

positive_nums = filter(is_positive, nums)
print(list(positive_nums))

# ----------------------------------------------------------------

some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'
new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)

# ----------------------------------------------------------------

# fanction any

nums = [0, False, 5, 0]
result = any(nums)
print(result)

# ----------------------------------------------------------------

nums = [1, 3, 5, 7, 9]
result = any(x % 2 ==0 for x in nums)
print(result)

# ----------------------------------------------------------------

# function all

nums = [1, 2, 3, 4]
result = all(nums)
print(result)

# ----------------------------------------------------------------

nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in  nums)
print(is_all_even)

# ----------------------------------------------------------------
words = ['Hello', 'World', 'Python']
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)

# ----------------------------------------------------------------