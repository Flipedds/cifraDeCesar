import timeit
from functions.cython.funcaoCifrar import cifrar
from functions.cython.funcaoDecifrar import decifrar
from functions.cython.funcaoBruteForce import brute_force

stringParaCifrar = "Filipe"
stringCifrada = "ilolsh"

inicio = timeit.default_timer()
# print(f"Cifrado: {cifrar(stringParaCifrar, 3)}")
# print(f"Decifrado: {decifrar(stringCifrada, 3)}")

brute_force("ilolsh")

fim = timeit.default_timer()
tempo = fim - inicio
print ('tempo de execução: %.3f ms' % ((tempo * 1000)))
