# Dicionarios sao coleçoes nao ordenada de pares de chave e valor

# Criando um dicionario
pessoa = {"nome" : "Joao", "idade" : 30, "cidade": "Sao Paulo"}

#Exibindo valores por chave
print("Nome:", pessoa["nome"])

pessoa["sobrenome"] = "Silva" #Adicionar
pessoa["idade"] = 31 #Atualizar
print("Meu dicionario:", pessoa)

#Removendo um par chave-valor
del pessoa["sobrenome"]

# Métodos: keys(), values(), items()
chaves = pessoa.keys()
print("Chaves do meu dicionario:", chaves)

valores = pessoa.values()
print("Valores do meu dicionario:", valores)

itens = pessoa.items()
print("Pares chave_valor do dicionario", itens)

# Para acessar a posição da chave, é necessario transformar o dicionario em lista. Exemplo:
chavesList = list(pessoa.keys())
itensList = list(pessoa.items())
print("Primeira chave:", chavesList[0])
print("Primeira chave-valor: %s = %s" % (itensList[0] [0], itensList[0] [1]))


