a = input('\nWhere is source file 1 located? ')
c = input('\nWhere is source file 2 located? ')
d = input('\nHow should the exit file be called? ')

f = open(a, 'r')      #open source file 1
g = open(c, 'r')      #open source file 2
e = open(d, 'a')      #open exit file

print('\n[====================================LOADING====================================]')

print('loading first file')

e.write(f.read())
e.write('\n')

print('finished loading first file')
print('loading second file')

e.write(g.read())
e.write('\n')

print('finished loading second file')
print('creating ' + d)

print('finish')