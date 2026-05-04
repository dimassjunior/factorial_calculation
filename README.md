# 🔢 Calculadora de Fatorial em Python

Este é um programa simples em Python que calcula o **fatorial de um número inteiro** informado pelo usuário, utilizando a biblioteca padrão `math`.

---

## 📌 Funcionalidades

- Solicita ao usuário um número inteiro
- Calcula o fatorial utilizando a função `math.factorial()`
- Exibe o resultado de forma clara no terminal

---

## 🧮 Conceito de Fatorial

O fatorial de um número inteiro positivo `n` é definido como:

n! = n × (n - 1) × (n - 2) × ... × 1

Exemplos:
- 5! = 5 × 4 × 3 × 2 × 1 = 120  
- 3! = 3 × 2 × 1 = 6  
- 1! = 1  

---

## 💻 Código

```python
# Importa a biblioteca matemática do Python
import math

# Solicita um número inteiro ao usuário e realiza a conversão (casting)
numero_inteiro = int(input("Digite um número inteiro entre 1 e 10: "))

# Calcula o fatorial utilizando a função da biblioteca math
fatorial_resultado = math.factorial(numero_inteiro)

# Exibe o resultado formatado
print(f"O fatorial de {numero_inteiro} é {fatorial_resultado}.")
```

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado
2. Salve o código em um arquivo, por exemplo:

```
fatorial.py
```

3. Execute no terminal:

```
python fatorial.py
```

4. Digite um número inteiro quando solicitado

---

## 📷 Exemplo de Uso

```
Digite um número inteiro entre 1 e 10: 5
O fatorial de 5 é 120.
```

---

## ⚠️ Observações

- O programa espera um número inteiro válido
- Valores negativos não são aceitos pela função `math.factorial()`
- Caso o usuário digite texto ou valores inválidos, ocorrerá erro (`ValueError`)

---

## 🚀 Possíveis Melhorias

- Validar entrada do usuário com `try/except`
- Garantir que o número esteja dentro do intervalo (1 a 10)
- Implementar cálculo manual do fatorial (sem `math`)
- Criar versão com interface gráfica (GUI)

---
