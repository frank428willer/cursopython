numero = '5456464'
string1 =''
for teste in numero:
    print(f'{teste}')
    string1 += f'*{teste}* '

print(string1)



#para utilizar for com numero
#necessario setar um range na variavel inteira
#range (numero inicial, numero final, quantidade de passos)
#range iniciando de 0 ao numero setado não conta o ultimo numero por 
#se tratar de indice.

numeros = range(15)

for numero in numeros:
    print(numero)