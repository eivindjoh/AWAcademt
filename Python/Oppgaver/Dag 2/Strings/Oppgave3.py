punishment_text = 'I will not teach others to fly\n'
numb_of_repetition = 10
punishment_text = punishment_text.replace('not ', '')
punishment_text = punishment_text.replace('teach', 'force')
text = punishment_text * numb_of_repetition

print(text)


punishment_text = 'Science class should not end in tragedy.\n'
numb_of_repetition = 10
text = punishment_text * numb_of_repetition
count_of_words = punishment_text.count('class')

print(text)
print(f'The number of the word CLASS in the original sentence is: {count_of_words}')