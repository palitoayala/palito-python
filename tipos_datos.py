# esto es una lista
dias_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

#imprimir los datos de una lista con for
print("Dias de la semana")
for dia in dias_semana:
    print(dia)

#Esto es un diccionario de alumnos con sus calificaciones
calificaciones = {
    "Pepe":[2,4,5],
    "Juan": [3,4,4],
    "Moisés":[4,3,5]
}
print("Lista de alumnos")
for c in calificaciones:
    print(c)

print("lista de alumnos con sus calificaciones")
for c in calificaciones:
    print(c, ' : ', calificaciones[c])

print("Lista de alumnos y promedio de calificaciones")
for c in calificaciones:
    print(c)
    suma = 0
    for i in calificaciones[c]:
        suma += i
    print('prom: {0}'.format((suma/len(calificaciones[c]))))

#tuplas, semejante a las listas pero inmutables
print("Meses del año")
meses = ('Enero','Febrero','Marzo','Abril','Mayo')
for mes in meses:
    print(mes)

#otra lisra, y los métodos de las listas
precios = [4500,1200,3600,8000]

print(precios)
#agregar elementos a la lista
precios.append(900)
print(precios)
#quitar elementos segun posicion
precios.remove(1200)
print(precios)
#quitar el ultimo elemento
print(precios.pop())
print(precios)

