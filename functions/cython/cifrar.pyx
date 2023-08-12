cpdef str cifrar(str string, int rot):
    cdef list values = []
    cdef list finalList = []
    cdef str cifrado = ''
    for char in string:
        values.append(int(ord(char) + rot))
        
    for value in values:
        finalList.append((chr(value)))

    for str in finalList:
        cifrado = cifrado + str

    return cifrado