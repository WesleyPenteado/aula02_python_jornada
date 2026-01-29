# Desafio Aula 02 - Refatorar evitando bugs

print("Bem-vindo ao sistema de cálculo de bônus salarial! \n" )

nome = input("Digite seu nome: ")

# Verificando erros na string
if nome.isdigit():
    print("Erro: O nome não pode conter números. Por favor, insira um nome válido.")
    exit()
elif len(nome) == 0:
    print("Erro: O nome não pode ser vazio. Por favor, insira um nome válido.")
    exit()
if nome.isspace():
    print("Erro: Você digitou só espaço. Por favor, insira um nome válido.")
    exit()


salario = input("Digite o valor do seu salário: ")
bonus = input("Digite o valor do seu bônus : ")
constante_bonus = 1000

valor_total = float(salario) * float(bonus) + float(constante_bonus)

print(f"\n Olá {nome}, o seu bônus foi de R$ {valor_total}")
