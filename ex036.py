casa = float(input('Qual é o valor da casa:'))
salario = float(input('Salario do comprador:'))
anos = int(input('Quantos anos de financiamneto?'))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' A prestação sera de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')




