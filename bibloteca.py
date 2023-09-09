import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def validar_codigo(codigo):
    libro_existe = False
    for libro_unico in libros:
        for key, value in libro_unico.items():
            if value == codigo:
                libro_existe = True
                return libro_existe
                break
    if not libro_existe:
        print("No se encontró libro con ese código.")


def ejemplares_prestados():
    print("EJEMPLARES PRESTADOS")
    for libro in libros:
        if libro['cant_ej_pr'] >= 1:
            print(
                f"El libro '{libro['titulo']}' tiene prestado/s {libro['cant_ej_pr']} ejemplar/es\n")
        else:
            print(
                f"El libro '{libro['titulo']}' no tiene ejemplares prestados\n")
    return None


def registrar_nuevo_libro():
    libro_nuevo = l.nuevo_libro()
    libros.append(libro_nuevo)
    return None


def eliminar_ejemplar_libro():
    print("ELIMINAR EJEMPLAR")
    codigo = str(input("Ingrese el código del libro: "))

    valido = validar_codigo(codigo)

    while not valido:
        codigo = str(input("Ingrese el código del libro: "))
        valido = validar_codigo(codigo)

    for libro in libros:
        if libro['cod'] == codigo:
            libros.remove(libro)
            print("El libro fue eliminado.")
            break
    return None


def prestar_ejemplar_libro():
    print("PRESTAMO DE EJEMPLAR")
    codigo = str(input("Ingrese el código del libro: "))

    valido = validar_codigo(codigo)

    while not valido:
        codigo = str(input("Ingrese el código del libro: "))
        valido = validar_codigo(codigo)

    for libro in libros:
        if libro['cod'] == codigo:
            print(
                f"\nTitulo: {libro['titulo']} \nAutor: {libro['autor']}  \nCantidad de ejemplares disponibles: {libro['cant_ej_ad']}")
            if libro['cant_ej_ad'] > 0:
                confirmacion = str(
                    input("Desea confirmar el prestamo? (Si/No): "))
                if confirmacion.lower() == "si":
                    print("Prestamo confirmado.")
                    libro['cant_ej_pr'] = libro['cant_ej_pr'] + 1
                    libro['cant_ej_ad'] = libro['cant_ej_ad'] - 1
                else:
                    print("Prestamo cancelado.")
            else:
                print("\nNo hay ejemplares disponibles para prestar.")
    return None


def devolver_ejemplar_libro():
    print("DEVOLVER EJEMPLAR")
    codigo = str(input("Ingrese el código del libro: "))

    valido = validar_codigo(codigo)

    while not valido:
        codigo = str(input("Ingrese el código del libro: "))
        valido = validar_codigo(codigo)

    for libro in libros:
        if libro['cod'] == codigo:
            if libro["cant_ej_pr"] > 0:
                print(f"Autor: {libro['autor']}")
                print(f"Título: {libro['titulo']}")
                confirmacion = str(input("Desea confirmar la devolución? (Si/No): "))
                if confirmacion.lower() == "si":
                    print("Devolución confirmada.")
                    libro['cant_ej_pr'] = libro['cant_ej_pr'] - 1
                    libro['cant_ej_ad'] = libro['cant_ej_ad'] + 1
                else:
                    print("Devolución cancelada.")
            else:
                print("El libro no tiene ejemplares prestados")
    return None


"""def nuevo_libro():
    # completar
    return None"""