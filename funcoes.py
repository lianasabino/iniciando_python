def saudacao(nome):
    print(f"Olá, {nome}!")

print("\n Chamando a função saudacao:")
saudacao("Alice")
saudacao("Bob")

# Funcao com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\n Chamando funcao quadrado:")
resultado_quadrado = quadrado(5)
print("\n Resultado da funcao quadrado:", resultado_quadrado)

# Funcao com multiplos parametros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\n Chamando a funcao soma:")
resultado_soma = soma(20, 50)
print("\n A soma do numero 20 e numero 50 é", resultado_soma)
