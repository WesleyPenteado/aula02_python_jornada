# Desafio Aula 02 - Refatorar evitando bugs

print("Bem-vindo ao sistema de cálculo de bônus salarial! \n" )

# Nome de usuário e tratamento de erros em caso de entrada inválida
nome = input("Digite seu nome: ")

if nome.isdigit():
    print("Erro: O nome não pode conter números. Por favor, insira um nome válido.")
    exit()
elif len(nome) == 0:
    print("Erro: O nome não pode ser vazio. Por favor, insira um nome válido.")
    exit()
if nome.isspace():
    print("Erro: Você digitou só espaço. Por favor, insira um nome válido.")
    exit()

#Informe salário somente em números (Não permite textos)
try:
    salario = float(input("Digite o valor do seu salário: ").replace(',', '.'))

except ValueError:
    print("Erro: Por favor, insira um valor numérico válido para o salário.")
    exit()


#Informe bônus e não permite que seja menor que zero
try:
    bonus = float(input("Digite o valor do seu bônus : "))
    if bonus < 0:
        print("Erro: O bônus não pode ser negativo. Por favor, insira um valor válido.")
        exit()
except ValueError:
    print("Erro: Por favor, insira um valor numérico válido para o bônus.")

constante_bonus = 1000
valor_total = (float(salario) * float(bonus)) + float(constante_bonus)
bonus_liquido = valor_total - salario

print(f"\n Olá {nome}, o seu salário foi de R$ {salario:.2f} e seu bônus foi de R$ {bonus_liquido:.2f}, totalizando R$ {valor_total:.2f}!")
