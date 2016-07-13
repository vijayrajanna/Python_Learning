ab = { 'Swaroop' : 'swaroop@swaroopch.com',
       'Larry' : 'larry@wall.org',
       'Spammer' : 'vijay@vijay.com'
     }
print('Swaroop address is', ab['Swaroop'])
print('Number of contacts before deleting \"Spammer\"')
print('There are',len(ab),'contacts in the address-book')
# Deleting a key-value pair
del ab['Spammer']
print('There are',len(ab),'contacts in the address-book')

for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print('Guidos address is', ab['Guido'])