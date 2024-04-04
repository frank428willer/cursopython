frase = "O Python é uma linguagem de programação "\
        "multiparadigma. "\
        "Python foi criado por Guido van Rossum."

tamanho_frase = len(frase)
cont = 0
apareceu_mais_vezes = 0
letra_que_mais_apareceu = ''

while cont < tamanho_frase:
        letra_atual = frase[cont]
        
        if letra_atual == ' ':
                cont += 1
                continue

        vezes_letra_apareceu_atual = frase.count(letra_atual)

        if apareceu_mais_vezes < vezes_letra_apareceu_atual:
                apareceu_mais_vezes = vezes_letra_apareceu_atual
                letra_que_mais_apareceu = letra_atual
        
        cont += 1

print(
        'A letra que mais apareceu foi '
        f'"{letra_que_mais_apareceu}" que apareceu '
        f'{apareceu_mais_vezes}x'
)