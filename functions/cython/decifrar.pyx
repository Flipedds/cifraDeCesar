def decifrar(str string, int rot):
    cdef list values = []
    cdef list finalList = []
    cdef str decifrado = ''
    for char in string:
        values.append(int(ord(char) - rot))
        
    for value in values:
        finalList.append((chr(value)))

    for str in finalList:
        decifrado = decifrado + str

    return decifrado

