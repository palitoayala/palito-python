# Escribe un programa que cree un diccionario simulando una cesta de compra.
# El programa deve preguntar el articulo y su precio y añadir el par al diccionaro,
# hasta que el usuario decida terminar. Despues se debe mostrar por pantalla la lista
# de compra y el coste total, con el siguiente formato

canasta = {}
continuar = True
while continuar:
    item = input('Introduce un articulo: ')
    precio = float(input('Introduce el precio de '+ item + ': '))
    canasta[item] = precio
    #para continuar se debe escribir si
    continuar = input('¿Quieres añadir articulos a la lista (si/no)? ') == "si"
coste = 0

print('Lista de compra')
for item, precio in canasta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)