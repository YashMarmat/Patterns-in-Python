
'''Triangle and Square Patterns'''

# Up and Down triangles (right formation)
'''
n = 6
for each in range(1, n):
    print('* ' *each)
for each in range(1, n):
    print('* ' * (n-each))
'''

# Up and Down triangles (left formation)
'''
n = 6
for each in range(1,n):
    print('  ' * (n - each) + each * ' *')
for each in range(1,n):
    print('  ' * each + ' *' * (n - each))
'''
# A Diamond : combination of above triangles (Method 1)
'''
n = 6
for each in range(1,n):
    print(('  ' * (n - each) + each * ' *') + ('* ' *each))
for each in range(1,n):
    print('  ' * each + ' *' * (n - each) + '* ' * (n-each))
'''

# A Diamond : (Method 2)
'''
n = 8
for each in range(1,n):
    print('  ' * (n - each)+ '  * ' * each)
p = 6
for each in range(1,p):
    print('  ' * each + '    *' * (p - each))
'''

# Both diamonds
'''
print('\n')
n = 6
for each in range(1,n):
    print(('  ' * (n - each) + each * ' *') + ('* ' *each))
for each in range(1,n):
    print('  ' * each + ' *' * (n - each) + '* ' * (n-each))

print('\n')

n1 = 8
for each in range(1,n1):
    print('  ' * (n1 - each)+ '  * ' * each)
p = 6
for each in range(1,p):
    print('  ' * each + '    *' * (p - each))
'''
# Square   print(('*') + (' ' * n + '*'))
'''
n = 5
print('\n' + '* ' * 9)
for each in range(1, n):
    print('*' + ('   ' * n + '*'))
print('* ' * 9)
'''

# A book shelf
'''
n = 5
print('\n' + '* ' * 9)
for each in range(1, n):
    print('*' + ('   ' * n + '*')), print('* ' * 9)
'''














