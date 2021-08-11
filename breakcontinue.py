def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break


    # texto = input("Escribe un texto: ")
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra)


    numero = int(input("Escribe un número uno para multiplicar: "))
    multiplicador = 1
    resultado = multiplicador * numero

    while resultado < 500:
        if resultado == 417:
            break
        resultado = resultado + 1
        print(int(resultado) * int(multiplicador))
    

if __name__ == "__main__":
    run()