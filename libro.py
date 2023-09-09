from cod_generator import generar

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1,
          "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2,
          "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0,
          "titulo": "El código Da Vinci", "autor": "Dan Brown"}


def nuevo_libro():
    print("REGISTRAR NUEVO LIBRO")
    codigo_libro = generar()

    titulo_libro = str(input("\nIngrese el titulo: "))

    autor_libro = str(input("\nIngrese el autor: "))

    cantidad_ejemplares = int(input("\nIngrese la cantidad de ejemplares existentes: "))
    while cantidad_ejemplares < 0:
        print("Por favor ingrese una cantidad valida.")
        cantidad_ejemplares = int(input("\nIngrese la cantidad de ejemplares existentes: "))

    cantidad_ejprestados = int(input("\nIngrese la cantidad de ejemplares prestados: "))
    while cantidad_ejprestados < 0:
        print("Por favor ingrese una cantidad valida.")
        cantidad_ejprestados = int(input("\nIngrese la cantidad de ejemplares prestados: "))

    libro_nuevo = {
        'cod': codigo_libro, 
        'cant_ej_ad': cantidad_ejemplares,
        'cant_ej_pr': cantidad_ejprestados, 
        "titulo": titulo_libro, 
        "autor": autor_libro
        }
    print(f"\nTitulo: {titulo_libro} \nAutor: {autor_libro} \nCodigo: {codigo_libro} \nCantidad de ejemplares existentes: {cantidad_ejemplares} \nCantidad de ejemplares prestados: {cantidad_ejprestados}")
    return libro_nuevo

"""def generar_codigo():
    # completar
    return None"""