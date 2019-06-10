s = 'azcbobobegghakl'
num_of_vowels = 0

for char in s:
    if char == 'a' or char == 'i' or char == 'u' or char == 'e' or char == 'o':
        num_of_vowels += 1

print('Number of vowels: ' + str(num_of_vowels))