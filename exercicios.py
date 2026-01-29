import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# num_01 = input("Insira o primeiro número inteiro: ")
# num_02 = input("Insira o segundo número inteiro: ")
# soma = int(num_01) + int(num_02)
# print(soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# num_01 = input("Insira um número: ")
# resto = int(num_01) % 5
# print(f'O resto da divisão de {num_01} por 5 é: {resto}')

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.


# num_01 = input("Insira o primeiro número inteiro: ")
# num_02 = input("Insira o segundo número inteiro: ")
# resultado = int(num_01) * int(num_02)
# print(resultado)


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero_01 = int(input("Inserir um numero inteiro: "))
# numero_02 = int(input("Inserir outro numero inteiro: "))
# resultado = numero_01 // numero_02
# print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# num_01 = input("Insira o primeiro número: ")
# quadrado = int(num_01) ** 2
# print(quadrado)


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# num_01 = input("Insira um número flutuante: ")
# num_02 = input("Insira o segundo número flutuante: ")
# soma = float(num_01.replace(',', '.')) + float(num_02.replace(',', '.'))
# print(soma)


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# num_01 = input("Insira um número flutuante: ")
# num_02 = input("Insira o segundo número flutuante: ")
# media = (float(num_01.replace(',', '.')) + float(num_02.replace(',', '.'))) / 2
# print(f"a media dos valores é: {media}")
 

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).


# base = input("Informe a base de uma potência: ")
# exp = input("Insira o expoente do cálculo: ")
# resultado = float(base.replace(',', '.')) ** float(exp.replace(',', '.'))
# print(f"O resultado da potência é: {resultado}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# temp_celsius = input("Informe a temperatura em Celsius: ").replace(',', '.')
# temp_fahrenheit = (float(temp_celsius) * 9/5) + 32
# print(f"{temp_celsius}ºC em Fahrenheit é: {temp_fahrenheit:.1f}")



# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio = float(input("Insira o raio do círculo: "))
# area = math.pi * (raio ** 2)
# print(f"A área do círculo é: {area:.2f}")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# string = input('Escreva o texto que quiser: ')
# string_maiuscula = string.upper()
# print(string_maiuscula)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome_completo = input("Insira seu nome completo: ")
# nome_minusculo = nome_completo.lower()
# print(nome_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Escreva uma frase:: ")
# frase_sem_espacos = frase.strip()
# print(frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Insira uma data no formato dd/mm/aaaa: ")
# dia, mes, ano = data.split("/")
# print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# str_01 = input("Coloque seu nome: ")
# str_02 = input("Coloque seu sobrenome: ")
# nome_concatenado = str_01 + " " + str_02
# print(f"Seu nome completo é: {nome_concatenado}")



# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# valor1 = input("Insira o primeiro valor booleano (True/False): ")
# valor2 = input("Insira o segundo valor booleano (True/False): ")
# resultado_and = valor1 and valor2
# print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# valor1 = input("Insira o primeiro valor booleano (True/False): ")
# valor2 = input("Insira o segundo valor booleano (True/False): ")
# resultado_or = valor1 or valor2
# print("Resultado do OR lógico:", resultado_or)


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# valor1 = input("Insira o primeiro valor booleano (True/False): ")
# valor_invertido = not valor1
# print("Valor invertido:", valor_invertido)


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# num_01 = input("Insira o primeiro número: ")
# num_02 = input("Insira o segundo número: ")
# sao_iguais = num_01 == num_02
# print(f"Os números são iguais? {sao_iguais}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# num_01 = input("Insira o primeiro número: ")
# num_02 = input("Insira o segundo número: ")
# sao_diferentes = num_01 != num_02
# print(f"Os números são diferentes? {sao_diferentes}")

# #### try-except e if

# 21: Conversor de Temperatura

# escolha = input(
#      "Escolha a conversão de temperatura:\n"
#      "1. Celsius para Fahrenheit\n"
#      "2. Fahrenheit para Celsius\n"
#      "Digite 1 ou 2: ")

# if escolha not in ('1', '2'):
#         print("Opção inválida. Por favor, escolha 1 ou 2.")
#         exit()
# try:
#     if escolha == '1':
#         celsius = input("Insira a temperatura em celsius: ")
#         celsius = float(celsius.replace(',', '.'))
#         fahrenheit = (celsius * 9/5) + 32
#         print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
#     else:
#         fahrenheit = input("Insira a temperatura em fahrenheit: ")
#         fahrenheit = float(fahrenheit.replace(',', '.'))
#         celsius = (fahrenheit - 32) * 5/9
#         print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
# except ValueError:
#     print("Entrada inválida. Por favor, insira um número válido para a temperatura.")

# 22: Verificador de Palíndromo

# print("Seja bem-vindo ao verificador de palíndromos!")

# entrada = input("\n Informe a palavra ou frase que deseja verificar: ")
# if isinstance(entrada, str):
#     string_limpa = entrada.strip().lower().replace(" ", "")
#     string_invertida = string_limpa[::-1]
#     if string_limpa == string_invertida:
#         print(F"\n O objeto informado é um palíndromo!")
#     else:
#         print(F"\n O objeto informado não é um palíndromo!")
# else:
#     print("\n Entrada inválida. Por favor, insira uma palavra ou frase válida.")
    

# 23: Calculadora Simples

# print("Seja bem-vindo à calculadora simples!")

# num_01 = input("\n Insira o primeiro número: ")
# num_02 = input("Insira o segundo número: ")
# operacao = input("Escolha a operação (+, -, *, /): ")
# try:
#     numero_01 = float(num_01.replace(',', '.'))
#     numero_02 = float(num_02.replace(',', '.'))

#     if operacao == '+':
#         resultado = numero_01 + numero_02
#     elif operacao == '-':
#         resultado = numero_01 - numero_02
#     elif operacao == '*':
#         resultado = numero_01 * numero_02
#     elif operacao == '/':
#         if numero_02 != 0:
#             resultado = numero_01 / numero_02
#         else:
#             print("Erro: Divisão por zero não é permitida.")
#             exit()
#     else:
#         print("Operação inválida. Por favor, escolha entre +, -, *, /.")
#         exit()

#     print(f"O resultado de {numero_01} {operacao} {numero_02} é: {resultado}")
# except ValueError:
#     print("Entrada inválida. Por favor, insira números válidos.")


# 24: Classificador de Números

# print("Seja bem-vindo ao classificador de números inteiros!")

# entrada = input("\n Insira um número inteiro: ")
# try:
#     numero = int(entrada)
#     if numero > 0:
#         print(f"\n O número {numero} é positivo.")
#     elif numero < 0:
#         print(f"\n O número {numero} é negativo.")
#     else:
#         print(f"\n O número é zero.")
#     if numero % 2 == 0:
#         print(f"\n O número {numero} é par.")
#     else:
#         print(f"\n O número {numero} é ímpar.")
# except ValueError:
#     print("\n Entrada inválida. Por favor, insira um número inteiro válido.")


# 25: Conversão de Tipo com Validação

# print("Seja bem-vindo ao conversor de tipos com validação!")

# entrada = input("\n Insira uma lista de números separados por vírgulas: ")
# valores_str = entrada.split(",")
# lista_valores = []
# try:
#     for num in valores_str:
#         lista_valores.append(int(num.strip()))
#     print(f"\n A lista convertida para inteiros é: {lista_valores}")
# except ValueError:
#     print("\n Entrada inválida. Por favor, insira números válidos separados por vírgulas.")



