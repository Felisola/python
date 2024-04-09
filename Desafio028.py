from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que numero eu pensei?')) # O Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Voce acertou, PARABENS')
else:
    print('GANHEI! Eu pensei em um numero {} e nao no {}'.format(computador, jogador))

velocidade = float(input('Qual é a velocidade atual do carro:'))
if velocidade > 80:
    print('MUTADO! Voce excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança')

print("Se beber nao dirija")






