def linha(N):
  for i in range(N):
    print(end = '_')
  print(" ")

def imprime_lista(L):
  contador = 0
  for valor in L:
    contador = contador + 1
    print(contador,')',valor)
  