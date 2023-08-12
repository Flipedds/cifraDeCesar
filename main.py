import timeit
from functions.cython.funcaoCifrar import cifrar
from functions.cython.funcaoDecifrar import decifrar

stringParaCifrar = "Filipe"
stringCifrada = "ilolsh"

inicio = timeit.default_timer()
print(f"Cifrado: {cifrar(stringParaCifrar, 3)}")
print(f"Decifrado: {decifrar(stringCifrada, 3)}")

fim = timeit.default_timer()
print ('tempo de execução: %f' % (fim - inicio))
