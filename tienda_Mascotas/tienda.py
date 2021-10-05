from tienda_Mascotas.Dominio.mascota import Mascota
from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Dominio.alimento import Alimento
from tienda_Mascotas.Dominio.accesorio import Accesorio
from tienda_Mascotas.Dominio.cliente import Cliente
from tienda_Mascotas.Dominio.empleado import Empleado
from tienda_Mascotas.Infraestructura.persistencia import Persistencia
from tienda_Mascotas.Dominio.especificacion import Especificacion
from tienda_Mascotas.Dominio.venta import Venta
from tienda_Mascotas.Infraestructura.configuracion import Configuracion
import os
if __name__=='__main__':

 """Primero declaramos la persistencia y luego utilizamos el metodo saver.connect cuando iniciamos la aplicacion
 esto genera la base de datos sqlite y las tablas de la entitades que necesitamos con sus atributos"""

 saver = Persistencia()
 saver.connect()

 #Metodo generar configuracion, el cual trae la configuracion que esta guardada en archivo plano json

 def generarConfiguracion():
    for file in os.listdir("./files"):
              if '1.json' in file:
                configuracion= Persistencia.load_json_configuracion(file)
    return configuracion

 """En el metodo generarInventario cargamos los datos que estan guardados tanto en archivos planos json y 
 los que estan guardados en base de datos sqlite para utilizarlos en uno solo, en este caso la clase inventario"""

 def generarInventario():
     inventario= Inventario()
     mascotas= saver.consultar_tabla_mascota()
     alimentos= saver.consultar_tabla_alimento()
     accesorios= saver.consultar_tabla_accesorio()
     clientes= saver.consultar_tabla_cliente()
     empleados= saver.consultar_tabla_empleado()
     for mascota in mascotas:
         inventario.agregar_mascota(mascota)
     for alimento in alimentos:
         inventario.agregar_alimento(alimento)
     for accesorio in accesorios:
         inventario.agregar_accesorio(accesorio)
     for cliente in clientes:
         inventario.agregar_cliente(cliente)
     for empleado in empleados:
         inventario.agregar_empleado(empleado)
     for file in os.listdir("./files"):
              if '1.json' in file:
                configuracion= Persistencia.load_json_configuracion(file)
              elif '.jsonMascota' in file:
               inventario.agregar_mascota(Persistencia.load_json_mascota(file))
              elif '.jsonEmpleado' in file:
                  inventario.agregar_empleado(Persistencia.load_json_empleado(file))
              elif '.jsonCliente' in file:
                  inventario.agregar_cliente(Persistencia.load_json_cliente(file))
              elif '.jsonAlimento' in file:
                  inventario.agregar_alimento(Persistencia.load_json_alimento(file))
              elif '.jsonAccesorio' in file:
                  inventario.agregar_accesorio(Persistencia.load_json_accesorio(file))
     return inventario

 """En el metodo agregar informacion, le damos al usuario una seria de opciones dadas por un while,
 y dependiendo la que elija, lo lleva a llenar los datos de la clase que escogio.Dependiendo de la configuracion
 esta lo guarda como un archivo plano json o base sqlite"""

 def agregar_informacion(saver,configuracion):
     inventario= generarInventario()
     ans=True
     while ans:
        print ("""
        BIENVENIDO A LA TIENDA DE MASCOTAS, ELIGE ENTRE NUESTRAS OPCIONES,
        PARA MANTENER LA TIENDA ORDENADA Y REGISTRAR SUS ELEMENTOS
        
        1.Agregar nueva mascota.
        2.Agregar nuevo alimento de mascotas.
        3.Agregar nuevo accesorio de mascotas.
        4.Agregar nuevo cliente.
        5.Agregar nuevo empleado.
        6.Configuracion.
        7.Regresar al menu principal.
        """)
        ans = input("Cual de las opciones quieres?: ")
        if ans == "1":
           codigoMascota= str(input("Ingrse el codigo de la mascota:"))
           tipo_mascota = str(input("Ingrese el de que tipo de animal que es la mascota:"))
           raza = str(input("Ingrese la raza de la mascota:"))
           nombre = str(input("Ingres el nombre provicional de la mascota:"))
           edad = int(input("Ingrese la edad que tiene la mascota:"))
           precioMascota = float(input("Ingrese el precio de la mascota:"))
           cantidadMascota= int(input("Ingrese la cantidad de mascotas que hay con estas caracteristicas:"))
           mascota= Mascota(codigoMascota,tipo_mascota,raza,nombre,edad,precioMascota,cantidadMascota)
           try:
               inventario.agregar_mascota(mascota)
               if configuracion.estado == "archivo plano json":
                  Persistencia.save_json_mascota(mascota)
                  print("\n Se agrego la mascota con exito en js")
               else:
                  saver.guardar_mascota(mascota)
                  print("\n Se agrego la mascota con exito en bd")
           except Exception as ex:
               print(ex)


        elif ans == "2":
           codigoAlimento= str(input("Ingrse el codigo del alimento:"))
           tipo_alimento = str(input("Ingrese el tipo de alimento que quiere registrar:"))
           nombreAlimento = str(input("Ingrese el nombre del producto::"))
           cantidadAlimento = int(input("Ingrese numero de existencias del articulo:"))
           cantidadContenido = int(input("Ingrese la cantidad de contenido del producto(en gramos):"))
           precioAlimento = float(input("Ingrese el precio del producto alimenticio:"))
           alimento= Alimento(codigoAlimento,tipo_alimento,nombreAlimento,cantidadAlimento,cantidadContenido,precioAlimento)
           try:
            inventario.agregar_alimento(alimento)
            if configuracion.estado == "archivo plano json":
                 Persistencia.save_json_alimento(alimento)
                 print("\n Se agrego el alimento para mascotas con exito en js")
            else:
               saver.guardar_alimento(alimento)
               print("\n Se agrego el alimento para mascotas con exito en bd")
           except Exception as ex:
               print(ex)
        elif ans == "3":
           codigoAccesorio= str(input("Ingrse el codigo del accesorio:"))
           nombreAccesorio= str(input("Ingrese el nombre del accesorio:"))
           descripcionAccesorio= str(input("Ingrese una descripcion corta del accesorio:"))
           usoAccesorio= str(input("Ingrese el uso del accesorio:"))
           precioAccesorio= float(input("Ingrese el precio del accesorio:"))
           cantidadAccesorio= int(input("Ingrese la cantidad de existencias del acesorio:"))
           accesorio= Accesorio(codigoAccesorio,nombreAccesorio,cantidadAccesorio,precioAccesorio,descripcionAccesorio,usoAccesorio)
           try:
              inventario.agregar_accesorio(accesorio)
              if configuracion.estado == "archivo plano json":
                 Persistencia.save_json_accesorio(accesorio)
                 print("\n Se agrego el accesorio de mascotas con exito en js")
              else:
                 saver.guardar_accesorio(accesorio)
                 print("\n Se agrego el accesorio de mascotas con exito en bd")
           except Exception as ex:
               print(ex)

        elif ans == "4":
           codigoCliente= str(input("Ingrse el codigo del cliente:"))
           nombreCliente= str(input("Ingrese el nombre del cliente:"))
           cedulaEmpleado= str(input("Ingrese la cedula del empleado:"))
           apellidoCliente= str(input("Ingrese el apellido del cliente:"))
           generoCliente= str(input("Ingrese el genero del cliente:"))
           edadCliente=int(input("Ingrese la edad del cliente"))
           direccionCliente=str(input("Ingrese la direccion de residencia del cliente:"))
           correoCliente=str(input("Ingrese el correo de contacto del cliente:"))
           tiempoCliente= str(input("Ingrese el tiempo que lleva la persona siendo su cliente:"))
           cliente= Cliente(codigoCliente,nombreCliente,apellidoCliente,cedulaEmpleado,generoCliente
                            ,direccionCliente,correoCliente,edadCliente,tiempoCliente)
           try:
               inventario.agregar_cliente(cliente)
               if configuracion.estado == "archivo plano json":
                 Persistencia.save_json_cliente(cliente)
                 print("\n Se agrego el nuevo cliente con exito en js")
               else:
                 saver.guardar_cliente(cliente)
                 print("\n Se agrego el nuevo cliente con exito en bd")
           except Exception as ex:
               print(ex)

        elif ans == "5":
           codigoEmpleado= str(input("Ingrse el codigo del empleado:"))
           nombreEmpleado= str(input("Ingrese el nombre del empleado:"))
           cedulaEmpleado= str(input("Ingrese la cedula del empleado:"))
           apellidoEmpleado= str(input("Ingrese el apellido del empleado:"))
           generoEmpleado= str(input("Ingrese el genero del empleado:"))
           edadEmpleado=int(input("Ingrese la edad del empleado:"))
           direccionEmpleado=str(input("Ingrese la direccion de residencia del empleado:"))
           correoEmpleado=str(input("Ingrese el correo de contacto del empledo:"))
           cargoEmpleado= str(input("Ingrese el cargo que tiene el empleado en la tienda:"))
           horarioEmpleado= str(input("Ingrese el horario que cumple el empleado:"))
           salarioEmpleado= str(input("Ingrese el salario que tiene el empleado:"))
           empleado= Empleado(codigoEmpleado,nombreEmpleado,cedulaEmpleado,apellidoEmpleado,cargoEmpleado,salarioEmpleado,generoEmpleado,
                              edadEmpleado,direccionEmpleado,correoEmpleado,horarioEmpleado)
           try:
             inventario.agregar_empleado(empleado)
             if configuracion.estado == "archivo plano json":
               Persistencia.save_json_empleado(empleado)
               print("\n Se agrego el nuevo empleado con exito en js")
             else:
               saver.guardar_empleado(empleado)
               print("\n Se agrego el nuevo empleado con exito en bd")
           except Exception as ex:
               print(ex)

        elif ans == "6":
          opcion= True
          while opcion:
            print("En estos momentos los elemento se guardan por medio de:"+" "+str(configuracion.estado))
            print("""Elija como quiere guardar sus elementos
                           1.Archivos planos tipo json
                           2.Base de datos sqlite
                           3.Regresar.
                           """)
            opcion= input("Que opcion elige?:")
            if opcion == "1":
                configuracion.cambiarEstadoConfiguracion("archivo plano json")
                Persistencia.save_json_configuracion(configuracion)
                print("Se cambio la configuracion a archivos planos de tipo json")
            elif opcion == "2":
                configuracion.cambiarEstadoConfiguracion("Base de datos sqlite")
                Persistencia.save_json_configuracion(configuracion)
                print("Se cambio la configuracion a Base de datos sqlite")
            elif opcion == "3":
                print("Se guardaron los cambios")
                opcion=False
            elif opcion !="":
                print("Opcion invalida")
        elif ans == "7":
          ans = False
        elif ans != "":
          print("\n Opcion no es valida, verifique el numero ingresado")

 """En el metodo buscar informacion el usuario se le da un menu de opciones para buscar la clase que quiera,y por 
 los atributos que quiera. Dependiendo de la clase que elija, se despliegan una serie de caracteristicas. El usuario
 escoje el numero de caracteristicas, el numero de referencia a la caracteristica y por ultimo el valor de esta,
 luego de esto se visualiza la representacion del objeto en caso de que exista"""

 def buscar_informacion():
       opc=True
       inventario= generarInventario()
       while opc:
            especificacion= Especificacion()
            print ("""
            BIENVENIDO A LA TIENDA DE MASCOTAS, ELEGI ENTRE NUESTRAS OPCIONES,
            PARA BUSCAR TUS ELEMENTOS Y TENER UN CONTROL SOBRE ESTOS
            
            1.Buscar mascota.
            2.Buscar alimento de mascotas.
            3.Buscar accesorio de mascotas.
            4.Buscar cliente.
            5.Buscar empleado.
            6.Regresar al menu principal.
            """)
            opc= input("Ingrese la opcion que desee:")
            if opc == "1":
                print ("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                A LA MASCOTA.
                
                1.Codigo mascota.
                2.tipo de mascota.
                3.raza de la mascota.
                4.nombre de la mascota.
                5.precio de la mascota.
                6.edad mascota.
                7.Regresar.
                """)
                resultado= int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
                if resultado >6:
                    print("No puede buscar por mas de 5 atributos para la mascota")
                else:
                   for i in range (resultado):
                       llave= input("Ingrese el numero al que corresponde la caracteristica:")
                       valor= input("Ingrese el valor de la caracteristica:")
                       if llave == "1":
                           llave = "codigoMascota"
                       elif llave == "2":
                           llave= "tipoMascota"
                       elif llave == "3":
                           llave = "raza"
                       elif llave == "4":
                           llave = "nombre"
                       elif llave == "5":
                           llave = "precio"
                       elif  llave == "6":
                           llave == "edad"
                       elif llave == "7":
                           print("No hubo busqueda")
                       elif llave != "":
                           print("Ingreso opciones invalidas")
                       especificacion.agregar_parametro(llave,valor)
                   print(list(inventario.buscar_mascota(especificacion)))
            elif opc == "2":
                print ("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                EL ALIMENTO PARA MASCOTAS.
                
                1.Codigo alimento de mascotas.
                2.tipo de alimento de mascotas.
                3.cantidad existencias.
                4.nombre del producto.
                5.precio del producto.
                6.cantidad de contenido alimento.
                7.Regresar.
                """)
                resultado= int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
                if resultado >6:
                    print("No puede buscar por mas de 5 atributos para el alimento")
                else:
                   for i in range (resultado):
                       llave= input("Ingrese el numero al que corresponde la caracteristica:")
                       valor= input("Ingrese el valor de la caracteristica:")
                       if llave == "1":
                           llave = "codigoAlimento"
                       elif llave == "2":
                           llave= "tipoAlimento"
                       elif llave == "3":
                           llave = "cantidadAlimento"
                       elif llave == "4":
                           llave = "nombreProducto"
                       elif llave == "5":
                           llave = "precio"
                       elif  llave == "6":
                           llave == "cantidadContenido"
                       elif llave == "7":
                           print("No hubo busqueda")
                       elif llave != "":
                           print("Ingreso opciones invalidas")
                       especificacion.agregar_parametro(llave,valor)
                   print(list(inventario.buscar_alimento(especificacion)))
            elif opc == "3":
                print ("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                EL ACCESORIO DE MASCOTAS.
                
                1.Codigo accesorio.
                2.Nombre del accesorio.
                3.Cantidad existencias del accesorio.
                4.Precio del accesorio.
                5.Descripcion del accesorio.
                6.Uso del accesorio.
                7.Regresar.
                """)
                resultado= int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
                if resultado >6:
                    print("No puede buscar por mas de 5 atributos para el accesorio")
                else:
                   for i in range (resultado):
                       llave= input("Ingrese el numero al que corresponde la caracteristica:")
                       valor= input("Ingrese el valor de la caracteristica:")
                       if llave == "1":
                           llave = "codigoAccesorio"
                       elif llave == "2":
                           llave= "nombreAccesorio"
                       elif llave == "3":
                           llave = "cantidadAccesorio"
                       elif llave == "4":
                           llave = "precioAccesorio"
                       elif llave == "5":
                           llave = "descripcionAccesorio"
                       elif  llave == "6":
                           llave == "usoAccesorio"
                       elif llave == "7":
                           print("No hubo busqueda")
                       elif llave != "":
                           print("Ingreso opciones invalidas")
                       especificacion.agregar_parametro(llave,valor)
                   print(list(inventario.buscar_accesorio(especificacion)))
            elif opc == "4":
                print ("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                A EL CLIENTE.
                
                1.Codigo del cliente.
                2.Cedula del cliente.
                3.Genero del cliente.
                4.Nombre del cliente.
                5.apellido del cliente.
                6.Edad el cliente.
                7.Direccion del cliente.
                8.Correo del cliente.
                9.Tiempo como cliente de la tienda.
                10.Regresar.
                """)
                resultado= int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
                if resultado >8:
                    print("No puede buscar por mas de 8 atributos para el cliente")
                else:
                   for i in range (resultado):
                       llave= input("Ingrese el numero al que corresponde la caracteristica:")
                       valor= input("Ingrese el valor de la caracteristica:")
                       if llave == "1":
                           llave = "codigoCliente"
                       elif llave == "2":
                           llave= "cedula"
                       elif llave == "3":
                           llave = "genero"
                       elif llave == "4":
                           llave = "nombre"
                       elif llave == "5":
                           llave = "apellido"
                       elif  llave == "6":
                           llave == "edad"
                       elif llave == "7":
                           llave="direccion"
                       elif llave == "8":
                           llave= "correo"
                       elif llave == "9":
                           llave= "tiempoCliente"
                       elif llave == "10":
                           print("No hubo busqueda")
                       elif llave != "":
                           print("Ingreso opciones invalidas")
                       especificacion.agregar_parametro(llave,valor)
                   print(list(inventario.buscar_cliente(especificacion)))
            elif opc == "5":
                print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                A EL EMPLEADO.
                
                1.Codigo del empleado.
                2.Cedula del empleado.
                3.Genero del empleado.
                4.Nombre del empleado.
                5.apellido del apellido.
                6.Edad del empleado.
                7.Direccion del empleado.
                8.Correo del empleado.
                9.Cargo del empleado.
                10.Horario del empleado.
                11.Salario del empleado.
                12.Regresar.
                """)
                resultado= int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
                if resultado >8:
                    print("No puede buscar por mas de 8 atributos para el cliente")
                else:
                   for i in range (resultado):
                       llave= input("Ingrese el numero al que corresponde la caracteristica:")
                       valor= input("Ingrese el valor de la caracteristica:")
                       if llave == "1":
                           llave = "codigo"
                       elif llave == "2":
                           llave= "cedula"
                       elif llave == "3":
                           llave = "genero"
                       elif llave == "4":
                           llave = "nombre"
                       elif llave == "5":
                           llave = "apellido"
                       elif  llave == "6":
                           llave = "edad"
                       elif llave == "7":
                           llave="direccion"
                       elif llave == "8":
                           llave= "correo"
                       elif llave == "9":
                           llave= "cargo"
                       elif llave == "10":
                           llave= "horario"
                       elif llave == "11":
                           llave= "salario"
                       elif llave == "12":
                           print("No hubo busqueda")
                       elif llave !="":
                           print("Ingreso opciones invalidas")
                       especificacion.agregar_parametro(llave,valor)
                   print(list(inventario.buscar_empleado(especificacion)))
            elif opc == "6":
                opc=False
            elif opc != "":
                print("\n Opcion invalida porfavor rectifica")

 """En el metodo generar venta el usuario puede vender productos de la tienda, ya sean mascotas, accesorios o alimentos
 pirmero ingresa el codigo del empleado que realiza la venta, el cliente que realiza la compra, y luego pasa a escoger
 los elementos que quiere vender, sus cantidades y precios. Por ultimo sale un resumen de los datos de la compra con
 su valor final"""

 def generarVenta():
     codigoEmpleado= input("Ingrese el codigo del empleado")
     codigoCliente= input("Ingrese el codigo del cliente que va a hacer la compra")
     inventario=generarInventario()
     especificacionEmpleado= Especificacion()
     especificacionEmpleado.agregar_parametro("codigo",codigoEmpleado)
     especificacionCliente= Especificacion()
     especificacionCliente.agregar_parametro("codigoCliente",codigoCliente)
     empleado= list(inventario.buscar_empleado(especificacionEmpleado))
     cliente= list(inventario.buscar_cliente(especificacionCliente))
     if len(empleado)==0 or len(cliente)==0:
         print("No se encontraron resultados con el cliente o el empleado, porfavor rectifique")
         elemento= False
     else:
         print("Se encontraron el cliente y el empleado de manera satisfactoria, proceda a generar la factura.....")
         factura=[]
         listaPrecios=[]
         listaCantidades=[]
         valorTotal=0
         elemento= True
     while elemento:
             especificacion= Especificacion()
             print("""Elija el elemento que quiere añadir a la compra:
             1.Accesorio
             2.Mascota.
             3.Alimento
             4.Terminar compra""")
             elemento= input("\n Ingrese le numero que hace referencia al elemento:")
             if elemento == "1":
                 codigoAccesorio= input("Ingrese el codigo del accesorio:")
                 especificacion.agregar_parametro("codigoAccesorio",codigoAccesorio)
                 producto= list(inventario.buscar_accesorio(especificacion))
                 if len(producto)==0:
                     print("No se encontro el accesorio especificado:")
                 else:
                    accesorio= producto[0]
                    listaPrecios.append(accesorio.precio)
                    print("\n la cantidad de existencias disponibles de este accesorio es de:"+" "+str(accesorio.cantidad))
                    print("\n El precio actual del accesorio es de:"+" "+str(accesorio.precio))
                    cantidadCompra= int(input("\n Ingrese la cantidad del accesorio que se desea comprar:"))
                    listaCantidades.append(cantidadCompra)
                    if cantidadCompra> accesorio.cantidad:
                        print("No puede comprar mas accesorios de los que estan disponibles")
                    else:
                        valorCompra= accesorio.precio*cantidadCompra
                        valorTotal=valorTotal+valorCompra
                        print("\n Registro la compra del accesorio")
                        factura.append(producto[0])

             elif elemento == "2":
                 codigoMascota= input("Ingrese el codigo de la mascota:")
                 especificacion.agregar_parametro("codigoMascota",codigoMascota)
                 producto= list(inventario.buscar_mascota(especificacion))
                 if len(producto)==0:
                     print("No se encontro la mascota especificada:")
                 else:
                    mascota= producto[0]
                    listaPrecios.append(mascota.precio)
                    print("la cantidad de mascotas con estas caracteristicas es de:"+" "+str(mascota.cantidad))
                    print("\n El precio actual de la mascota:"+" "+str(mascota.precio))
                    cantidadCompra= int(input("\n Ingrese la cantidad de mascotas con estas caracteristicas que desea comprar:"))
                    listaCantidades.append(cantidadCompra)
                    if cantidadCompra> mascota.cantidad:
                        print("No puede comprar mas mascotas de este tipo de las que estan disponibles")
                    else:
                        valorCompra= mascota.precio*cantidadCompra
                        valorTotal=valorTotal+valorCompra
                        print("\n se registro la compra de las mascota")
                        factura.append(producto[0])


             elif elemento == "3":
                 codigoAlimento= input("Ingrese el codigo del alimento:")
                 especificacion.agregar_parametro("codigoAlimento",codigoAlimento)
                 producto= list(inventario.buscar_alimento(especificacion))
                 if len(producto)==0:
                     print("No se encontro el alimento especificado:")
                 else:
                    alimento= producto[0]
                    listaPrecios.append(alimento.precio)
                    print("\n la cantidad de existencias disponibles de este alimento es de:"+" "+str(alimento.cantidad))
                    print("\n El precio actual del alimento es de:"+" "+str(alimento.precio))
                    cantidadCompra= int(input("\n Ingrese la cantidad de alimento que se desea comprar:"))
                    listaCantidades.append(cantidadCompra)
                    if cantidadCompra> alimento.cantidad:
                        print("No puede comprar mas alimento de los que estan disponibles")
                    else:
                        valorCompra= alimento.precio*cantidadCompra
                        valorTotal=valorTotal+valorCompra
                        print("\n se registro la compra del accesorio")
                        factura.append(producto[0])


             elif elemento == "4":
                 print("Gracias por realizar tu compra:")
                 venta=Venta(empleado[0],cliente[0],factura,listaCantidades,listaPrecios,valorTotal)
                 Persistencia.save_json_venta(venta)
                 print("Empleado que realiza la venta:"+" "+venta.empleado.nombre)
                 print("Cliente que realiza la compra:"+" "+venta.cliente.nombre)
                 print("La lista de compras esta compuesta por:")
                 for i in range(len(factura)):
                     print("Elemento:"+" "+str(factura[i])+" "+str(listaCantidades[i])+" "+str(listaPrecios[i]))
                 print("Valor total de la venta:"+" "+str(valorTotal))
                 elemento= False
             elif elemento != "":
                 print("Opcion invalida")

 """En el mostrar venta buscamos los archivos que corresponden a una venta, para luego mostrar la representacion al
 usuario de cada venta"""

 def mostrarVenta():
     ventas= []
     for file in os.listdir("./files"):
              if '.jsonVenta' in file:
                  ventas.append(Persistencia.load_json_venta(file))
     if len(ventas)==0:
         print("No hay ventas aun")
     else:
        for venta in ventas:
         print(venta)




 """Este es el while principal donde se ejecutan todos los metodos previamente dichos dependiendo de la 
 decision del usuario"""

 ansPrin= True
 while ansPrin:
            print ("""
            BIENVENIDO A LA TIENDA DE MASCOTAS, ELEGI ENTRE NUESTRAS OPCIONES,
            PARA AGREGAR, BUSCAR O VENDER UN ELEMENTO DE TU TIENDA:
            
            1.Agregar elemento.
            2.Buscar elemento.
            3.Vender elemento.
            4.Ver ventas.
            5.Terminar y salir.
            """)
            ansPrin = input("Cual de las opciones quieres?: ")
            if ansPrin == "1":
                configuracion= generarConfiguracion()
                agregar_informacion(saver,configuracion)
            elif ansPrin == "2":
                 buscar_informacion()
            elif ansPrin == "3":
                generarVenta()
            elif ansPrin == "4":
                mostrarVenta()
            elif ansPrin !="":
                print("\n Nos vemos hasta la proxima!")
                ansPrin= False

