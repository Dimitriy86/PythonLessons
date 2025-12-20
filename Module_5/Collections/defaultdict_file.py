from collections import defaultdict

# --------------------------------------------------------------------------------------------

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)

# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

print(d)

# --------------------------------------------------------------------------------------------

d = defaultdict(int)

# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1

print(d)

# --------------------------------------------------------------------------------------------

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)
for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))
