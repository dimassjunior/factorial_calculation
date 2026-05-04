# Importa a biblioteca matemática do Python
import math

# Solicita um número inteiro ao usuário e realiza a conversão (casting)
numero_inteiro = int(input("Digite um número inteiro entre 1 e 10: "))

# Calcula o fatorial utilizando a função da biblioteca math
fatorial_resultado = math.factorial(numero_inteiro)

# Exibe o resultado formatado
print(f"O fatorial de {numero_inteiro} é {fatorial_resultado}.")