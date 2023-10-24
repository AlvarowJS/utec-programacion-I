def draw(rows):
    body = ""

    for i in range(1, rows+1):
        body += ' ' * (rows-i)
        body += '#' * (i) 
        body += '\n'

    print('filas: '+ str(rows))
    print(body)    

draw(5)