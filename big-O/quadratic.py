# (n^2): Descreve algoritmos cujo desempenho é quadrático em relação ao tamanho da entrada. Geralmente, é considerado ineficiente para entradas grandes.
lista = [1, 2, 3, 4, 5]

def quadratic(n):
  for i in n:
    for j in n:
      print(i, j)
    print('---')

quadratic(lista)