import json
import os
MI_RUTA = ''

def new_file(param):
    with open(MI_RUTA, "w") as wf:
        json.dump(param, wf, indent=4)

def open_file():
    with open(MI_RUTA,"r") as rf:
        return json.load(rf)

def AddData(*param):
    with open(MI_RUTA,"r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file.update({param[0]:param[1]})
        else:
            data_file.update({param[0]})
        # data_file[llavePrincipal].update({codigo:info})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)
        rwf.close()

def Eliminar(camper_info, campers):
    if isinstance(camper_info, dict):
        id_number_to_delete = camper_info.get('id_number')
        for i, camper in enumerate(campers):
            if isinstance(camper, dict) and 'id_number' in camper_info and camper_info['id_number'] == id_number_to_delete:
                campers.pop(i)
                return True
    return False


def check_file(*param):
    data = list(param)
    if os.path.isfile(MI_RUTA):
        open_file()
    elif len(param) > 0:
        new_file(data[0])