num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converte para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igula a {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção invalida. Tente novamente.')

