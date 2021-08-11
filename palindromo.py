palabra = str(input("Ingresa una palabra para saber si es o no un palíndromo: "))
palabra = palabra.lower().replace(" ", "")
palabrados = palabra
palabrados = palabrados[::-1]

if palabra.strip() == palabrados:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")



    #def es_palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    
    if palabra[::] == palabra[::-1]:
        return True
    
    else:
        return False


def run():
    palabra = input('Ingrese una palabra: ')
    if es_palindromo(palabra):
        print('Es palindromo')

    else:
        print('No es palindromo')


if __name__ == "__main__":
    run()