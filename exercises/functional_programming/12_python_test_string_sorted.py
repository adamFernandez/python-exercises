sentence = "is2 Thi1s T4est 3a"
# def order(s):
#     words = s.split()
#     sorted_output = ''
    
# order(sentence)

words = sentence.split()

# def extract_number(word):
#     for char in word:
#         if char.isdigit():
#             return int(char)
#     return float('inf')  # To handle words without numbers

# sorted_words = sorted(words, key=extract_number)

sorted_words = sorted(words, key=lambda word: int(next(filter(str.isdigit, word), float('inf'))))


result = " ".join(sorted_words)
print(result)


# Other results: 

# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))