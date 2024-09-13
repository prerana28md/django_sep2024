# Program to check if a letter is present in a name

my_name = input('Enter your name: ')
letter = input('Enter the letter to be searched: ')

# 'anantapuram'
letter_index = my_name.find('a')
print('Index of a = ', letter_index)
letter_index = my_name.find('a', 3)
print('Index of a = ', letter_index)
letter_index = my_name.find('a', 6, 9)
print('Index of a = ', letter_index)