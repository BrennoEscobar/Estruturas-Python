#-------------------------------------------------------#

print('-' * 55)
print("\nExercício 03 Estrutura de repetição\n")
numero = int(input("Digite o número para a tabuada: "))
for sequencia in range(1,11):
  print("%2d x %2d = %3d" %(sequencia,numero,sequencia*numero))
#%2d -> serve para criar um alinhamento de colunas entre os valores

#-------------------------------------------------------#

print('-' * 55)
print("\nExercício 02 Estrutura de repetição\n")
s = 0
for contador in range(1,11):
  nota = float(input("Digite a nota "+str(contador)+": "))
  s += nota
print("Média = ",s/10)

#-------------------------------------------------------#

print('-' * 55)
print("Exercício 01 Estrutura de repetição\n")
s = 0
for x in range(3,334,3):
  s += x
print("Soma = ",s)
