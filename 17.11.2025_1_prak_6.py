temp=float(input('Введите температуру тела в Цельсиях: '))
pressure = float(input('Введите Ваше верхнее давление: '))
puls= int(input('Введите свой пульс: '))

if (temp>=36 or temp<=37) or (pressure>=110 or pressure<=130) or (puls>=60 or puls<=100):
    print ('Все хорошо, никаких действий не требуется.')
elif ((temp>=35) and (temp<=36) or ((temp>=37) and (temp<=38))) or ((pressure>=105) and (pressure<=110)) or ((pressure>=130) and (pressure <=140)) or ((puls>=55 and puls<=60) or (puls>=100 and puls<=110)):
    print ('Отдохните, у Вас легкое недомогание')
else:
    print ('Требуется помощь врача.')
print ('Хорошего дня, желаем здоровья')
