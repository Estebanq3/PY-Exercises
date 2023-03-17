#ESPECIFICACIONES
# USB -> TXT
# al iniciar el bootloader se cargan las instrucciones del sistema operativo que se seleccionó 


#Simular una ram mediante un vector
#Se debe contar con un menú para el group que estamos mencionando, simulación me permita escoger si
#quiero cargar un linux o un windows, sólo nos permite cargar uno a la vez
#Tambien necesitamos una opción de cargar desde un CD o un dispositvio externo
#Asimismo también está el modo mantenimiento
#RAM y almacenamiento fallan si no se logro cargar correctamente SO e info o así

#En primer lugar la RAM debe comenzar vacía, cada vez que se apaga se queda vacía
#El disco duro obviamente no comienza vacío debido a que debe contener la info de los SO y todo listo para cargar a la RAM lo que se le solicite
#Dos sectores llenos, uno con la info de Linux  y otro con la info de Windows, deben estar separados NO juntos


#Entonces como primer punto del bootloader, vamos a verificar que la RAM y el Disco Duro estén bien y sirvan
#Simular fallos mediante probabilidad, que un bit se jodió por ejemplo




#-----------------------------------------------------------------------------------------------------------------------------------
#ALMACENAMIENTO
#Simulacion del almacenamiento y la memoria RAM
#Tabla de Particiones
# 0 Tabla de Particiones 1&8
# 1 Instrucciones de Windows 9&16
# 2 Instrucciones de Linux 17&24
# 3 Instrucciones de un programa 25&32
# 4 Instrucciones de un programa 33&40
# 5 Instrucciones de un programa 41&48
# 6 Instrucciones de un programa 49&56
# 7 Instrucciones de un programa 57&64

almacenamiento = ["1|8" ,"9|16" ,"17|24","25|32","33|40","41|48","49|56","57|64", #Sector1: Primeras 8 posiciones indican la tabla de particiones que muestran de donde a donde se encuentra cierta informacion
                  "110" , "111" , "112" , "113" , "114" , "115" , "116" , "117" , #Sector2: Instrucciones de Windows
                  "210" , "211" , "212" , "213" , "214" , "215" , "216" , "217" , #Sector3: Instrucciones de Linux
                  None  , None  , None  , None  , None  , None  , None  , None  , #Sector4:Instrucciones Programa Vacio
                  None  , None  , None  , None  , None  , None  , None  , None  , #Sector5:Instrucciones Programa Vacio
                  None  , None  , None  , None  , None  , None  , None  , None  , #Sector6:Instrucciones Programa Vacio
                  None  , None  , None  , None  , None  , None  , None  , None  , #Sector7:Instrucciones Programa Vacio
                  None  , None  , None  , None  , None  , None  , None  , None  , #Sector8:Instrucciones Programa Vacio
                ]

#-----------------------------------------------------------------------------------------------------------------------------------
#RAM
RAM = [None, None, None,None,None,None, None, None,   #Bloque donde se carga el Bootloader en la RAM
       None, None, None,None,None,None, None, None,   #Bloque donde se carga el sistema operativo de arranque
       None, None, None,None,None,None, None, None,   #Bloque donde posiblemente se pueda cargar algun programa
       None, None, None,None,None,None, None, None,   #Bloque donde posiblemente se pueda cargar algun programa
      ]

#-----------------------------------------------------------------------------------------------------------------------------------
#BOOTLOADER:

#Funcion para cargar un sistema operativo Windows o Linux
def cargarSistemaOperativo():
    indiceRam = 8
    sistema = input("Digite W si desea cargar Windows o L si desea cargar Linux: ")

    if(sistema == "W"):
        for i in range(8,16):
            RAM[indiceRam] = almacenamiento[i]
            indiceRam += 1
    elif(sistema == "L"):
        for i in range(16,24):
            RAM[indiceRam] = almacenamiento[i]
            indiceRam += 1


#Funcion para cargar desde una unidad externa, el usuario podra seleccionar un txt cualquiera de afuera que tendra que tener el siguiente formato valido:
#Linea 1:  310 311 312 313 314 315 316 317
#Simulando un determinado sistema Operativo que se cargara el la memoria RAM, en los 8 espacios disponibles para el Sistema Operativo
def cargarDesdeUnidadExterna():
    nombreUnidadExterna = input("Digite el nombre de la unidad externa desde la cual desea cargar el sistema operativo: ")
    unidadExterna = open(nombreUnidadExterna, "r")
    print(unidadExterna.read())



def show_menu():
    print ("\nMenu Bootloader")
    print ("------------------------")
    print ("1) Verificar Funcionamiento")
    print ("2) Cargar Sistema Operativo")
    print ("3) Cargar Desde Dispositivo Externo")
    print ("4) Modo Mantenimiento")

    print ("Q) Exit\n")
 
def menu():
    while True:
        show_menu()
        choice = input('Digite Operacion a realizar: ').lower()
        if choice == '1':
            print("Verificando Funcionamiento...")
        elif choice == '2':
            cargarSistemaOperativo()
        elif choice == '3':
            cargarDesdeUnidadExterna()
        elif choice == '4':
            print("Modo mantenimiento...")
        elif choice == 'q':
            return
        else:
            print(f'No es una opcion correcta: <{choice}>, digite nuevamente')
 

#-----------------------------------------------------------------------------------------------------------------------------------
#INICIO SIMULACION BOOTLOADER

if __name__ == '__main__':
            #En primera instancia cargamos el bootloader en la RAM
    menu()



#------------------------------------------------------------------------------------------------------------------------------------
#METODOS EXTRAS
#Metodo para automatizar, sin embargo me puedo creer superusuario y saber donde empieza y finaliza cada cuestion en especifico
#Prepara la tabla de particiones para definir correctamente cual es el inicio y final correctos de determinado segmento en la tabla
for i in range(0, 8):
    tablaParticiones = almacenamiento[i]
    x = tablaParticiones.split("|")
    inicio = x[0]
    final = x[1]
    #print("Inicio: " + inicio + " Final: " + final)