from functions.cifrar import cifrar
from functions.decifrar import decifrar

stringParaCifrar = input("Digite a palavra/frase à ser cifrada!: ")
rotacao = int(input("Digite a rotação: "))

print(f"Cifrado: {cifrar(stringParaCifrar, rotacao)}")

stringCifrada = input("Digite a palavra/frase à ser decifrada!: ")
rotacao = int(input("Digite a rotação: "))
print(f"Decifrado: {decifrar(stringCifrada, rotacao)}")
