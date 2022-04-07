# Nam Doan
# 1847037

input_text = input()
text = input_text.split()

for word in text:
    frequency = text.count(word)
    print(word, frequency)
