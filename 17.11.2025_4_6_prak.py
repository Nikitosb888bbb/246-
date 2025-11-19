vert_1,horiz_1 = map(int,input('Введите положение клетки_1 через пробел (вертикаль горизонталь): ').split())
vert_2,horiz_2 = map(int,input('Введите положение клетки_2 через пробел (вертикаль горизонталь): ').split())
if not (1<=vert_1<=8 and 1<=horiz_1<=8 and 1<=vert_2<=8 and 1<=horiz_2<=8):
    print('Ошибка! Неправильный ввод данных клеток.')
else:
    if abs(vert_1-vert_2)==abs(horiz_1-horiz_2):
        print('YES. Слон может так ходить')
    else:
        print('NO. Слон не может так ходить')

