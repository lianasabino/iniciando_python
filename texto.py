# Declaração

nome_completo = "Liana Sabino"

nome_completo_aspas = """Liana
Sabino"""

nome_completo_quebra = "Liana \
Sabino"

nome = "Liana"
Sobrenome = "Sabino"

# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Liana", "Sabino" )
print("Nome completo (4a forma): %s" % nome_completo)
print("Nome completo (5a forma): %s %s" % (nome, Sobrenome))
print(f"Nome completo (6a forma): {nome} {Sobrenome}")
print("Nome completo (7a forma): {} {}".format(nome, Sobrenome))

# Operadores lógicos: and e or

