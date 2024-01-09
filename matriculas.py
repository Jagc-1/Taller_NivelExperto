import funciones.campers as campers
import funciones.corefile as cf
import os

trainers = {
        'trainer_A': [
            'Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)',
            'Programación Web (HTML, CSS y Bootstrap)'
        ],
        'trainer_B': [
            'Programación Web (HTML, CSS y Bootstrap)',
            'Programación formal (Java, JavaScript, C#)',
        ],
        'trainer_C': [
            'Bases de datos (Mysql, MongoDb y Postgresql).',
            'Backend (NetCore, Spring Boot, NodeJS y Express)'
        ],
    }


def registration_manager():
    horario_final = ''
    id_number = int(input("Ingrese el número de identificación: "))
    salon_entrenamiento = input('Ingrese el salon asignado: ')
    training_areas = int(input('que area le desea inscribir : \n1.Fundamentos de programación\n2.Programación Web\n3.Programación formal\n4.Bases de datos\n5.Backend\n'))
    trainer = str(input("Escoja un trainer [A - B - C]: ")).lower()
    ruta_entrenamiento = input('que area le desea inscribir (NetCore,Nodejs,Java): ').lower()
    horario = int(input("Escoje un numero para el horario [1.mañana - 2.tarde]: "))
    fechaInicio = input("Ingrese la fecha de inicio (formato DD/MM/AAAA): ")
    fechaFin = input("Ingrese la fecha de finalización (formato DD/MM/AAAA): ")
    registration_of_training_areas(training_areas, id_number)

    for camper in campers.campers:
         if camper['id_number'] == id_number and camper['estado'] == 'aprobado' and camper['info_matricula']['ruta_entrenamiento'] is not None:
            camper['info_matricula']['experto encargado'] = trainer
            camper['info_matricula']['salon de entrenamiento'] = salon_entrenamiento
            camper['info_matricula']['ruta_entrenamiento'] = ruta_entrenamiento
            if horario == 1:
                horario_final = 'mañana'
            elif horario == 2:
                horario_final = 'tarde'
            else:
                print('solo se puede ingresar los numeros 1 para mañana y 2 para tarde')

            camper['info_matricula']['horario'] = horario_final
            camper['info_matricula']['fecha de inicio'] = fechaInicio
            camper['info_matricula']['fecha finalizacion'] = fechaFin
            print(f'Se ha matriculado al camper con ID {id_number} en la ruta {camper["info_matricula"]["ruta_entrenamiento"]}.')
            print('Información de matrícula actualizada:', camper['info_matricula'])
            os.system('pause')

    else:
        print('No se encontró el camper')
        cf.new_file(campers.campers)



#Function for register campers notes
def registration_of_training_areas(route_number, id_number):
    maxium_capacity = 32
    route_number -= 1

    route = list(campers.training_routes.keys())[route_number]
    for camper in campers.campers:
        if len(campers.training_routes[route]) <= maxium_capacity:
            print(camper['info_matricula']['ruta_entrenamiento'])
            if camper['id_number'] == id_number and camper['estado'] == 'aprobado' and camper['info_matricula']['ruta_entrenamiento']  is None:
                camper['info_matricula']['ruta_entrenamiento'] = route
                campers.training_routes[route].append(camper['id_number'])
                os.system('pause')
    else:
        print("No se pueden agregar más campers a esta ruta.")
        os.system('pause')

    cf.new_file(campers.campers)

