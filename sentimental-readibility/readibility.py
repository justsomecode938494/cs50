from cs50 import get_string

text = get_string("Text: ")

letter = 0
space = 0
sentence = 0

for characters in text:
    if characters.isalpha():
        letter += 1
    elif characters == ' ':
        space += 1
    elif characters == '.' or characters == '?' or characters == '!':
        sentence += 1

words = space + 1

l = (letter/words) * 100
s = (sentence/words) * 100

grade = 0.0588 * l - 0.296 * s - 15.8

if grade > 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {round(grade)}")
