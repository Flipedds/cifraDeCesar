from functions.new import Array

def cifrar(string: str, rot: int):
    values: Array = []
    finalList: Array = []
    cifrado: str = ''
    for char in string:
        values.append(int(ord(char) + rot))
        
    for value in values:
        finalList.append((chr(value)))

    for str in finalList:
        cifrado = cifrado + str

    return cifrado
