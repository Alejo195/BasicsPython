
def suma(a, b):
    print("se suman dos números")
    resultado = a + b
    return resultado


sumatoria = suma(1, 4)
print(sumatoria)




####

def imprimir_mensaje():
    print("Mensaje Especial")
    print("Estoy aprendiendo a usar funciones")


imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()





#
def conversacion(mensaje):
    print("hola")
    print("cómo estás?")
    print(mensaje)
    print("bye")



opcion = int(input("Elige una opción: "))
if opcion == 1:
    conversacion("Elegiste la opción 1")
elif opcion == 2:
    conversacion("Elegiste la opción 2")

elif opcion == 3:
    conversacion("Elegiste la opción 3 ")

else:
    print("Escribe la opción correcta")