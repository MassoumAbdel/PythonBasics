# 04-23-2023   Chapter 7: While Loop
# while loop - looping with conditions
# Note:  you need to increment/decrement or make sure there is ending condition for while loop

total = 0
while total <= 5:
    # here is the code to execute when expression returns True
    print(total)
    total +=1
print('************* completed first loop ************')
print('************* starting second loop ************')

total = 10 # while loop should have lower boundary
while total >= 5:
    # here is the code to execute when expression returns True
    print(total)
    total -=1

num = 0
while num != -1:
    num = int(input('Enter the number: ').strip())
    print(f'square of the number is: {num**2}')

print('************* completed ************')
print('************* completed second loop ************')

msg = ''
while msg.lower() != 'exit' and msg.upper() != 'X' and msg.lower() != 'no':
    msg= input('Enter you name: ').strip()
    if msg == '':
        print('whitespace characters were entered...')
        continue # go to next iteration, ignore next lines in this iteration
        # break # stop looping
    print(f'Hi {msg.title()} have a wonderful day !!!')
print('************* completed ************')

# how to find a number from the list of numbers and exit the loop when you find.   interview question


print('************* conditions with empty list and dictionary ************')

names = []
friends = {}
while friends and names:
    print('data structure is not empty')
print('************* completed ************')






