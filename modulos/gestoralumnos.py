from tabulate import tabulate
alumno ={}

def AddsStudent(alumnos:dict):
    id = input('Ingrese el id: ')
    nombre = input('Ingrese el nombre: ')
    edad = int (input(f'Ingrese el edad de {nombre}: '))
    email = input(f'Ingrese el email {nombre}: ')
    alumno = {
        'id': id,
        'nombre':nombre,
        'edad':edad,
        'email':email
    }
    alumnos.update({id:alumno}) #UPDATE 4 ACTUALIZAR O AGREGAR EN UN DICCIONARIO
    print(alumno)

def SearchStudent(alumnos:dict):
    id = input('Ingrese el # del id del estudiante: ')
    data = alumnos.get(id,False)
    if(type(data) == dict):
        print(data)
    elif ((type(data) == bool) and (data == False)):
        print('El estudiante no se encuentra registrado')

def LitData(alumnos:dict):
    info =[]
    for key,value in alumnos.items():
        info.append(value)
    print(tabulate(info,headers="keys",tablefmt='grid'))

def ValidateStudent(alumnos : dict)->bool:
    return bool(alumnos.get(id,''))

def DelStudent(alumnos : dict):
    id= input('Ingrese numero edl id del estudiante: ')
    if (ValidateStudent(alumnos,id)):
        alumnos.pop(id)
    else:
        print(f'El estudiante con id {id} no esta registrado')

def DelByName(alumnos :dict):
    nombre = input('Ingrese # id del estudiante: ')
    for llave,valor in alumnos.items():
        if (nombre in valor['nombre']):
            alumnos.pop(llave)
            break
def AddGrades(alumnos : dict):
    notas = {
    'parciales' : [],
    'quices' : [],
    'trabajos' : []
    }
    for key,value in alumnos.items():
        
        value.update({'calificaciones': notas})
        id_alumno = input('Ingrese el ID del alumno al que desea asignar las notas: ')
    estudiante = alumnos.get(id_alumno)
    if estudiante:
        estudiante['calificaciones']['parciales'] = input('Ingrese las notas de parciales separadas por comas: ').split(',')
        estudiante['calificaciones']['quices'] = input('Ingrese las notas de quices separadas por comas: ').split(',')
        estudiante['calificaciones']['trabajos'] = input('Ingrese las notas de trabajos separadas por comas: ').split(',')
        LitData(alumnos)
    else:
        print(f"No se encontró ningún alumno con el ID '{id_alumno}'.")





        