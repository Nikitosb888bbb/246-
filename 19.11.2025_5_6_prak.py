vert_1,horiz_1 = map(int,input('Введите положения клетки 1 через пробел (Вертикаль Горизонталь): ').split())
vert_2,horiz_2 = map(int,input('Введите положение клетки 2 через пробел (Вертикаль Горизонталь): ').split())
if not (1<=vert_1<=8 and 1<=horiz_1<=8 and 1<=vert_2<=8 and 1<=horiz_2<=8):
    print('Ошибка! Неправильный ввод данных клеток.')
else:
    if vert_1==vert_2 or horiz_1==horiz_2 or abs(horiz_1-horiz_2)==abs(vert_1-vert_2):
        print('YES. Ферзь может ходить таким образом')
    else:
        print('NO. Ферзь не может так ходить')