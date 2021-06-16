#PREPARACION DE NOMBRE PARA TOKENS
reservadas = {
    'print':'RPRINT',
    'var': 'RVAR',
    'new':'NEW',

    #datos primitivos
    'true':'RTRUE',
    'false':'RFALSE',
    'null':'RNULL',
    'double':'RDOUBLE',
    'int':'RINT',
    'boolean':'RBOOLEAN',
    'char':'RCHAR',
    'string':'RSTRING',


    #ciclos, bucles , condicionales
    'if':'RIF',
    'else':'RELSE',
    'switch':'RSWITCH',
    'case':'RCASE',
    'default':'RDEFAULT',


    'while':'RWHILE',
    'for':'RFOR',
    'break':'RBREAK',
    'continue':'RCONTINUE',
    'return':'RRETURN',

    'func':'RFUNC',
    'read':'RREAD',

    'tolower':'RTOLOWER',
    'toupper':'RTOUPPER',

    'length':'RLENGTH',
    'truncate':'RTRUNCATE',
    'round':'RROUND',
    'typeof':'RTYPEOF',
    'main':'RMAIN',



}


tokens = [
    #operadores aritemticos
    'SIGNOMAS',
    'SIGNOMENOS',
    'SIGNOMULTIPLICACION',
    'SIGNODIVISION',
    'SIGNOPOTENCIA',
    'SIGNOMODULO',

    # OPERADORES
    'SIGNOIGUALACION',
    'SIGNODIFERENCIA',
    'SIGNOMENORQUE',
    'SIGNOMAYORQUE',
    'SIGNOMENORIGUAL',
    'SIGNOMAYORIGUAL',
    #OPERADORES LOGICOS
    'OR',
    'AND',
    'NOT',

    #SPECIAL CARACTER
    'DOSPUNTOS',

    #COMENTARIOS
    'COMENTARIOSUNALINEA',
    'COMENTARIOSMULTILINEA',

    #SIGNO S DE AGRUPACION
    'PARENTESISABRE',
    'PARENTESISCIERRA',

    #CARACTERES DE FINALIZACION
    'PUNTOYCOMA',
    'LLAVEABRE',
    'LLAVECIERRA',

    # DECLARACION Y ASIGNACION DE VARIABLES
    'SIMBOLOIGUAL',
    #INCREMENTEO Y DECREMENTO
    'INCREMENTO',
    'DECREMENTO',

    #ARREGLOS
    'CORCHETEABRE',
    'CORCHETECIERRA',

    #TIPOS DE DATOS PRIMITIVOS

    'ENTEROS',
    'DECIMAL',
    'CARACTER',
    'CADENA',
    'ID',
]+list(reservadas.values())

#ASIGNACION DE TOKENS
# OPERADORES ARITMETICOS
t_SIGNOMAS = r'\+'
t_SIGNOMENOS = r'-'
t_SIGNOMULTIPLICACION = r'\*'
t_SIGNODIVISION = r'/'
t_SIGNOPOTENCIA = r'\^'
t_SIGNOMODULO = r'%'
# operadores
t_SIGNOIGUALACION = r'=='
t_SIGNODIFERENCIA = r'!='
t_SIGNOMENORQUE= r'<'
t_SIGNOMAYORQUE=r'>'
t_SIGNOMENORIGUAL=r'<='
t_SIGNOMAYORIGUAL=r'>='
#operadores logicos
t_OR = r'\|'
t_AND= r'&'
t_NOT= r'~'
#caracteres especiales
t_DOSPUNTOS= r':'
#signos de agrupacion
t_PARENTESISABRE= r'\('
t_PARENTESISCIERRA =r'\)'

#caracteres de finalizacion
t_PUNTOYCOMA=r';'
t_LLAVEABRE=r'\{'
t_LLAVECIERRA=r'\}'
#declaracion simbolo igual
t_SIMBOLOIGUAL = r'='
#incremento y decremento
t_INCREMENTO = r'++'
t_DECREMENTO = r'--'
#tipos de datos primitivos
#enteros
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t
#decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t
#caracter

#Cadena
def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t
#ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  # Check for reserved words
    return t

#comentarios
def t_COMENTARIOSMULTILINEA(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count('\n')

def t_COMENTARIOSUNALINEA(t):
    r'\#.*\n'
    t.lexer.lineno += 1