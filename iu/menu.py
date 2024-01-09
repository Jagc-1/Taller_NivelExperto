import funciones.campers as c
import os

opciones  = ['Gestor campers', 'Gestor matriculas','Salir']
opCampers = ['Nuevo camper','Borrar camper','Editar camper','Buscar camper','Registro prueba','Registro de áreas de entrenamiento','Estudiantes en riesgo','reportes','Menu principal']


def menuPrincipal() -> int:
    c.cf.check_file(c.campers) #Invocar metodo para verificar si el archivo existe
    os.system('cls')
    header = """
    ***********************************
    * Registro Campers de Campuslands *
    ***********************************
    """
    print(header)
    for i,item in enumerate(opciones):
        print(f'{(i+1)} - {item}')
    while True:
        try:
            return int(input(":)"))
        except ValueError:
            print("Error en el dato ingresado")

def generarCamperMenu():
    isActiveCustomer = True
    header = """
    ******************************
    * ADMINISTRACION DE CAMPERS  *
    ******************************
    """
    while (isActiveCustomer):
        os.system('cls')
        print(header)
        for i,item in enumerate(opCampers):
            print(f'{(i+1)} - {item}')
        try:
            op = int(input(':)_'))
        except ValueError:
            print('Error en el tipo  de dato')
        else:
            if(op == 1):
                os.system('cls')
                title = """
                +++++++++++++++++++++++++++++++++++++
                +      CREACION DE NUEVO CAMPER      +
                +++++++++++++++++++++++++++++++++++++
                """
                print(title)
                c.add_camper()
            elif(op == 2):
                c.del_camper('campers')
            elif(op == 3):
                c.modify_camper("id_number", 'campers')
            elif(op == 4):
                c.search_camper('campers')
            elif(op == 5):
                c.get_camper()
            elif(op == 6):
                c.periodic_evaluation()
            elif(op == 7):
                c.students_at_risk()
            elif(op == 8):
                c.report_data()
            elif(op == 9):
                isActiveCustomer = False
