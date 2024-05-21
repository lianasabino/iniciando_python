print("Exemplo de importacao de um modulo padrao")
import math 

raiz_quadrada = math.sqrt(25)
print(f"Resultado: {raiz_quadrada}")

# OU

print("Exemplo 2 de importacao de um modulo padrao")
from math import sqrt

raiz_quadrada2 = sqrt(25)
print(f"Resultado: {raiz_quadrada2}")

print("\nExemplo de criacao e utilizacao de um modulo personalizado")
import meu_modulo

mensagem = meu_modulo.saudacao("Liana")
resultado_dobro = meu_modulo.dobro(5)
print(mensagem)
print(f"O dobro de 5 e: {resultado_dobro}")