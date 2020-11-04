#Se importa la librería random para hacer que las preguntas sean aleatorias
import random
#Se importa la librería webbrowser para poder abrir las páginas de consulta
import webbrowser

#función que genera la llave usada para usar valores diferentes cada vez
def inicio_nuevo (lrange, rrange):
    quiz = random.randint(lrange,rrange)
    return quiz

#Se crean listas con los valores que serán usados en las preguntas
#Como el valor de la variable quiz es constante a lo largo del programa, al ser aleatoria permite que cada intento sea diferente del anterior
#El objetivo de este programa es comprobar mediante condicionales guardados en la función corroborar si las respuestas son correctas o no
#dando retroalimentación instantánea al usuario.

#MATEMÁTICAS
#Pregunta 1 matemáticas
altura = [20, 50, 60, 90, 100, 120, 75]
pisos = ["4", "10", "12", "18", "20", "24", "15"]

#Pregunta 2 matemáticas
dados = ["1 y 2", "1, 2 y 3", "2", "3, 4 y 5", "3", "1, 2, 3, 4 y 5", "1 y 4" ]
fraccion = ["4", "6", "2", "6", "2", "10", "4"]

#Pregunta 3 matemáticas
medidas = [" 5cm, 5cm y 5cm", " 4cm, 5cm y 5cm", " 4cm, 6cm y 5cm", " 8cm, 8cm y 8cm", " 19cm, 19cm y 10cm", " 15cm, 15cm y 15cm", " 6cm, 9cm y 6cm", ]
triangulo = ["equi", "iso", "esca", "equi", "iso", "equi", "iso"]

#Pregunta 4 matemáticas
ecuaciones=["x^2-25=0", "x^2-5x=0", "3x^2-24x=0", "x^2-16=0", "x^2-x=0", "x^2-5x=0", "3x^2-27x=0"]
valores_de_x=["5","5","8","4","1","5","3"]

#Usuarios
users=[["test"], ["test"]]

#Se comprueba si el usuario ingresado se encuentra en la matriz users
def comprobar_usuario (user, contraseña):
    for i in range(0, len(users[0])):
        if ((users[0][i] == user) and (users[1][i] == contraseña)):
            #Si el usuario y la contraseña coinciden se regresa True
            return True
    return False
        

#Funcion que permite al slumno registrarse
def registrarse():
    print("Bienvenido al menú de registro")
    #El usuario ingresa sus datos
    user = str(input("Ingrese su nombre de usuario: "))
    contraseña = str(input("Ingrese su contraseña: "))
    contraseña1 = str(input("Confirme su contraseña: "))
    #si las contraseñas coinciden
    if contraseña1 == contraseña:
        #Se añaden el nombre del usuario y su contraseña a la matriz de users
        users[0].append(user)
        users[1].append(contraseña)
        print("Bienvenido ", user)
    #Si las contraseñas no coinciden se imprime error y regresa al inicio de sesión
    else:
        print("Error: las contraseñas no coinciden")

#Funcion que permite iniciar sesion
def inicio_sesion():
    print("Inicie sesión para poder ingresar al programa de estudio y guardar su progreso \n Ingrese 1 si cuenta con una cuenta \n Ingrese 2 si desea registrarse")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        user = str(input("Ingrese su nombre de usuario: "))
        contraseña = str(input("Ingrese su contraseña: "))
        if comprobar_usuario(user, contraseña):
            return True
        else:
            print("El usuario o la contraseña son incorrectos")
            return False
    elif opcion ==2:
        registrarse() 
        return False
    else:
        print("Opcion no válida")
        return False
    
#Con esta función se regresa un 1 si la respuesta ingresada es igual a la correcta y un 0 si es duiferente
def suma_respuestas (respuesta, correcta):
    if respuesta == correcta:
        return 1
    else:
        return 0

#Con esta función se imprime si la respuesta es correcta comparando la respuesta del usuario con la respuesta que se ubica en el mismo índex de la pregunta
def corroborar (respuesta, correcta):
    if respuesta == correcta:
        print("--Su respuesta es correcta")
    else:
        print("--La respuesta correcta era ", correcta)

#Con esta función se ingresan las respuestas y se comparan con los valores de la lista dependiendo del valor random generado al inicio del programa
#Examen de matemáticas
def mate ():
    quiz = inicio_nuevo(0, 6)
    #Se declara el contador de respuestad correctas
    print("***Bienvenico a la pruaba de matemáticas***")
    n=0
    
    #Pregunta 1
    print("PREGUNTA 1: Un edificio de ", altura[quiz], " metros de altura tiene pisos que miden 5 metros \n ¿Cuántos pisos tiene este edificio?")
    #El usuario ingresa la cantidad de pisos que tiene el edificio
    respuesta = input("Ingrese su respuesta: ")
    corroborar(respuesta, pisos[quiz])
    #Se le suma al contador n el valor que regresa la función suma_respuestas para contar las preguntas correctas
    n= n + suma_respuestas(respuesta, pisos[quiz])

    #Pregunta 2
    print("PREGUNTA 2: ¿Cuál es la probabilidad de que salga ", dados[quiz], " en dos dados iguales? \n Conteste en fracción")
    #El usuario ingresa el valor de la fracción
    respuesta = input("Ingrese el valor faltante en _/12: ")
    corroborar(respuesta, fraccion[quiz])
    #Se le suma al contador n el valor que regresa la función suma_respuestas para contar las preguntas correctas
    n= n + suma_respuestas(respuesta, fraccion[quiz])

    #Pregunta 3
    print("PREGUNTA 3: Escriba el tipo de triángulo a partir de las siguientes medidas ", medidas[quiz], "\n Conteste iso si el triáncgulo es isóceles \n Conteste esca si el triángulo es escaleno \n Conteste equi si es equilátero")
    #El usuario ingresa el tipo de triángulo
    respuesta = str(input("Ingrese su respuesta: "))
    corroborar(respuesta, triangulo[quiz])
    #Se le suma al contador n el valor que regresa la función suma_respuestas para contar las preguntas correctas
    n= n + suma_respuestas(respuesta, triangulo[quiz])

    #Pregunta 4
    print("PREGUNTA 4: Resuelva las siguientes ecuaciones para x ingresando un número entero")
    #Se crea un ciclo que imprime una ecuación diferente cada vez que se repite
    for i in range (0,7):
        #Se imprime la ecuacón ubicada en el index con el valor de i 
        print(ecuaciones[i])
        #El ususario ingresa el valor de x en esa ecuación
        respuesta=input("Respuesta: ")
        #Se llama la función corroborar y se imprime si el resultado es correcto
        corroborar(respuesta, valores_de_x[i])
        #Se le suma al contador n el valor que regresa la función suma_respuestas para contar las preguntas correctas
        n= n + suma_respuestas(respuesta, valores_de_x[i])
    #Se imprime el número de respuestas correctas
    print("Usted tuvo ", n, "respuestas correctas en esta prueba")
    print("***Felicidades, ha completado el examen!!!")
    #Se manda llamar la función menú para que el usuaario pueda elegir si repetir la prueba o entrar a otra sección de la aplicación

#Examen de ciencias
#En este examen se accede a un banco de datos que almacena las preguntas y sus respuestas en un archivo txt
def ciencias ():
    print("***Bienvenico a la pruaba de ciencias***")
    #Contador de respuestas correctas
    n = 0
    #Se abre el archivo de las preguntas y el de las respuestas con el modo read
    pciencias = open("ciencias.txt", "r")
    rciencias = open("cienciasresp.txt", "r")
    #Se guarda dentro de cadenas cada línea de texto de ambos archivos
    preguntasCiencias = pciencias.readlines()
    respuestaCiencias = rciencias.readlines()
    #Se cierran ambos archivos
    pciencias.close()
    rciencias.close()
    #Ciclo que recorre la lista que contiene las preguntas y se detiene hasta haber recorrido todo el ciclo
    for i in range(0, len(preguntasCiencias)):
        #Bumero que se imprimirá en pantalla
        numeroPregunta = 1 + i
        #Se imprime la pregunta en pantalla
        print("Pregunta ", numeroPregunta, " ", preguntasCiencias[i])
        #Se imprimen las opciones
        print("Sus opciones son: \n", "A)",respuestaCiencias[random.randint(0, 19)], "B)",respuestaCiencias[i], "C)",respuestaCiencias[random.randint(0, 19)])
        #El ususario ingresa su respuesta
        respuesta = str(input("Ingrese su respuesta: "))
        #Se corrobora si es una respuesta correcta
        corroborar(respuesta + "\n", respuestaCiencias[i])
        #Se suma al contador el resultado de llamar la función suma respuestas
        n = n + suma_respuestas(respuesta + "\n", respuestaCiencias[i])
        print("\n")
    #Se imprime el total de respuestas correctas
    print("Usted obtuvo un total de ", n, " respuestas correctas \n")

def comprobartxt(numtxt, resp):
    #Se define el contador de respuestas correctas
    n = 0
    #Se definen las respuestas para cada texto
    resp1 = "ACDBE"
    resp2 = "ED"
    resp3 = "CC"
    #Dependiendo del texto generado se ejecutan las siguientes operaciones
    if numtxt == 1:
        #Si la longitud de caracteres es diferente a la de la cedena se arroja error
        if len(resp) != 5:
            return "El numero de caracteres ingresado excede la cantidad de preguntas \n REPITA EL EXAMEN"
        else:
            #Se crea un ciclo que recorre cada letra en la respuesta y en la cadena del ususario comparándolas
            for i in range(0, len(resp)):
                #Se suma el valor de llamar la funcion suma_respuestas con los caracteres de la respuesta y la cadena del ususario al contador
                n = n + suma_respuestas(resp[i], resp1[i])
            #Se imprime la cantidad de respuestas correctas que obtuvo el ususario
            return "Usted obtuvo " + str(n) + " respuestas correctas en esta prueba"
    elif numtxt == 2:
        if len(resp) != 2:
            return "El numero de caracteres ingresado excede la cantidad de preguntas \n REPITA EL EXAMEN"
        else:
            for i in range(0, len(resp)):
                n = n + suma_respuestas(resp[i], resp2[i])
            return "Usted obtuvo " + str(n) + " respuestas correctas en esta prueba"
    elif numtxt == 3:
        if len(resp) != 2:
            return "El numero de caracteres ingresado excede la cantidad de preguntas \n REPITA EL EXAMEN"
        else:
            for i in range(0, len(resp)):
                n = n + suma_respuestas(resp[i], resp3[i])
            return "Usted obtuvo " + str(n) + " respuestas correctas en esta prueba"

#Funcion del examen de lectura             
def lectura():
    #Se  randomiza el numero de texto que será usado en la prueba
    quiz = random.randint(1, 3)
    #Se define la variable que guardará el nombre del archivo 
    lectura = "texto" + str(quiz) + ".txt"
    #Se abre el archivo que contiene a la lectura
    texto1 = open(lectura, "r")
    #Se guarda el texto separandolo en un array por lineas
    textoSave = texto1.readlines()
    #Se cierra el archico
    texto1.close()
    #Se crea un ciclo que imprime cada linea del archivo original
    for i in textoSave:
        print(i)
    #Se imprimen las indicaciones
    print("**Conteste las preguntas anteriores en base al texto mostrado en pantalla ingresando las letras de la opción elegida sin espacios** \n")
    #El usuario inresa las respuestas a cada una de las preguntas
    respuesta = str(input("Ingrese los incisos en orden de aparición sin espacios: "))
    #Se imprime el resultado de llamar a la funcion comprobartxt
    print(comprobartxt(quiz, respuesta.upper()), "\n")
    
#Función del menú de consulta
def consulta ():
    print("Bienvenido a la sección de consulta \n Revisar matemáticas: pulse 1 \n Revisar ciencias: pulse 2 \n Revisar lectura: pulse 3 \n Salir de la sección: pulse 4")
    #Se guardan los links de cada tema dentro del arreglo links
    links_consulta = [["https://www.significados.com/pensamiento-matematico/#:~:text=El%20pensamiento%20matem%C3%A1tico%20es%20la,y%20el%20significado%20de%20n%C3%BAmero.",
        "https://www.portaleducativo.net/octavo-basico/778/como-resolver-una-ecuacion",
        "http://www.elabueloeduca.com/aprender/matematicas/fracciones/fracciones.html",],
        ["http://www.centroscomunitariosdeaprendizaje.org.mx/capacitacion/conferencias/quimica-basica#:~:text=La%20ciencia%20que%20estudia%20las,en%20referencia%20con%20el%20tiempo.",
        "http://www2.montes.upm.es/dptos/digfa/cfisica/",
        "https://es.khanacademy.org/science/biology"], [
        "https://guiauniversitaria.mx/8-consejos-para-mejorar-la-comprension-de-lectura/",
        "http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S1727-81202013000300014",
        "https://observatorio.tec.mx/edu-bits-blog/2017/8/21/la-comprensin-lectora-un-reto-para-alumnos-y-maestros"]]
    while True:
        consulta = int(input("Ingresa una opción: "))
        if ( consulta == 1 ):
            for link in range(0, len(links_consulta[0])):
            #Se abren links relacionados a matemáticas
                webbrowser.open(links_consulta[0][link], new=1, autoraise=True)
        elif ( consulta == 2):
             for link in range(0, len(links_consulta[0])):
                #Se abren links relacionados a ciencias
                webbrowser.open(links_consulta[1][link], new=1, autoraise=True)
        elif ( consulta == 3):
            for link in range(0, len(links_consulta[0])):
                #Se abren links relacionados a ciencias
                webbrowser.open(links_consulta[2][link], new=1, autoraise=True)       
        elif ( consulta == 4):
            #se regresa al menú
            break
    return
  
#ciclo que solo se rompe cuando el usuario es capaz de iniciar sesión
while True:
    validar = inicio_sesion()
    if validar:
        break

#Función que contiene el menú del programa
def inicio():
    while True:
        print("Bienvenido al programa de práctica de la prueba PISA \n Escoja la sección que desea practicar; \n Matemáticas: pulse 1 \n Ciencias: pulse 2 \n Lectura: pulse 3 \n Materiales de consulta: pulse 4 \n Salir del programa: pulse 5")
        #Dependiendo del valor que ingrese el ususario se iniciará el quiz del tema que necesite prácticar
        prueba=input("Escriba la prueba a la que desea ingresar ")
        #Dependiedo del valor ingresado se aplican diferentes quizes
        if prueba == "1":
            print("\n")
            mate()
        if prueba == "2":
            print("\n")
            ciencias()
        elif prueba == "3":
            print("\n")
            lectura()
        elif prueba == "4":
            print("\n")
            consulta()
        elif prueba == "5":
            print("\n")
            break
        else:
            print("***Esa función no está disponible por el momento")

#una vez que se ha roto el ciclo de inicio de sesión el usuario puede ingresar al programa       
inicio()

print("Gracias por usar este programa")

#La relación que tiene este programa con el proyecto final es que es una prueba de la funcionalidad de las preguntas aleatorias,
#haciendo que repetir un módulo de la prueba sea beneficiario al hacer que el alumno se enfrente a problemas diferentes, adicionalmente,
#con este programa pude comprobar que las funciones podían ser usadas como bloques que imrpimen un grupo de valores en la consola para de
#esta forma solo tener que llamar a una función cuando tenga que imprimir si una pregunta fue contestada correctamente.

#La relación de la segunda entrega (ciclos) con el tema es que en esta versión del programa se crea un ciclo que imprime diferentes ecuaciones
#y comprueba si las respuestas del usuario a cada ecuación son correctas, haciendo que la pregunta 4 evalue la lógica matemática del usuario
#y ayudándolo a prácticar el tema, desarrollando la competencia y ampliando sus conocimientos de álgebra. Además, con esta versión se usa un contador
#tanto dentro del ciclo como fuera de él para contar el número de respuestas correctas y darle feedback al usuario al completar su prueba.

#Con esta nueva versión del programa se incluye la versión que contiene los materiales de consulta para que los alumnos puedan revisar los 
#temas con los que necesiten ayuda al abrir una liga de consulta en su navegador. Para esto se incluye la librería webbrowser que se encarga
#de abirir URLs en el navegador.

#Con esta nueva versión se crea una base de datos de usuarios que es revisada por la función inicia sesión y si los datos no coinciden con
#los de algún usuario el programa no deja que el cliente avance y empiece a resolver el cuestionario.

#En esta versión del programa ya están habilitadas las secciones de ciencias y de comprensión lectora gracias a la implementación de 
#la lectura de archivos y el uso de strings para comparar las respuestas dadas por el ususario letra por letra, pues en la parte de lectura es necesario
#comprobar que cada uno de los incisos sean contestados con la letra correcta.