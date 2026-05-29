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

if __name__ == "__main__":
    main()
