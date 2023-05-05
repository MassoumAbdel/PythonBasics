# H/W on Problem-solving
# 1 - given string input count how many vowels used in the string (e, o , i , u, a)
# hello -> 2 vowels
#    # count = 0

input_text = input('Enter any word: ').lower()
count = 0
for vowel in input_text :
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u': # or if vowel in 'aeiou':
        count+= 1
print(f'number of vowels in your word are: {count}')


# 2 - given string input count how many times each letter is used. Ignore whitespace(spaces,tabs, enters)
# hello -> result = {'h':1, 'e':1, 'l':2, '0':1}
#    # result['o'] = result['o'] + 1
#    # loop through input
#    # result.setdefault('o',1)
#    # result['o'] = result['o'] +1


for letter in 'hello':
    print(letter)
msg = ''
while msg.lower() != 'exit' and msg.upper() != 'X' and msg.lower() != 'no':
    msg= input('Enter you name: ').strip()
    if msg == '':
        print('whitespace characters were entered...')
        continue # go to next iteration, ignore next lines in this iteration.
        # break # stop looping
    print(f'Hi {msg.title()} have a wonderful day !!!')