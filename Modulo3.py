from pymongo import MongoClient
from random import randint
from pprint import pprint

client = MongoClient("mongodb://root:12345@localhost:27017/")

def conexion(db):
    return db


def agregarpalabra(db):
    print("introduzca una palabra")
    palabra = input()
    print("introduzca su significado")
    significado = input()
    db.panameno.insert_one({
        'palabra': palabra,
        'significado': significado
    })
    print("Palabra agregada exitosamente.")
    return


def editarpalabra(db):
    print("introduzca la palabra a editar")
    palabra = input();
    print("introduzca su significado")
    significado = input();

    db.panameno.update_one({
        'palabra': palabra
    },{
        '$set': {'significado':significado}
    })

    print("Palabra Actualizada exitosamente.")
    return


def eliminarpalabra(db):
    print("introduzca la palabra a eliminar")
    palabra = input();

    db.panameno.delete_one({
        'palabra': palabra
    })

    print("Palabra eliminada exitosamente.")
    return


def listarpalabras(db):
    records = db.panameno.find()
    for row in records:
        print("id:", row['_id'], " | palabra:", row['palabra'], " | significado:", row['significado'])
    return


def buscarpalabra(db):
    print("introduzca la palabra a buscar")
    palabra = input();
    records = db.panameno.find({'palabra':palabra})
    for row in records:
        print("id:", row['_id'], " | palabra:", row['palabra'], " | significado:", row['significado'])
    return


def main():
    db = conexion(client.pruebas)

    print("Modulo 1");
    print("Menu");
    print("1 - Agregar Palabra");
    print("2  - Editar Palabra");
    print("3  - Eliminar Palabra");
    print("4  - Ver listado de palabra");
    print("5  - Buscar significado");
    print("-----------------------------");
    print("seleccione unas de las opciones anteriores");
    opciones = int(input());

    if opciones == 1:
        print("Vamos agregar una Palabra");
        agregarpalabra(db)

    if opciones == 2:
        print("Vamos a editar una Palabra");
        editarpalabra(db)

    if opciones == 3:
        print("Vamos a eliminar una Palabra");
        eliminarpalabra(db)

    if opciones == 4:
        print("Ver listado de palabra");
        listarpalabras(db)

    if opciones == 5:
        print("Buscar significado");
        buscarpalabra(db)




if __name__ == '__main__':
    main()