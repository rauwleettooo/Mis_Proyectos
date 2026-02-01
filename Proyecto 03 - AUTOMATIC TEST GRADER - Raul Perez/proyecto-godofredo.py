import os
nombre_todos_alumnos = {}

# FUNCIONES

# Defino la función para pedir notas del alumno
def pedir_notas(n):
    '''Pide las respuestas del alumno y las almacena en una lista'''
    respuestas_alumno = []
    contador = 1

    while contador <= n:
        respuesta = input(f"{contador}. ").strip().lower()

        if respuesta not in ["a", "b", "c", "d", ""]:  # Permite respuesta vacía
            print("Introduce una respuesta válida (a, b, c, d o deja en blanco)")
        else:
            respuestas_alumno.append(respuesta)
            contador += 1

    return respuestas_alumno

# Función para establecer las respuestas correctas
def resp_correctas(n):
    '''Solicita y almacena las respuestas correctas'''
    respuestas_correctas = []
    contador = 1

    while contador <= n:
        respuesta = input(f"{contador}. ").strip().lower()

        if respuesta not in ["a", "b", "c", "d"]:
            print("Introduce una respuesta válida (a, b, c o d)")
        else:
            respuestas_correctas.append(respuesta)
            contador += 1

    return respuestas_correctas

# Función para comparar respuestas y calcular la nota
def comparar_respuestas(respuestas_alumno, respuestas_correctas, num):
    '''Compara las respuestas del alumno con las correctas y calcula la nota'''
    correctas = 0
    incorrectas = 0
    vacias = 0

    for alumno, correcta in zip(respuestas_alumno, respuestas_correctas):
        if alumno == correcta:
            correctas += 1
        elif alumno == "":  
            vacias += 1
        else:
            incorrectas += 1

    # Calculamos la nota solo con las respuestas contestadas (sin contar vacías)
    total_contestadas = correctas + incorrectas + vacias
    if total_contestadas > 0:
        valor_correctas = 10 / total_contestadas
        valor_incorrectas = valor_correctas / 3  # Penalización de 1/3 por error
        nota = (correctas * valor_correctas) - (incorrectas * valor_incorrectas)
        nota = max(nota, 0)  
    else:
        nota = 0  # Si no respondió nada, la nota es 0

    return correctas, incorrectas, vacias, round(nota, 2)

# -------------------------------------------------------------------------------------------------------------------------
# PROGRAMA
#bienvenida
print("="*50)
print("Bienvenido al corrector automatico de examenes")
print("="*50)
input("")
while True:
    

    os.system("cls")
    
    num = int(input("¿Cuántas preguntas tiene el examen? "))
    
    print("Introduce las respuestas correctas del examen:")
    respuestas_correctas = resp_correctas(num)

    os.system("cls")

    print("\nAhora, introduce las respuestas de los alumnos")

    num_alumnos = int(input("Introduce el número de alumnos: "))

    for i in range(num_alumnos):
        nombre = input(f"\nIntroduce el nombre del alumno {i + 1}: ")
        os.system("cls")

        print(f"Introduce las respuestas de {nombre}:")
        respuestas_alumno = pedir_notas(num)

        correctas, incorrectas, vacias, nota = comparar_respuestas(respuestas_alumno, respuestas_correctas, num)

        print(f"{nombre} ha acertado {correctas}, ha fallado {incorrectas}, dejó {vacias} en blanco. Ha sacado un {nota}.")
        nombre_todos_alumnos[nombre] = nota

    # Mostrar resultados finales
    os.system("cls")
    print("="*50)
    print("Notas finales de los alumnos:")
    print("="*50)
    for alumno, nota in nombre_todos_alumnos.items():
        print(f"{alumno}: {nota}")

    salida = int(input("Pulse 1 para salir o pulse 0 para seguir corrigiendo: "))
    if salida == 1:
        print("Gracias por usar esta aplicación.")
        input()
        break  
    elif salida == 0:
        input("Presiona ENTER para continuar corrigiendo.")
        os.system("cls")  
    else:
        print("Introduce una opción válida (0 o 1).")
        os.system("cls")