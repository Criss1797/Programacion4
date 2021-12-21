import pymysql
import sqlalchemy as db
engine = db.create_engine('mysql+pymysql://root:12345@localhost/pruebas?charset=utf8mb4')

def conexion(db):
    connection = engine.connect()
    return connection

def agregarpalabra(conn):
    
    print("introduzca una palabra")
    palabra = input();
    print ("introduzca su significado")
    significado = input();
    metadata = db.MetaData()
    panameno = db.Table('panameno', metadata, autoload=True, autoload_with=engine)
    query = db.insert(panameno).values(palabra=palabra, significado=significado) 
    ResultProxy = conn.execute(query)
    print ("Palabra agregada exitosamente.")
    return ResultProxy

def editarpalabra(conn):
    print ("introduzca la palabra a editar")
    palabra = input();
    print ("introduzca su significado")
    significado = input();
    
    metadata = db.MetaData()
    panameno = db.Table('panameno', metadata, autoload=True, autoload_with=engine)
    query = db.update(panameno).values(significado=significado) 
    query = query.where(panameno.columns.palabra == palabra)
    ResultProxy = conn.execute(query)
    print ("Palabra Actualizada exitosamente.")
    return ResultProxy
   
def eliminarpalabra(conn):
    print ("introduzca la palabra a eliminar")
    palabra = input();
    
    metadata = db.MetaData()
    panameno = db.Table('panameno', metadata, autoload=True, autoload_with=engine)
    query = db.delete(panameno);
    query = query.where(panameno.columns.palabra == palabra)
    ResultProxy = conn.execute(query)
    print ("Palabra eliminada exitosamente.")
    return ResultProxy

def listarpalabras(conn):
    metadata = db.MetaData()
    panameno = db.Table('panameno', metadata, autoload=True, autoload_with=engine)
    query = db.select([panameno]) 
    ResultProxy = conn.execute(query)
    records = ResultProxy.fetchall()
    for row in records:
        print ("id:", row [0]," | palabra:", row [1], " | significado:", row [2])
    return ResultProxy

def buscarpalabra(conn):
    print ("introduzca la palabra a buscar")
    palabra = input();
    metadata = db.MetaData()
    panameno = db.Table('panameno', metadata, autoload=True, autoload_with=engine)
    query = db.select([panameno]) 
    query = query.where(panameno.columns.palabra == palabra)
    ResultProxy = conn.execute(query)
    records = ResultProxy.fetchall()
    for row in records:
        print ("significado:", row [2])
    return ResultProxy

def main():
    database = db
    conn = conexion(database)
    
    print ("Modulo 1");
    print ("Menu");
    print ("1 - Agregar Palabra");
    print ("2  - Editar Palabra");
    print ("3  - Eliminar Palabra");
    print ("4  - Ver listado de palabra");
    print ("5  - Buscar significado");
    print ("-----------------------------");
    print ("seleccione unas de las opciones anteriores");
    opciones = int(input());

    with conn:

        if opciones == 1:
            print ("Vamos agregar una Palabra");
            agregarpalabra(conn)

        if opciones == 2:
            print ("Vamos a editar una Palabra");
            editarpalabra(conn)

        if opciones == 3:
            print ("Vamos a eliminar una Palabra");
            eliminarpalabra(conn)

        if opciones == 4:
            print ("Ver listado de palabra");
            listarpalabras(conn)

        if opciones == 5:
            print ("Buscar significado");
            buscarpalabra(conn)
    
        
        

if  __name__ == '__main__':
    main()

