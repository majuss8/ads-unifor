# 1  ALGORTIMO verifica_par_impar

# numero = int(input("Digite um número: "))

# if numero >= 0:
#     resto = numero % 2

#     if resto == 0:
#         print("O número informado é par!")

#     else:
#         print("O número informado é ímpar!")

# else:
#     print("O número deve ser postivo!")

#####################################################################

# 2 Algoritmo novo_salario

# salario = float(input("Informe seu salário: "))

# if salario >= 0:

#     if salario <= 500:
#         salario =+ salario + (salario * 0.20)
#         print(f'O novo salário será de R$ {salario:.2f}')

#     else:
#         salario =+ salario + (salario * 0.10)
#         print(f'O novo salário será de R$ {salario:.2f}')

# else:
#     print("O valor deve ser postivo!")

#####################################################################

# 3 Algoritmo media_notas

# nota1 = float(input("Informe a nota 1: "))
# nota2 = float(input("Informe a nota 2: "))

# if nota1 >= 0 and nota2 >= 0:
#     media = (nota1 + nota2) / 2

#     if media <= 6:
#         print(f'A média do(a) aluno(a) foi: {media:.1f}, logo ele(a) foi REPROVADO(A)')

#     else:
#         print(f'A média do(a) aluno(a) foi: {media:.1f}, logo ele(a) foi APROVADO(A)')

# else: 
#     print("Informe valores positivos!")

#####################################################################

# 4 Algoritmo idade_cnh

# idade = int(input("Informe sua idade: "))

# if idade >= 0:
#     if idade < 18:
#         tempoRestante = 18 - idade
#         print(f'O candidado não está apto para tirar a CNH, ainda falta(m) {tempoRestante} ano(s) para tirar')
    
#     else:
#         print("O candidato está apto para tirar a CNH")

# else:
#     print("A idade deve ser um valor postivo!")