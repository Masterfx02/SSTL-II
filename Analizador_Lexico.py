import re

# Definición de tipos de tokens
class TipoToken:
    TIPO_DATO = 0
    IDENTIFICADOR = 1
    CONSTANTE = 2
    PUNTO_Y_COMA = 3
    COMA = 4
    PARENTESIS_IZQUIERDO = 5
    PARENTESIS_DERECHO = 6
    LLAVE_IZQUIERDA = 7
    LLAVE_DERECHA = 8
    IGUAL = 9
    IF = 10
    WHILE = 11
    RETURN = 12
    ELSE = 13
    FOR = 14
    OP_ADICION = 15
    OP_MULTIPLICACION = 16
    OP_LOGICO = 17
    OP_RELACIONAL = 18
    CADENA = 19  # Token para cadenas de texto
    FIN = 20

# Mapeo de los tipos numéricos a sus nombres
token_nombre = {
    TipoToken.TIPO_DATO: "TIPO_DATO",
    TipoToken.IDENTIFICADOR: "IDENTIFICADOR",
    TipoToken.CONSTANTE: "CONSTANTE",
    TipoToken.PUNTO_Y_COMA: "PUNTO_Y_COMA",
    TipoToken.COMA: "COMA",
    TipoToken.PARENTESIS_IZQUIERDO: "PARENTESIS_IZQUIERDO",
    TipoToken.PARENTESIS_DERECHO: "PARENTESIS_DERECHO",
    TipoToken.LLAVE_IZQUIERDA: "LLAVE_IZQUIERDA",
    TipoToken.LLAVE_DERECHA: "LLAVE_DERECHA",
    TipoToken.IGUAL: "IGUAL",
    TipoToken.IF: "IF",
    TipoToken.WHILE: "WHILE",
    TipoToken.RETURN: "RETURN",
    TipoToken.ELSE: "ELSE",
    TipoToken.FOR: "FOR",
    TipoToken.OP_ADICION: "OP_ADICION",
    TipoToken.OP_MULTIPLICACION: "OP_MULTIPLICACION",
    TipoToken.OP_LOGICO: "OP_LOGICO",
    TipoToken.OP_RELACIONAL: "OP_RELACIONAL",
    TipoToken.CADENA: "CADENA",
    TipoToken.FIN: "FIN"
}

# Estructura para representar un token
class Token:
    def __init__(self, tipo, lexema):
        self.tipo = tipo
        self.lexema = lexema

# Función para escanear el código fuente y generar tokens
def obtener_siguiente_token(codigo, indice):
    token = Token(TipoToken.FIN, "")
    patrones = [
        (TipoToken.TIPO_DATO, r'\b(int|float|char|void|string)\b'),
        (TipoToken.IF, r'\bif\b'),
        (TipoToken.WHILE, r'\bwhile\b'),
        (TipoToken.RETURN, r'\breturn\b'),
        (TipoToken.ELSE, r'\belse\b'),
        (TipoToken.FOR, r'\bfor\b'),
        (TipoToken.CONSTANTE, r'\b\d+(\.\d+)?\b|\bpi\b'),
        (TipoToken.IDENTIFICADOR, r'[A-Za-z_][A-Za-z0-9_]*'),
        (TipoToken.OP_ADICION, r'[+-]'),
        (TipoToken.OP_MULTIPLICACION, r'[*\/]|<<|>>'),
        (TipoToken.OP_LOGICO, r'&&|\|\|'),
        (TipoToken.OP_RELACIONAL, r'[<>]=?|==|!='),
        (TipoToken.CADENA, r'"[^"]*"'),  # Regla para cadenas
        (TipoToken.PUNTO_Y_COMA, r';'),
        (TipoToken.COMA, r','),
        (TipoToken.PARENTESIS_IZQUIERDO, r'\('),
        (TipoToken.PARENTESIS_DERECHO, r'\)'),
        (TipoToken.LLAVE_IZQUIERDA, r'\{'),
        (TipoToken.LLAVE_DERECHA, r'\}'),
        (TipoToken.IGUAL, r'='),
        (TipoToken.FIN, r'\$')
    ]

    while indice[0] < len(codigo):
        if codigo[indice[0]] == ' ':
            indice[0] += 1
            continue

        for tipo, patron in patrones:
            match = re.match(patron, codigo[indice[0]:])
            if match:
                lexema = match.group(0)
                token.tipo = tipo
                token.lexema = lexema
                indice[0] += len(lexema)
                return token
    return token

# El usuario ingresa la cadena
codigo = input("Introduce una cadena de código a validar: ")
indice = [0]

print("Código fuente:", codigo)
print("Tokens generados:")

# Proceso de escaneo y generación de tokens
while True:
    token = obtener_siguiente_token(codigo, indice)
    if token.tipo == TipoToken.FIN:
        print("Tipo: FIN")
        break
    else:
        # Imprimir el tipo de token junto con su nombre y el lexema
        print(f"Tipo: {token.tipo} ({token_nombre[token.tipo]}), Lexema: {token.lexema}")