original_str = input('Enter the original string: ')
rotated_str = input('Enter the rotated string: ')

temp_str = rotated_str + rotated_str
#temp_str = rotated_str * 2

if temp_str.find(original_str) == -1:
    print(rotated_str, 'is not rotated string of', original_str)
else:
    print(f'{rotated_str} is rotated string of  {original_str}')

