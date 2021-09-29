import os

# Variables goblales
CARPETA = 'contactos/'

def app():
    # Revisa si la carpeta existe, sino la crea
    crear_directorio()
    # Muestra el menu de opciones
    mostrar_menu()
    # Preguntar al usuario
    preguntar = True
    while preguntar:
        opt = input('Seleccione una opcion: \r\n')
        opt = int(opt)

        if opt == 1:
            print('Agregar contacto')
            agregar_contacto()
            mostrar_menu()
        elif opt == 2:
            print('Modifica contacto')
            editar_contacto()
            mostrar_menu()
        elif opt == 3:
            print('Ver contacto')
            mostrar_contacto()
            mostrar_menu()
        elif opt == 4:
            print('Buscar contacto')
            buscar_contacto()
            mostrar_menu()
        elif opt == 5:
            print('Borrar contacto')
            eliminar_contacto()
            mostrar_menu()
        elif opt == 6:
            print('Cerraste la aplicacion, escribe en la consola "python proyecto.py" si quieres reiniciarla')
            preguntar = False
        else:
            print('Esa opcion no existe')
    


def eliminar_contacto():
    nombre = input('Escriba el nombre del contacto que desea eliminar: \r\n')


def buscar_contacto():
    nombre = input('Escriba el nombre del contacto que desea buscar: \r\n')


def mostrar_contacto():
    archivos = os.listdir(CARPETA)


def editar_contacto():
    print('Escribe el nombre del contacto')


def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto:')

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)


def mostrar_menu():
    print('Selecciones del menu:')
    print('1 - Agregar contacto')
    print('2 - Modifica contacto')
    print('3 - Ver contacto')
    print('4 - Buscar contacto')
    print('5 - Borrar contacto')
    print('6 - Salir')


app()