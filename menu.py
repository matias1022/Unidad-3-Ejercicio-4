import os
from ClaseColeccion import Coleccion

class Menu:
      __op = 0
      def __init__(self,opcion=0):
        self.__op = opcion
      def Ejecutar(self,tamaño):
          os.system('cls')
          salir = False
          coleccion=Coleccion(tamaño)
          coleccion.agregarEmpleadoPlanta()
          coleccion.agregarEmpleadoContratado()
          coleccion.agregarEmpleadoExterno()

          while salir == False:
              print('1-\t Ingresar el DNI de un empleado y la cantidad de horas trabajadas hoy e incrementar la cantidad de las horas trabajadas del empleado.')
              print('2-\tDada una tarea mostrar el monto a pagar para ella. Solo se consideran las tareas que no han finalizado.')
              print('3-\tLa empresa dará una ayuda solidaria a los empleados cuyo sueldo sea inferior a $25000; listar nombre, dirección y DNI de los empleados que les corresponde la ayuda.')
              print('4-\tMostrar nombre, teléfono y sueldo a cobrar de todos los empleados.')
              print('0-\tSalir')
              self.__op = int(input('Ingrese la opcion: '))
              if self.__op == 1:  
                 dni=input("Ingresar DNI de el empleado a buscar:")#1
                 horas=int(input("Ingresar la cantidad de horas trabajadas hoy dia:"))
                 if coleccion.verificarDNI(dni)==True:
                       coleccion.registrarHora(horas,dni)
                 else: print("No hay empleado con el DNI ingresado")
              elif self.__op == 2: 
                 tarea=input("Ingresar Tarea(Carpinteria, Electricidad, Plomeria):")
                 if tarea=="Carpinteria" or tarea=="Electricidad" or tarea=="Plomeria":
                     coleccion.mostrarMonto(tarea)
                 else: print("La tarea ingresada no esta disponible")
              elif self.__op == 3: 
                  coleccion.ayuda()
              elif self.__op == 4: 
                  coleccion.mostrarSueldo()
              elif self.__op == 0: 
                  salir = True
              else:
                 print('Opcion ingresada incorrecta')
                 input('Presiona ENTER para continuar...')

        
          print('Cerrando Menú..')   