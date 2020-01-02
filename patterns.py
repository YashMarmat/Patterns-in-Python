
'''Patterns basic concepts'''


# Simple pattern
'''
n = 6
for each in range(1,n):
    print('*')
'''
# Understanding Pattern Multiplication
'''
n = 6
for each in range(1,n):
    print('* ' * each)
'''

# Understanding Pattern sunbtraction
'''
n = 6
for each in range(1, n):
    print((n - each) * ' *')
'''

# understanding blank spaces
'''
n = 6
for each in range(1, n):
    print(' ' * each + each * ' * ')
'''

'''from below we see the patterns applied by using above logic'''

# right triangle (facing left)
'''
n = 6
for each in range(1, n):
    print('  ' * (n-each) + each * '* ')
'''

# right triangle (facing right)
'''
n = 6
for each in range(1,n):
    print('* ' * each)
'''

# A triangle
'''
n = 7
for each in range(1, n):
    print(' ' * (n-each) + each * '* ')
'''

# Tree
'''
n = 7
for each in range(1, n):
    print(' ' * (n-each) + each * '* ')
p = 3
for each in range(1, p):   # running this loop twice
    print(' ' * 5 + '* *')
'''

# A christmas tree (just a bigger tree)
'''
n = 7
for each in range(1, n):
    print(' ' * (n-each) + each * '* ')
for each in range(4, n+1):
    print(' ' * (n-each) + each * '* ')
for each in range(4, n+1):
    print(' ' * (n-each) + each * '* ')
p = 4
for each in range(1, p):   # running this loop twice
    print(' ' * 5 + '* *')
'''




















