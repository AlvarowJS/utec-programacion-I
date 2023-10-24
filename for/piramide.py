def pyramid(rows):
    body = ""

    for i in range(1, rows + 1):
        body += ' ' * (rows - i)

        for j in range(1, i + (i - 1)):
            num = j % 10 
            body += str(num)

        body += ' ' * (rows - (i))
        body += '\n'

    print('filas: ' + str(rows))
    print(body)

pyramid(11)

