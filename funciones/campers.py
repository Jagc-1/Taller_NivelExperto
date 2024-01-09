import funciones.corefile as cf
import os
import matriculas as mt
campers = []
cf.MI_RUTA = 'data/campers.json'
risk = {}
training_routes = {
    'Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)': [],
    'Programación Web (HTML, CSS y Bootstrap)': [],
    'Programación formal (Java, JavaScript, C#)' : [],
    'Bases de datos (Mysql, MongoDb y Postgresql).': [],
    'Backend (NetCore, Spring Boot, NodeJS y Express)': []
}

def add_camper():
    id_number = int(input("Ingrese el número de identificación: "))
    name = input("Ingrese los nombres: ")
    last_name = input("Ingrese los apellidos: ")
    adress = input("Ingrese la dirección: ")
    estado_inicial = input("Ingrese el estado del camper: ").lower()
    telefono = {
        'telefono': []
    }
    while True:
        phone = {
            "titulo": '',
            "valor": ''
        }
        phone["titulo"] = input("Ingrese ubicación (Casa, Oficina, Móvil): ")
        phone["valor"] = input(f'Ingrese el Nro {phone["titulo"]} del Camper {name}: ')
        telefono["telefono"].append(phone)
        if not input("Para terminar presione Enter... o cualquier letra para continuar"):
            break

    node = ''
    java = ''
    netcore = ''

    camper_info = {
        'id_number': id_number,
        'name': name,
        'last_name': last_name,
        'adress': adress,
        'attendant': {},
        'contact_phone': {},
        'estado_inicial': estado_inicial,
        'estado': '',
        'promedio': '',
        'notas': {
            'Nota_practica': 0,
            'Nota_teorica': 0,
            'otros': 0
        },
        'rutas': {
            'Node Js': node,
            'Java': java,
            'NetCore': netcore
        },
        'info_matricula': {
            'experto_encargado': '',
            'ruta_entrenamiento_asignada': '',
            'fecha_inicio': '',
            'fecha_finalizacion': '',
            'salon_entrenamiento': '',
            'ruta_entrenamiento': '',
            'horario': ''
        }
    }
    camper_info['contact_phone'].update(phone)
    campers.append(camper_info)
    cf.new_file(campers)
    return campers

#funcion para buscar al camper
def search_camper(campers):
    try:
        id_to_search = int(input('Ingrese el Nro Id a Buscar: '))
    except ValueError:
        print("Ingrese un número entero válido.")
        return

    found_camper = None
    for camper in campers:
        if isinstance(camper, dict) and camper.get('id_number') == id_to_search:
            found_camper = camper
            break

    if found_camper is not None:
        print("Camper encontrado:")
        print(found_camper)
    else:
        print(f"No se encontró un camper con el id_number '{id_to_search}'.")

    input("Presione Enter para continuar...")

# Funcion para eliminar un camper
def del_camper(campers):
    id_to_delete = int(input('Ingrese el Nro Id a Eliminar: '))

    new_campers = [camper for camper in campers if isinstance(camper, dict) and int(camper.get('id_number')) != id_to_delete]

    if len(new_campers) < len(campers):
        print("Camper eliminado con éxito.")
        cf.new_file(new_campers)
    else:
        print(f"No se encontró un camper con el id_number '{id_to_delete}'.")


# Funcion para editar un camper
def modify_camper(id_number: str, campers: list):
    print("Lista de campers antes de la búsqueda:", campers)
    id_to_edit = input('Ingrese el Nro Id a Editar: ').strip()
    found_camper = None

    for camper in campers:
        if isinstance(camper, dict) and int(camper.get('id_number')) == int(id_to_edit):
            print("Camper encontrado:", camper)
            found_camper = camper
            break


    if found_camper is not None:
        for key, value in found_camper.items():
            if key != 'id_number':
                user_input = input(f"Desea editar el campo {key} (Enter para Sí, cualquier otra cosa para No): ")
                if user_input != '':
                    new_value = input(f"Ingrese {key.capitalize()} del camper: ")
                    found_camper[key] = new_value

        print("Camper modificado con éxito.")

        # Actualizar el archivo JSON con la lista de campers modificada
        cf.new_file(campers)
    else:
        print(f"No se encontró un camper con el id_number '{id_to_edit}'.")


def get_camper():
    id_number = int(input("Ingrese el número de identificación: "))

    found_camper = None
    for camper in campers:
        if camper['id_number'] == id_number and camper['estado_inicial'] == 'inscrito':
            new_practice_note = float(input("Ingrese el puntaje de la nota práctica: "))
            new_theoretical_note = float(input("Ingrese el puntaje de la nota teórica: "))

            camper['notas']['Nota_practica'] = new_practice_note
            camper['notas']['Nota_teorica'] = new_theoretical_note
            print("Notas ingresadas correctamente.")

            sum_total_notes = new_practice_note + new_theoretical_note
            average_note = sum_total_notes / 2
            camper['promedio'] = average_note

            print(f"Promedio de notas: {average_note}")

            if average_note > 60:
                camper['estado'] = 'aprobado'
            else:
                camper['estado'] = 'rechazado'

            print('El camper ha sido:', camper['estado'])
            found_camper = camper
            break

    if found_camper is None:
        print("No se encontró camper.")

    # Guardar cambios en el archivo JSON después de todas las modificaciones
    cf.new_file(campers)


def Registration_of_training_areas(route_number):
    maxium_capacity = 32

    for camper in campers:
        route = list(training_routes.keys())[route_number]
        if len(training_routes[route]) <= maxium_capacity:
            if camper['estado_inicial'] == 'aprobado' and camper['ruta_entrenamiento'] is None:
                camper['info_matricula']['ruta_entrenamiento'] = route
                training_routes[route].append(camper['id_number'])
        else:
            print(training_routes)
            print("No se pueden agregar más campers a esta ruta.")
            break
    os.system('pause')
    cf.new_file(campers)


def periodic_evaluation():
    id_number = int(input("Ingrese el número de identificación: "))

    for camper in campers:
        print(camper)
        os.system('pause')
        if camper['id_number'] == id_number and camper['estado'] == 'aprobado':
            new_practice_note = float(input("Ingrese el puntaje de la nota práctica: "))
            new_theoretical_note = float(input("Ingrese el puntaje de la nota teórica: "))
            new_others_notes = float(input("Ingrese el puntaje del trabajo o quiz: "))

            print('antes: ', camper['notas'])
            camper['notas']['Nota_practica'] = new_practice_note * 0.6
            camper['notas']['Nota_teorica'] = new_theoretical_note * 0.3
            camper['notas']['otros'] = new_others_notes * 0.1
            print("Notas ingresadas correctamente.")
            print('Después: ', camper['notas'])

            sum_total_notes = new_practice_note + new_theoretical_note + new_others_notes
            average_note = sum_total_notes // 3
            camper['promedio'] = average_note
            print(f"Promedio de notas: {average_note}")

            if average_note > 60:
                camper['estado'] = 'aprobado'
            else:
                camper['estado'] = 'rechazado'

            print('El camper ha sido: ', camper['estado'])
            os.system('pause')
            
            # Llamada para guardar los cambios en el archivo JSON
            cf.new_file(campers)
            
            break
    else:
        print("No se encontró un camper con la identificación y estado especificados.")


def students_at_risk():
    for camper in campers:
        if camper['promedio'] < 60:
            risk.update({camper['name']: camper['id_number']})

    show_data(risk)
    os.system('pause')
    cf.new_file(campers)  


def show_data(risk):
    if not risk:
        print("El diccionario está vacío.")
        return

    max_longitud_clave = max(map(len, risk.keys()))

    for clave, valor in risk.items():
        print(f"{clave.ljust(max_longitud_clave)} : {valor}")



def report_data():
    menu = """
    1. Listar los campers que se encuentren en estado de inscrito.
    2. Listar los campers que aprobaron el examen inicial.
    3. Listar los entrenadores que se encuentran trabajando con campuslands.
    4. Listar los estudiantes que cuentan con bajo rendimiento.
    5. Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.
    6. Mostrar cuántos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.
    7. Salir
    """
    while True:
        print(menu)
        opcion = input("Ingrese el número de la opción deseada (o '7' para salir): ")

        if opcion == '1':
            print("Listar campers en estado de inscrito:")
            for camper in campers:
                if camper['estado_inicial'] == 'inscrito':
                    print(camper)
            os.system('cls')

        elif opcion == '2':
            print("Listar campers que aprobaron el examen inicial:")
            for camper in campers:
                if camper['estado_inicial'] == 'aprobado':
                    print(camper)
            os.system('cls')
            
        elif opcion == '3':
            print("Listar entrenadores que trabajan con campuslands:")
            print(mt.trainers)
        elif opcion == '4':
            print("Listar estudiantes con bajo rendimiento:")
            for camper in campers:
                if camper['promedio'] < 60:
                    print(camper)
        elif opcion == '5':
            print("Listar campers y entrenador asociados a una ruta de entrenamiento:")
        elif opcion == '6':
            print("Mostrar cuántos campers perdieron y aprobaron cada módulo:")
        elif opcion == '7':
            print("Saliendo del menú.")
            break
        else:
            print("Opción no válida. Ingrese un número del 1 al 7.")

