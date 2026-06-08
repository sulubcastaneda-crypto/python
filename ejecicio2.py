# casting basico
#implicita: int + float = float automaticamente
resultado = 5 + 2.0
print(resultado)
print(type(resultado))

#emplicita: str a int
texto_numero = "42"
numero = int(texto_numero)
print(numero) 

#explicita: int a str para concatenar
edad = 18
mesanje = "hola, soy Sulub y mi edad es " + str(edad)
print(mesanje)

#float a int
precio = 9.99
print(int(precio))

numero = 7.99
redondeado = round(numero)
print(redondeado)

# simularemos input con variables fijas
dato_usuario = "25"
print(type(dato_usuario))
#print(dato_usuario + 5)

edad_correcta = int(dato_usuario)
print(edad_correcta + 5)

#patron correcto para la entrada de datos:
edad = int(input("Ingrese su edad: "))
