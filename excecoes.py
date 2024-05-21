print("Exemplo de captura de excecoes")
try:
    numero = int(input("Digite um numero inteiro: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Tipo de variaveis incopativeis") #manipula o erro.
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}") #executa apenas se deu certo.
finally: 
    print("Operacao finalizada!") #executa independente se deu certo ou errado.