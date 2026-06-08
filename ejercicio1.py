
#este es un comentario
#que ocupa varias lineas

"""
este es un comentario
de comentario multilinea"""

'''
este es otro ejemplo 
de comentario multilinea'''

entero = 42 #numeros enteros
decimal =3.1416 #numeros decimales (float)
logico = True #boolean 
nombre = "sombra177" #string

print(entero)
print(type(decimal))
print(type(logico))
print(type(nombre))

#Declara variables que almacenen su nombre, apellido paterno, apellido materno ,edad, esatatura

nombre = "Diego Rafael"
apellido_paterno = "Sulub"
apellido_materno = "Castaneda"
edad = 18
estatura = 1.75 

print(nombre)
print(apellido_paterno)
print(apellido_materno)
print(edad)
print(estatura)    

#list,tuple,set,dic,arrays,range,frozenset,


nombreMateria = "programacion"
print(nombreMateria[0])
print(nombreMateria[-1])
print(nombreMateria[0:6])

#list - mutable
calificaciones = [8.5,7.5,8.5,7.5,6.5]
calificaciones.append(9.5)
calificaciones[0] = 9.0
print(calificaciones)

#tuple - inmutable
coordenadas = (19.4567 , -99.1234)
print(coordenadas[0])

# dict - clave:valor 
alumno = {"nombre":"Diego","edad":18,"promedio":8.0}
print(alumno["nombre"])
alumno["promedio"] = 8.5
print(alumno)

#crea un diccionario con tuS DATOS: NOMBRE,EDAD Y MATERIA FAVORITA. IMPRIME SOLO TU NOMBRE ACCEDIENDO A LA CLAVE CORRECTAMENTE.
datos_personales = {"nombre":"Diego Rafael","edad":18,"materia_favorita":"programacion"}
print(datos_personales["nombre"])
print(datos_personales["edad"])
print(datos_personales["materia_favorita"])

#escribe un programa que pida al usuario su nombre (str) y su año de nacimiento (int). calcual e imprime su edad aproximada restando el año actual (2026)

nombre_usuario = input("ingresa tu nombre:")
anio_nacimiento = int(input("ingresa tu año de nacimiento:"))
anio_actual = 2026
edad_usuario = anio_actual - anio_nacimiento
print("hola",nombre_usuario,"tu edad proximada es:",edad_usuario)

