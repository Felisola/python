peso = float(input('Qual o seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (M)'))
imc = peso / (altura **2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PAREBENS. Você esta na faixa de PESO NORMAL')
elif 25 <= imc <30:
    print('Você esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Você esta em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MORBIDA, cuidado!')
    
