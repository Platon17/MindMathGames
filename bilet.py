def bilet(n, op = '+-*/'):
    r = n.pop()
    nz = len(n) - 1     # количество знаков
    kop = len(op)       # количество операторов
    nv = kop ** nz  # количество вариантов

    for v in range(nv):  # перибираем все возможные варианты от 0000 до v
        # для каждого варианта высчитаем комбинацию знаков
        f = v
        z = ""
        for i in range(nz):
            z += op[f % kop]  # знак зависит от остатка деления на 4
            f = f // kop

        # формируем строку из чисел и знаков
        s = str(n[0])
        for i in range(nz):
            s += z[i]  # добавляем знак
            s += n[i + 1]  # добавляем следующее число

        rs = eval(s)  # вычисляем

        if float(r) == float(rs):
            break
    return str(s+"="+str(rs))
