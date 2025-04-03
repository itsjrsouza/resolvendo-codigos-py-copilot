# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita dois números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita o tipo de operação
operacao = input("Escolha a operação (+, -, *, /): ")

# Executa a operação escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero."
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print("Resultado:", resultado)


# 4️⃣ Verificando Números Pares e Ímpares 🧮
# O programa recebe um número inteiro e verifica se ele é par ou ímpar usando o operador de módulo (%).

# Solicita um número inteiro ao usuário
num = int(input("\nDigite um número inteiro: "))

# Verifica se é par ou ímpar
if num % 2 == 0:
    print("O número é PAR.")
else:
    print("O número é ÍMPAR.")


# 5️⃣ Calculando Média de Notas 📚
# O usuário insere três notas e o programa calcula a média aritmética delas.

# Solicita três notas ao usuário
nota1 = float(input("\nDigite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado formatado para duas casas decimais
print(f"A média das notas é: {media:.2f}")


# 6️⃣ Verificando Palíndromos 🔄
# O programa recebe uma palavra e verifica se ela é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente).

# Solicita uma palavra ao usuário
palavra = input("\nDigite uma palavra: ").strip().lower()

# Compara a palavra original com sua versão invertida
if palavra == palavra[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")