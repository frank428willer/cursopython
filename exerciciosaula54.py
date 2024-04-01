"""
faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. caso o usuario não digite um
numero inteiro, informe que não é um numero inteiro
"""

numero_str = input('Digite um numero Inteiro: ')

try:
    numero_int = int(numero_str)
    numero_par = numero_int % 2


    if numero_par == 0:
        print(f'o numero {numero_int} é par')
    else:
        print(f'o numero {numero_int} é impar')
except:
    print(f'o caracter [{numero_str}] que voce digitou não é um numero inteiro!!')



"""
faça um programa que pergunte a hora ao usuario e baseando-se no horario
descrito, exiba a saudação apropriada. ex
bom dia 0-11, boa tarde 12-17 e boa noite 18-23
"""

hora_atual = input('Digite o Horario atual: ')

hora_int = int(hora_atual[:2])

if hora_int >= 00 and hora_int <= 11:
    print (f'São {hora_atual} Bom dia !!')
elif hora_int >= 12 and hora_int <= 17:
    print (f'São {hora_atual} Boa tarde !!')
else:
    print(f'são {hora_atual} Boa Noite!!')



"""
faça um programa que peça o primeiro nome do usuario. se o nome tiver 4
letras ou menos escreva "seu nome é curto", se tiver entre 5 e 6 letras,
escreva "seu nome é normal", maior que 6 escreva "seu nome é muito grande"
"""

nome = input('Digite seu primeiro nome: ')

tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print(f'Seu nome {nome} é curto')
elif tamanho_nome > 4 and tamanho_nome <= 6:
    print(f'seu nome {nome} é normal')
elif tamanho_nome >6:
    print(f'seu nome {nome} é muito grande')