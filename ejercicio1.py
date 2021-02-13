frutas={
    'Platano':1.35,
    'Manzana':0.80,
    'Pera':0.85,
    'Naranja':0.70
}
usuarioFruta= input('¿Fruta que desea comprar?')
usuarioKilos= input('¿Cuantos kilos de fruta que desea comprar?')
kilosNumeros = int(usuarioKilos)
if usuarioFruta in frutas:
    print(usuarioKilos+' kilos de '+usuarioFruta+' cuesta '+str(kilosNumeros*frutas[usuarioFruta]))
else:
    print('no hay')
