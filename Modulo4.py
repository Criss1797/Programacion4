import redis

def agregarpalabra(client):
    print("introduzca una palabra")
    palabra = input()
    print("introduzca su significado")
    significado = input()
    client.hset('panameno',palabra,significado)
    print("Palabra agregada exitosamente.")
    return


def editarpalabra(client):
    print("introduzca la palabra a editar")
    palabra = input()
    print("introduzca su significado")
    significado = input();

    client.hset('panameno',palabra,significado)

    print("Palabra Actualizada exitosamente.")
    return


def eliminarpalabra(client):
    print("introduzca la palabra a eliminar")
    palabra = input();

    client.delete('panameno:'+palabra)

    print("Palabra eliminada exitosamente.")
    return


def listarpalabras(client):
    records = client.hgetall('panameno')
    for row in records:
        print('palabra: '+row.decode("utf-8") +' |  significado:'+records[row].decode('utf-8'))
    return


def buscarpalabra(client):
    print("introduzca la palabra a buscar")
    palabra = input();
    signficado = client.hget('panameno', palabra)
    print("palabra:", palabra, " | significado:", signficado.decode('utf-8'))
    return


def main():
    # connect to redis
    client = redis.Redis(host='localhost', port=6379)
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
        agregarpalabra(client)

    if opciones == 2:
        print("Vamos a editar una Palabra");
        editarpalabra(client)

    if opciones == 3:
        print("Vamos a eliminar una Palabra");
        eliminarpalabra(client)

    if opciones == 4:
        print("Ver listado de palabra");
        listarpalabras(client)

    if opciones == 5:
        print("Buscar significado");
        buscarpalabra(client)




if __name__ == '__main__':
    main()
