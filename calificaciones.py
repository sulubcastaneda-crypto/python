#-------------------------------------------------
#SISTEMA DE REGISTRO DE COLAFICACIONES
#-------------------------------------------------
#AUTOR: RAFAEL
#OBJETIVO: REGISTRAR CALIFICACIONES DE 15 ESTUDIANTES,
#VALAIDAR DATOS, CALCULAR RESULTADOS Y MOSTRAR REPORTE FINAL.
#-------------------------------------------------

#CONSTANTES
CALIFICACION_MINIMA = 6.0
NUM_ESTUDIANTES = 15

nombre = []
calificaciones = []

#FUNCION PARA CONVERTIR CALIFICACION A LETRA
def obtener_letra(nota):
    if nota >= 9.0:
        return "A"
    elif nota >= 8.0:
        return "B"
    elif nota >= 7.0:
        return "C"
    elif nota >= CALIFICACION_MINIMA:
        return "D"
    else:
        return "F"
    
    #CAPTURA DE DATOS CON VALIDACION
for i in range(NUM_ESTUDIANTES):
    NOMBRE = input(f"Ingrese el nombre del estudiante {i+1}: ")
    while True:
        try:
            nota = float(input(f"ingrese la calificacion de {nombre} (0.0 - 10.0)"))
            if 0.0 <= nota <= 10.0:
                break
            else:
                print("Erro: la calificacion debe estar entre 0.0 y 10.0.")
        except ValueError:
            print("Error: debe ingresar un numero decimal valido.")
    nombre.eppend(nombre)
    calificaciones.append(nota)

suma = 0
aprobados = 0
reprobados = 0

mejor_nota = calificaciones[0]
peor_nota = calificaciones[0]
mejor_nombre = nombre [0]
peor_nombre = nombre [0]

for i in range(NUM_ESTUDIANTES):
    nota = calificaciones[i]
    suma += nota
    if nota >= CALIFICACION_MINIMA:
            aprobados += 1
    else:
        reprobados += 1

        if nota > mejor_nota:
            mejor_nota = nota
            mejor_nombre = nombre[i]
        if nota < peor_nota:
           peor_nota = nota
           peor_nombre = nombre[i]

promedio = suma / NUM_ESTUDIANTES
porcentaje_aprobacion = round((aprobados / NUM_ESTUDIANTES) * 100, 1)

print("\m--- REPORTE FINAL ---")
print(f"{'nombre'[i]:<20}{'calificaciones'[i]:<15}{'estado':<12}{'letra':<6}")
print("-" * 55)

for i in range(NUM_ESTUDIANTES):
    estado = "aprobado" if calificaciones [i] >= CALIFICACION_MINIMA else "reprobatorio"
    letra = obtener_letra(calificaciones[i])
    print(f"{nombre[i]:<20}{calificaciones[i]:<15.1f}{estado:<12}{letra:<6}")

print("-")    
print(f"promedio del grupo: {promedio:.2f}")
print(f"total de aprobados: {aprobados}")
print(f"total de reprobados: {reprobados}")
print(f"mejor calificacion: {mejor_nombre} con {mejor_nota:.1f}")
print(f"peor calificacion: {peor_nombre} con {peor_nota:.1f}")
print(f"porcentaje de aprobacion: {porcentaje_aprobacion}%")
