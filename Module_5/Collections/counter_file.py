from collections import Counter

# --------------------------------------------------------------------------------------------

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
marks_counts = {}
for mark in student_marks:
    if mark in marks_counts:
        marks_counts[mark] += 1
    else:
        marks_counts[mark] = 1

print(marks_counts)

# --------------------------------------------------------------------------------------------

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = Counter(student_marks)
print(mark_counts)

# --------------------------------------------------------------------------------------------

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = Counter(student_marks)

print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))

# --------------------------------------------------------------------------------------------

letter_count = Counter('banana')
print(letter_count)

# --------------------------------------------------------------------------------------------

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)

# # Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")
