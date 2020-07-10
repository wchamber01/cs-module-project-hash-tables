import string
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# import the message
txt = open('./applications/crack_caesar/ciphertext.txt').read()

cipher_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
               'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

cipher = {i: cipher_list[i] for i in range(0, len(cipher_list))}

dictionary = {}

alphabet = string.ascii_uppercase

for character in txt:
    for alpha in alphabet:
        # if character.isalpha(): --> doesn't work for this scenario
        if character in alpha and character not in dictionary:
            # dictionary[character] = 1 if character not in dictionary else dictionary[character] + 1
            dictionary[character] = 1
    else:
        if character in dictionary:
            dictionary[character] += 1

# sort d by highest freq to lowest
sorted_dict = dict(
    sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

# loop through sorted_dict and replace all values with corresponding letter from cipher
for index, key in enumerate(sorted_dict):
    if index in cipher:
        sorted_dict[key] = cipher[index]

code = ''
for i in txt:
    if i in alphabet:
        # print(i)
        code += sorted_dict[i]
    else:
        code += i
print(code)
