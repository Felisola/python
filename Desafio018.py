from math import radians, sin, cos, tan
Angulo = float(input('Digite o Angulo que você deseja:'))
seno = sin(radians(Angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(Angulo, seno))
cosseno = cos(radians(Angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(Angulo, cosseno))
tangente = tan(radians(Angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(Angulo, tangente))