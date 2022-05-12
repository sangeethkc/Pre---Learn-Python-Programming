
x = input('Enter a string: ')

y = []
z = []

for i in range(len(x)):
        if i % 2 == 0:
            y.append(x[i])
        else:
            z.append(x[i])

if len(x) > 7:
    print('Even indexed characters: {}'.format(y))
else:
    print('Odd indexed characters: {}'.format(z))