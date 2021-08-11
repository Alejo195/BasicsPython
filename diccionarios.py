def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }

    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])


    población_paises = {
        "Argentina": 44333820,
        "Brasil": 210229338,
        "Colombia": 50338227
    }

    # print(población_paises["Argentina"])

    # for pais in población_paises.keys():
    #     print(pais)

    # for pais in población_paises.values():
    #     print(pais)

    for pais, poblacion in población_paises.items():
        print(pais + " " + str(poblacion))



if __name__ == "__main__":
    run()