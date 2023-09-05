from re import I

set_A = set()
set_B = set()
set_resultado = set()
print("Defina o conjunto A: \n")
menu = ""
operacoes = ""

while True:
  menu = int(
      input(
          "Digite 0 para adicionar um numero ao conjunto A:\n\nDigite 1 para adicionar um numero ao conjunto B:\n\nDigite 3 para ir para as operaçoes: \n"
      ))
  if menu == 0:
    print("--------------------------------------")
    set_A.add(int(input("\nDigite o numero: \n\n")))
  if menu == 1:
    print("--------------------------------------")
    set_B.add(int(input("\nDigite o numero: \n\n")))
  if menu == 3:
    print("")
    print(set_A)
    print(set_B)
    print("")
    break

while True:
  operacoes = int(
      input(
          "Digite 1 para realizar a União dos Conjuntos\n\nDigite 2 para realizar a Intersecção dos Conjuntos\n\nDigite 3 para realizar a diferença\n\nDigite 4 para realizar o produto Cartesiano:\n}\nDigite 5 para sair: \n"
      ))
  if operacoes == 1:
    resultado = set_A.union(set_B)
    print(
        f"\nUnião: conjunto 1: {set_A}, conjunto 2 {set_B}. Resultado: {resultado}\n"
    )
  if operacoes == 2:
    resultado = set_A.intersection(set_B)
    print(
        f"\nIntersecção: conjunto 1: {set_A}, conjunto 2 {set_B}. Resultado: {resultado}\n"
    )
  if operacoes == 3:
    resultado = set_A.difference(set_B)
    print(
        f"\nDiferença: conjunto 1: {set_A}, conjunto 2 {set_B}. Resultado: {resultado}\n"
    )
  if operacoes == 4:
    resultado = [(x, y) for x in set_A for y in set_B]
    print(
        f"\nProduto cartesiano: conjunto 1: {set_A}, conjunto 2 {set_B}. Resultado: {resultado}\n"
    )
  if operacoes == 5:
    break
