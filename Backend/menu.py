from persona import Persona
from administrador import Administrador
from destinos import Destinos

print('Bienvenido al sistema de ventas de ISPC TOUR')

def verificar_Si_No(respuesta):
    if respuesta.lower() == 'si':
        return respuesta.lower()
    elif respuesta.lower() == 'no':
        return respuesta.lower()
    else:
        print('Seleccione una respuesta valida.')
        return verificar_Si_No(input('Por favor seleccione entre SI o NO: '))
        
def validar_numero():
    while True:

        numero = input("Por favor, ingresa su eleccion: ")
        if numero == '1' or numero == '2' or numero == '3' or numero == '4':
            return numero
        else:
            print("Por favor, selecciona un número válido.")


while True:

    respuestaUsuario = verificar_Si_No(input('Posee un usuario registrado? SI/NO: '))
    #print(respuestaUsuario)

    if respuestaUsuario == 'si':
        #print('Menu de inicio')
        for intento in range(3):
            validar_usuario = Persona.verificar_usuario(respuestaUsuario)
            if validar_usuario != False:
                print('Bienvenido ', validar_usuario, '!')
                break
            else:
                print('Contraseña incorrecta. Te quedan', 2 - intento, 'intentos.')
            
            if intento == 2:
                print("Usuario bloqueado.")
                respuestaUsuario = False
                break
        break
    else:
        print('Menu registro')
        nuevoUsuario = Persona()
        print('El sistema va a reiniciar, seleccione la opcion SI al inicio del programa.')
        print('Y acontinuación ingrese su usuario registrado')
        print('*********')

if Administrador.verificarAdministrador(validar_usuario) == 1:
    while True:
        print('******************************')
        print('Bienvenido al menu de administrador')
        print('******************************')
        print('1 - Cambiar rol de usuario')
        print('2 - Agregar destino')
        print('3 - Editar destino')
        print('4 - Salir de menu de administrador y pasar al menu normal')

        seleccion_administrador = input('Ingrese la opcion seleccionada: ')

        if seleccion_administrador == '1':
            print('Permite seleccionar usuarios para editar')
            Administrador.modificar_rol()
            print('********')
    
        elif seleccion_administrador == '2':
            print('Opciones para agregar destinos')
            nuevo_destino = Destinos()
            
            print('********')
    
        elif seleccion_administrador == '3':
            print('Muestra destinos y permite seleccionar uno para editar')
            Destinos.editarDestino()
            
            print('********')
    
        elif seleccion_administrador == '4':
            print('Usted ha salido de menu administrador')
            print('********')
            break

        else:
            print('La opcion seleccionada no es valida')
            print('********')




while respuestaUsuario != False:
    print('Por favor seleccione el numero de la opción que desee realizar.')
    print('1 - Ver paquetes de viajes disponibles.')
    print('2 - Ver mis reservas.')
    print('3 - Eliminar alguna reserva')
    print('4 - Terminar sesión')

    seleccion_menu = validar_numero()

    if seleccion_menu == '1':
        print('Muestra destinos turisticos disponibles')
        print('********')
    
    elif seleccion_menu == '2':
        print('En caso de tener reservas muestras las mismas y si no muestra "No tiene reservas"')
        print('********')
    
    elif seleccion_menu == '3':
        print('Muestra las revervas y da la opcion de eliminarlas')
        print('********')
    
    else:
        print('Sesión cerrada')
        print('********')
        break




print('Gracias por usar nuestro sistema de ventas')