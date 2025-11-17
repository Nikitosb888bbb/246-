temp=float(input('Введите температуру тела в Цельсиях: '))
pressure = float(input('Введите Ваше верхнее давление: '))
pulse= int(input('Введите свой пульс: '))

if 36<=temp<=37 and 110<=pressure<=130 and 60<=pulse<=100:
    print('Никаких действий не требуется.')
elif 35<=temp<=36 and 105<=pressure<=110 and (55<=pulse<=60 or 100<=pulse<=110):
    print('Отдохните, у Вас легкое недомогание')
else:
    print('Необходима помощь врача!')
