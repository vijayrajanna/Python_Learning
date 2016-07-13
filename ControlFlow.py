# __author__ = 'Vijay'
#
# number = 23
# guess = int(raw_input('Enter an integer : '))
# if guess == number:
#     print 'Congratulations, you guessed it.'
#     print '(but you do not win any prizes!)'
# # New block ends here
# elif guess < number:
# # Another block
#     print 'No, it is a little higher than that'
# # You can do whatever you want in a block ...
# else:
#     print 'No, it is a little lower than that'
# # you must have guessed > number to reach here
# print 'Done'
# # This last statement is always executed,
# # after the if statement is executed.
#
# name = raw_input('Enter your name')
# print ' your name is ', name
#
# for i in range(1, 5):
#     print i

for i in range(0,7):
    print i

while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    print 'Length of the string is', len(s)
print 'Done'

