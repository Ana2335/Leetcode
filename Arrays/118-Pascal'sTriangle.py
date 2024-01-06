def first(numRows):
    fila = []
    pascal = []
    cont = 2

    for i in range(6):
        fila = []
        if i == 0:
            fila.append(1)
            pascal.append(fila)
        elif i == 1:
            fila.insert(0, 1)
            fila.insert(-1, 1)
            pascal.append(fila)
        else:
            fila.insert(0, 1)
            print(fila)
            if i % 2 == 0:
                for j in range(i - 1):
                    fila.append(i)
                    print(fila)
                    cont += 1
            else:
                for j in range(i - 1):
                    fila.append(cont)
                    print(fila)
            fila.append(1)
            print(fila)
            pascal.append(fila)

    print(pascal)


def second(numRows):
    pascal = []
    lista = [1]
    pascal.append(lista)
    lista = [1, 1]
    pascal.append(lista)
    cont2 = 2
    cont3 = 3

    for i in range(numRows - 1):
        lista = []
        if i % 2 == 0:
            if i < 3:
                lista.append(1)
                lista.append(cont2)
                lista.append(1)
                pascal.append(lista)
                cont2 *= 2
            elif i > 3:
                lista.append(1)
                for j in range(i - 1):
                    lista.append(cont2)
                lista.append(cont2 + 2)
                for j in range(i - 1):
                    lista.append(cont2)
                lista.append(1)
                pascal.append(lista)

        elif i % 2 != 0:
            lista.append(1)
            for j in range(i - 1):
                lista.append(cont3)
            for j in range(i - 1):
                lista.append(cont3)
            lista.append(1)
            pascal.append(lista)

    print(pascal)


def third(numRows):
    pascal = []
    cont = 2

    for i in range(6):
        fila = []
        if i == 0:
            fila = [1]
            pascal.append(fila)
        elif i == 1:
            ila = [1, 1]
            pascal.append(fila)
        else:
            fila.append(1)
            print(fila)
            if i % 2 == 0:
                for j in range(i - 1):
                    fila.append(i)
                    print(fila)
                    cont += 1
            else:
                for j in range(i - 1):
                    fila.append(cont)
                    print(fila)
            fila.append(1)
            print(fila)
            pascal.append(fila)

    print(pascal)


def fourth(numRows):
    pascal = []
    fila = []

    for i in range(numRows):
        fila = []
        if i == 0:
            fila = [1]
        elif i == 1:
            fila = [1, 1]
        else:
            fila = [1]
            for j in range(i - 1):
                n = pascal[i - 1][j + 1] + pascal[i - 1][j]
                fila.append(n)
            fila.append(1)
        pascal.append(fila)

    print(pascal)


numRows = 5
fourth(numRows)