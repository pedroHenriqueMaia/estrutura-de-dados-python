
lista = [1, 2, 3, 4, 5]

#O(1) + O(5) + O(n) + O(n) + O(3)
#O(9) + O(2n) -> O(n)
def combination(n):
  #O(1)
  print(n[0])
  
  #O(5)
  for i in range(5):
    print('test', i)
  
  #O(n)
  for i in n:
    print(i)
  
  #O(n)  
  for i in n:
    print(i)
  
  #O(3)
  print('python')
  print('python')
  print('python')

combination(lista)