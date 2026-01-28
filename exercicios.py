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
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação