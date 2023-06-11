def run():
    """
    Introduce una palabra, el programa va imprimir letra por letra 
    de la palabra que introduciste hasta que encuentre la letra O,
    cuando la encuentre el porgrama se cerrará haciendo un break 
    saliendo del ciclo
    """
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()