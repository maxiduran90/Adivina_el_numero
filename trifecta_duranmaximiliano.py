def iniciar_programa():
    entrada = input("Ingresa un número entero: ")

    try:
        # Intentamos convertir la entrada a un número entero
        numero = int(entrada)
        
        # Evaluamos el número
        if numero != 0:
            print(f"Número ingresado: {numero}. ¡El programa ha iniciado!")
            # Aquí puedes agregar el resto de tu código
        else:
            print("Se ingresó un 0. El programa finalizará.")
            
    except ValueError:
        # Esto captura el error si el usuario ingresa texto o un número decimal
        print("Entrada inválida. No es un número entero. El programa finalizará.")

if __name__ == "__main__":
    iniciar_programa()



# Solicitamos la palabra o frase al usuario
texto = input("Ingresa una palabra o frase: ")
# Contamos los caracteres con la función len()
cantidad_caracteres = len(texto)

# Mostramos el resultado en pantalla
print(f"La cantidad de caracteres es: {cantidad_caracteres}")



import math

n = 9  # Reemplaza esto con el número que necesites

# Calcular el factorial
factorial = math.factorial(n)

# Comprobar si es par o impar
if factorial % 2 == 0:
    resultado_paridad = "par"
else:
    resultado_paridad = "impar"

print(f"El factorial de {n} es {factorial}, y es un número {resultado_paridad}.")



def main():
    entrada = input("Ingresa un número entero: ")
    
    try:
        # Intentamos convertir la entrada a un número entero
        numero = int(entrada)
        
        # Verificamos si es distinto de cero
        if numero != 0:
            print(f"¡Número {numero} ingresado! El programa ha iniciado.")
            # Aquí va el resto de tu código principal
        else:
            print("Se ingresó un 0. El programa finalizará.")
            
    except ValueError:
        # Esto captura el error si ingresan texto, decimales o caracteres especiales
        print("Entrada inválida. No es un número entero. El programa finalizará.")

if __name__ == "__main__":    main()