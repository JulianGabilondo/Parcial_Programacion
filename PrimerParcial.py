pacientes = []

# Función para verificar si hay pacientes registrados
def verificar_pacientes_registrados():
    if len(pacientes) == 0:
        print("No hay pacientes registrados, para la operacion solicitada\n")
        return False
    return True

# Función para solicitar un número entero con validación
def solicitar_numero(mensaje, mensaje_error="Por favor ingrese un número válido"):
    while True:
        # Solicitamos el input
        valor = input(mensaje)
        
        # Verificamos si es un número entero
        if valor.isdigit() or (valor.startswith('-') and valor[1:].isdigit()):
            return int(valor)  
        else:
            print(mensaje_error)

# Función para cargar múltiples pacientes
def cargar_pacientes():
    cantidad_pacientes = solicitar_numero("\nIngrese la cantidad de pacientes a registrar: ", "Por favor ingrese un número positivo para la cantidad de pacientes.")
    
    if cantidad_pacientes <= 0:
        print("Por favor ingrese un número positivo para la cantidad de pacientes.\n")
        return
    
    for _ in range(cantidad_pacientes):
        print("\n-+- Ingreso de Datos del Paciente -+-")
        # Solicitamos los datos del paciente
        numero_historia_clinica = solicitar_numero("Ingrese el número de historia clínica: ")
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        edad_paciente = solicitar_numero("Ingrese la edad del paciente: ")
        diagnostico = input("Ingrese el diagnóstico: ")
        dias_internacion = solicitar_numero("Ingrese la cantidad de días de internación: ")
        
        # Añadimos los datos del paciente como una nueva fila 
        paciente = [numero_historia_clinica, nombre_paciente, edad_paciente, diagnostico, dias_internacion]
        pacientes.append(paciente)
    print(f"{cantidad_pacientes} pacientes registrados con éxito.\n")

# Función para mostrar los pacientes almacenados
def mostrar_pacientes():
    print("\n-+- Pacientes Registrados -+-")
    if verificar_pacientes_registrados():
        # Tabla
        print(f"{'Historia clínica':<18} | {'Nombre':<25} | {'Edad':<4} | {'Diagnóstico':<15} | {'Días de Internación':<17}")
        print("-" * 80)  # Línea de separacion para que se vea la tabla 

        for paciente in pacientes:
            # Ajustamos la tabla para que se vea de forma simetrica (asi se ve un poco mas linda jaja)
            print(f"{paciente[0]:<18} | {paciente[1]:<25} | {paciente[2]:<4} | {paciente[3]:<15} | {paciente[4]:<17}")
    else:
        print("No hay pacientes registrados.")
    print()  # Salto de línea al final

# Función para buscar un paciente por su número de historia clínica
def buscar_paciente_por_historia_clinica():
    if not verificar_pacientes_registrados():
        return

    print("\n-+- Buscar paciente por Historia Clínica -+-")
    numero_historia_clinica = solicitar_numero("Ingrese el número de historia clínica del paciente a buscar: ")
    encontrado = False
    for paciente in pacientes:
        if paciente[0] == numero_historia_clinica:
            print(f"\nPaciente encontrado:")
            print(f"Historia clínica: {paciente[0]}")
            print(f"Nombre: {paciente[1]}")
            print(f"Edad: {paciente[2]}")
            print(f"Diagnóstico: {paciente[3]}")
            print(f"Días de internación: {paciente[4]}\n")
            encontrado = True
            break
    if not encontrado:
        print("Paciente no encontrado.\n")

# Función para determinar el paciente con más días de internación
def paciente_con_mas_dias_internacion():
    if not verificar_pacientes_registrados():
        return

    paciente_mas_dias = pacientes[0]  # Siempre tomo el primer paciente para comprobar (ya sea con mas o menos dias)
    for paciente in pacientes:
        if paciente[4] > paciente_mas_dias[4]:  # Comparamos los días de internación
            paciente_mas_dias = paciente

    print("\n-+- Paciente con más días de internación -+-")
    print(f"Historia clínica: {paciente_mas_dias[0]}")
    print(f"Nombre: {paciente_mas_dias[1]}")
    print(f"Edad: {paciente_mas_dias[2]}")
    print(f"Diagnóstico: {paciente_mas_dias[3]}")
    print(f"Días de internación: {paciente_mas_dias[4]}\n")

# Función para determinar el paciente con menos días de internación
def paciente_con_menos_dias_internacion():
    if not verificar_pacientes_registrados():
        return

    paciente_menos_dias = pacientes[0]  # Realizo lo mismo que dije en la linea 85
    for paciente in pacientes:
        if paciente[4] < paciente_menos_dias[4]:  # Comparamos los días de internación
            paciente_menos_dias = paciente

    print("\n-+- Paciente con menos días de internación -+-")
    print(f"Historia clínica: {paciente_menos_dias[0]}")
    print(f"Nombre: {paciente_menos_dias[1]}")
    print(f"Edad: {paciente_menos_dias[2]}")
    print(f"Diagnóstico: {paciente_menos_dias[3]}")
    print(f"Días de internación: {paciente_menos_dias[4]}\n")

# Función para contar la cantidad de pacientes con más de 5 días de internación
def contar_pacientes_mas_de_5_dias():
    if not verificar_pacientes_registrados():
        return

    contador = 0
    for paciente in pacientes:
        if paciente[4] > 5:
            contador += 1

    print(f"\n-+- Pacientes con más de 5 días de internación -+-")
    print(f"Cantidad de pacientes con más de 5 días de internación: {contador}\n")

# Función para calcular el promedio de días de internación
def calcular_promedio_dias_internacion():
    if not verificar_pacientes_registrados():
        return

    total_dias = sum(paciente[4] for paciente in pacientes)
    promedio = total_dias / len(pacientes)

    print(f"\n-+- Promedio de días de internación -+-")
    print(f"El promedio de días de internación de todos los pacientes es: {promedio:.2f} días\n")

# Función para ordenar los pacientes por número de historia clínica 
def ordenar_pacientes():
    if not verificar_pacientes_registrados():
        return

    # Ordenamos usando el algoritmo de ordenamiento por inserción
    for i in range(1, len(pacientes)):
        clave = pacientes[i]
        j = i - 1
        # Mover los elementos de pacientes[0..i-1], que son mayores que la clave, a una posición adelante
        while j >= 0 and pacientes[j][0] > clave[0]:
            pacientes[j + 1] = pacientes[j]
            j -= 1
        pacientes[j + 1] = clave

    print("\n-+- Pacientes ordenados por número de historia clínica -+-")
    mostrar_pacientes()

# Menú de opciones para interactuar con el sistema
def menu():
    while True:
        print("-+- Sistema de Gestión de Pacientes -+-")
        print("1. Cargar pacientes")
        print("2. Mostrar pacientes")
        print("3. Buscar paciente por número de historia clínica")
        print("4. Mostrar paciente con más días de internación")
        print("5. Mostrar paciente con menos días de internación")
        print("6. Cantidad de pacientes con más de 5 días de internación")
        print("7. Promedio de días de internación de todos los pacientes")
        print("8. Ordenar pacientes por número de historia clínica")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_pacientes()
        elif opcion == "2":
            mostrar_pacientes()
        elif opcion == "3":
            buscar_paciente_por_historia_clinica()
        elif opcion == "4":
            paciente_con_mas_dias_internacion()
        elif opcion == "5":
            paciente_con_menos_dias_internacion()
        elif opcion == "6":
            contar_pacientes_mas_de_5_dias()
        elif opcion == "7":
            calcular_promedio_dias_internacion()
        elif opcion == "8":
            ordenar_pacientes()
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

# Ejecutar el menú
menu()