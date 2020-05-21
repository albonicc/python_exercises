


def printTable(tableData):
    colWidths = [0] * len(tableData)
    longestStr = 0
    row = range(len(tableData))
    column = range(len(tableData[0]))

    for i in row:
        for j in column:
            if  len(tableData[i][j]) > longestStr:
                longestStr = len(tableData[i][j])
        colWidths[i] = longestStr
        longestStr = 0
    print(" ")
    for i in  column:
        for j in row:
            x = tableData[j][i].rjust(colWidths[j]) 
            if  j == max(row):
                print(x)
            else:
                print(x, end = " ")
    print(" ")





tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
