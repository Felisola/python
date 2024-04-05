'''co = float(input('Cumprimento do cateto oposto:'))
ca = float(input('Cumprimento do cateto adijacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai merdir {:.2f}'.format(hi))'''
from math import hypot
co = float(input('Cumprimeito do cateto oposto:'))
ca = float(input("Cumprimento do cateto adijacente:"))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(hi))

