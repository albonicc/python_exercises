def insertComa(list):
    for i in range(len(list)):
        if i < len(list) - 2: 
            list[i] = list[i] + ", "
        elif i == len(list) - 2:
            list[i] = list[i] + " "
        else:
            list[i] = "and " + list[i]
    result = "".join(list)
    print(result)

#def toStr(list):
#    string = ""
#    for i in range(len(list)):
#        string += list[i]
#    return string

spam = ['apples', 'bananas', 'tofu', 'cats']
insertComa(spam)
#result = toStr(spam)
#print(result)
 
