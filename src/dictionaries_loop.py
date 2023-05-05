print('########  Loop with Dictionaries')

student6 = {'name': 'raj',
            'age':  27,
            'location': 'dallas'
            }
print(" Loop only keys.")
for value in student6:
    print(f'element, by default key: {value}')
    print(f'value of key: {student6[value]}')

print(" Making the loop explicitly by keys() function.")
for value in student6.keys():
    print(f'element, by default key: {value}')
    print(f'value of key: {student6[value]}')

print("  Looping through the values() function.")
for value in student6.values():
    print(f'value: {value}')

print("  Looping through keys and values at the same time with items() function.")
for key, value in student6.items():
    print(f'key: {key}')
    print(f'value: {value}')


# H/W: 6-4, 6-5, 6-6 (chapter 6)









