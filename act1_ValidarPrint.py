#ACTIVIDAD 1: Validación simple de una instrucción
#YESHUA NEFTALI ESPINOZA GONZÁLEZ
#SEMINARIO DE SOLUCIÓN DE TRADUCTORES DE LENGUAJE II

def validar_instruccion(instruccion):
    # Verificar si la instrucción comienza con 'print('
    if not instruccion.startswith("print("):
        if not instruccion.startswith("print"):
            return "UPS! La instrucción no contiene la palabra 'print' completa."
        elif not instruccion.startswith("print("):
            return "UPS! Falta el carácter '(' después de 'print'."

    # Verificar si la instrucción termina con ')'
    if not instruccion.endswith(")"):
        return "UPS! La instrucción no termina con ')'."
    
    # Extraer el contenido entre los paréntesis
    contenido = instruccion[6:-1].strip()
    
    # Verificar si el contenido está entre comillas
    if not ((contenido.startswith('"') and contenido.endswith('"')) or
            (contenido.startswith("'") and contenido.endswith("'"))):
        if not (contenido.startswith('"') or contenido.startswith("'")):
            return "UPS! Falta la comilla de apertura."
        elif not (contenido.endswith('"') or contenido.endswith("'")):
            return "UPS! Falta la comilla de cierre."
    
    # Verificar si el contenido es una cadena válida
    if len(contenido) < 2:
        return "UPS! La cadena dentro de print está vacía o no es válida."

    return "Instrucción válida."

print("Ingresa una instrucción print para validar:")
instruccion_usuario = input()
resultado = validar_instruccion(instruccion_usuario)
print(resultado)
