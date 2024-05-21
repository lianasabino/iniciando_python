# Tupla é uma coleção ordenada e imutável de elementos

# Criando uma tupla
minha_tupla = (1, 2, 2, 3, 4)
print("Minha tupla", minha_tupla)

print("Minha_tupla[0]:", minha_tupla[0])
print("Minha_tupla[-1]:", minha_tupla[-1]) #Traz o ultimo elemento

# Método count e index
contagem = minha_tupla.count(2)
print("Quantidade de vezes o elemento 2 aparece:", contagem)

indice = minha_tupla.index(3)
print("Indice da primeira ocorrencia do elemento 3:", indice)