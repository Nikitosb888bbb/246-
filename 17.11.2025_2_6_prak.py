section=int(input('Введите номер кармана рулетки (0-36): '))

if section==0:
    print ('Карман зелёный')
elif 1<=section<=10:
    if section%2==0: #четный
        print('Карман черный')
    else:
        print ('Карман красный')
elif 10<=section<=18:
    if section%2==0:
        print('Карман красный')
    else:
        print('Карман черный')
elif 19<=section<=28:
    if section%2==0:
        print('Карман черный')
    else:
        print('Карман красный')
elif 29<=section<=36:
    if section%2==0:
        print('Карман красный')
    else:
        print('Карман черный')
else:
    print('Неправильный номер кармана рулетки')