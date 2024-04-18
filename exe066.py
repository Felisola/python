soma = cont = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos valores foi de {soma}')
print(f'E a quantidade de numeros digitados foi {cont}')

