#identificadores y variables
#variables con snake_case

#quiero obtener el nombre de un alumno, como debo definir mi identificador
nombre_alumno = "sulub"
edad_alumno = 18
promedio_alumno = 9.5

#constantes con screaming snake case 
TASA_IVA = 0.16
CALIFICACION_MINIMA = 7.0
PESO_PARCIAL = 0.20
PI = 3.1416
GRAVEDAD_PLANETA = 9.84
CAPACIDAD_MAXIMA = 25

#Tipado dinamico - la variable cambia de tipo
dato = 100
print(type(dato))
dato = "cien"
print(type(dato))

#Uso de constantes en un calculo
precio_base = 500.0
precio_final = precio_base * (1 + TASA_IVA)
print(f"precio con IVA: ${precio_final:.2f}")

#Define 3 constantes: peso_parcial=0.20,peso_proyecto=0.40 y calificacion_minima=6.0. luego crea 4 variables con calificaciones y calcula el promecio usando las constantes. imprime si el alumno aporbo o reprobo
PESO_PARCIAL = 0.20
PESO_PROYECTO = 0.40
CALIFICAION_MINIMA = 6.0
calificacion_parcial = 10.0
calificacion_proyecto = 10.0
calificacion_final = (calificacion_parcial + PESO_PARCIAL) + calificacion_proyecto * PESO_PROYECTO
print(f"calificaion final: {calificacion_final:.2f}")
if calificacion_final >= CALIFICACION_MINIMA:
    print("el alumno aprobo") 
else:  print("el alumno reprobo") 
