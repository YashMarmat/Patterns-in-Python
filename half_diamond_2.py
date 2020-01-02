# Up and Down triangles (left formation)

n = 6
for each in range(1,n):
    print('  ' * (n - each) + each * ' *')
for each in range(1,n):
    print('  ' * each + ' *' * (n - each))
