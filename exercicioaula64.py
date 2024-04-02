nome = 'frank willer'
tamanho_nome = len(nome)
novo_nome = ''
contador = 0

while contador < tamanho_nome:
    letra = (f'*{nome[contador]}*')
    novo_nome += letra
    contador += 1

print(novo_nome)