cpdef str brute_force (str string):
    possiveis_tentativas = 20
    for i in range(0, possiveis_tentativas):
        values = []
        finalList = []
        decifrado = ''
        for char in string:
            values.append(int(ord(char) - i))
        
        for value in values:
            finalList.append((chr(value)))

        for str in finalList:
            decifrado = decifrado + str
        
        print(decifrado)
        