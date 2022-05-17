l1 = "5.0, 100, 5.5, 101, 6.0, 102:L10;5.0, 99, 5.5, 100, 6.0, 101:L20;"

def makeMatrix(astring):
    matrix = []
    headers = []
    astring = astring.split(',')

    row = 0
    for item in astring:
        if ":" in item:
            x = item.split(":")
            matrix[row].append(x[0])
            row += 1
            x = x[-1].split(";")
            matrix.append([])
            matrix[row].append(x[-1])

        else:
            if len(matrix) <= row:
                matrix.append([])
            matrix[row].append(item)

    matrixDict = {}
    for item in matrix:
        if item[0] == "":
            continue
        print(item)
        matrixDict.get(item[0])






print(makeMatrix(l1))