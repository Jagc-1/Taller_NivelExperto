import os
import json
import iu.menu as mn
import funciones.campers as c
import funciones.corefile as cf
import matriculas as mat

limpiar_pantalla = lambda : os.system("cls")
info = ''
camper = None
cf.MI_RUTA = 'data/campers.json'


if __name__ == '__main__':
    while True:
        opMainMenu = 0
        limpiar_pantalla()
        try:
            opMainMenu = mn.menuPrincipal()
        except ValueError:
            print("Error en el dato de ingreso")
            input("Presione Enter para continuar...")
        else:
            if(opMainMenu == 1):
                mn.generarCamperMenu()
            elif (opMainMenu == 2):
                mat.registration_manager()
            elif (opMainMenu == 3):
                print("¡Hasta luego!. Gracias Por Visitarnos")
                break
