time = ('Botafogo', 'Aletico-MG', 'Bragantino', 'Athletico-PR', 'Bahia', 'Internacional',
        'Cruzeiro', 'Flamengo', 'Grêmio', 'Criciuma', 'Fortaleza', 'Juventude', 'Corinthians',
        'Palmeiras', 'Fluminense', 'São Paulo', 'Vasco', 'Vitória', 'Atlético-GO', 'Cuiabá')
print('-=' * 20)
print(f' Os 5 primeiros times são {time[0:5]}')
print('-=' * 20)
print(f' Os ultimos 4 colocados são {time[-4:]}')
print('-=' * 20)
print(f' times em ordem alfabética {sorted(time)}')
print('-=' * 20)
print(f'O Flamengo esta na {time.index("Flamengo")+1} posição')