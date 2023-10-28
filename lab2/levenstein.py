#Процедура печати матрицы
def print_mas(mas, rows, cols, s1, s2):
    for i in range (0, rows):
        for j in range (0, cols):
            if i == 0 and j > 0:
                print(s2[mas[i][j] - 1], " ", end = "")
            elif j == 0 and i > 0:
                print(s1[mas[i][j] - 1], " ", end = "")
            else:
                print(mas[i][j], " ", end = "")
        print()

#Функция, возвращающая расстояние левенштейна между двумя словами
def levenstein(s1, s2):
    #Создание пустой матрицы(s1 - вертикаль, s2 - горизонталь)
    rows = len(s1)+1
    cols = len(s2)+1
    mas = [[0 for j in range(cols)] for i in range(rows)]

    #Заполнение первого столбца и первой строки
    for i in range(1, rows):
        mas[i][0] = i
    for j in range(1, cols):
        mas[0][j] = j

    #Заполнение всей матрицы
    for col in range(1, cols):
        for row in range(1, rows):
            #Сравнение текущих букв
            if s1[row-1] == s2[col-1]:
                cost = 0
            else:
                cost = 1
            mas[row][col] = min(mas[row-1][col] + 1,      # удаление 
                                mas[row][col-1] + 1,      # вставка
                                mas[row-1][col-1] + cost) # замена
    
            if row > 1 and col > 1 and s1[row-1] == s2[col-2] and s1[row-2] == s2[col-1]:
                mas[row][col] = min(mas[row][col], mas[row-2][col-2] + cost)

    print_mas(mas, rows, cols, s1, s2)
    return mas[row][col]

s1 = input("Введите первое слово: ")
s2 = input("Введите второе слово: ")

print("Расстояние Левенштейна между словами", s1, "и", s2, "равно", levenstein(s1, s2))

final = input("Завершение программы: ")
