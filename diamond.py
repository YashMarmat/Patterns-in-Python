# A Diamond : by combination of triangles 

n = 6
for each in range(1,n):
    print(('  ' * (n - each) + each * ' *') + ('* ' *each))
for each in range(1,n):
    print('  ' * each + ' *' * (n - each) + '* ' * (n-each))
