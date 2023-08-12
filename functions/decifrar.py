from functions.new import Array

def decifrar(string: str, rot: int):
    values: Array = []
    finalList: Array = []
    decifrado: str = ''
    for char in string:
        values.append(int(ord(char) - rot))

    for value in values:
        finalList.append(chr(value))

    for str in finalList:
        decifrado = decifrado + str

    return decifrado
