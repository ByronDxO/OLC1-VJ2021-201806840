''' 
José Puac
VACACIONES DE JUNIO 2020

INTERPRETER SAMPLE  
'''
import re
from TS.Excepcion import Excepcion

errores = []
reservadas = {
    'int'       : 'RINT',
    'float'     : 'RFLOAT',
    'string'    : 'RSTRING',
    'boolean'   : 'RBOOLEAN',
    'var'       : 'RVAR',
    'print'     : 'RPRINT',
    'for'       :  'RFOR',
    'if'        : 'RIF',
    'else'      : 'RELSE',
    'while'     : 'RWHILE',
    'true'      : 'RTRUE',
    'false'     : 'RFALSE',
    'break'     : 'RBREAK',
    'main'      : 'RMAIN',
    'func'      : 'RFUNC',
    'return'    : 'RRETURN',
    'null'      : 'RNULL',

}

tokens  = [
    'PUNTOCOMA',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
    'COMA',
    'MAS',
    'MENOS',
    'POR',
    'MENORQUE',
    'MAYORQUE',
    'IGUALIGUAL',
    'IGUAL',
    'DIFERENTE',
    'AND',
    'OR',
    'NOT',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'ID',
    'MENORIGUAL',
    'MAYORIGUAL',
    'POT',
    'DIV',
    'MOD',
    'INCREMENTO',
    'DECREMENTO',
    'COMENTARIO_MULTI',
    'COMENTARIO_SIMPLE',
    'CHARACTER'



] + list(reservadas.values())

# Tokens
t_PUNTOCOMA     = r';'
t_PARA          = r'\('
t_PARC          = r'\)'
t_LLAVEA        = r'{'
t_LLAVEC        = r'}'
t_COMA          = r','
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_MENORQUE      = r'<'
t_MAYORQUE      = r'>'
t_IGUALIGUAL    = r'=='
t_IGUAL         = r'='
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_DIFERENTE     = r'!='
t_MENORIGUAL    = r'<='
t_MAYORIGUAL    = r'>='
t_POT           = r'\*\*'
t_DIV           = r'\/'
t_MOD           = r'\%'
t_INCREMENTO    = r'\+\+'
t_DECREMENTO    = r'--'
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] # remuevo las comillas
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace("\\'", '\'')
    return t
def t_CHARACTER(t):
    r"""\' (\\'| \\\\ | \\n | \\t | \\r | \\" | .)? \'"""
    t.value = t.value[1:-1] # remuevo las comillas
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace("\\'", '\'')
    return t
def t_COMENTARIO_MULTI(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count("\n")
# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1
#COMENTARIO MULTILINEA

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex(reflags= re.IGNORECASE)

# Asociación de operadores y precedencia
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UNOT'),
    ('left','MENORQUE','MAYORQUE','IGUALIGUAL','DIFERENTE','MENORIGUAL','MAYORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','POR','DIV','MOD'),
    ('left','POT'),
    ('right','UMENOS'),
    ('left','INCREMENTO','DECREMENTO')
    )

# Definición de la gramática

#Abstract
from Abstract.Instruccion import Instruccion
from Instrucciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos
from TS.Tipo import OperadorAritmetico, OperadorLogico, TIPO, OperadorRelacional
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Instrucciones.Declaracion import Declaracion
from Expresiones.Identificador import Identificador
from Instrucciones.Asignacion import Asignacion
from Instrucciones.If import If
from Instrucciones.While import While
from Instrucciones.Break import Break
from Instrucciones.Main import Main
from Instrucciones.Funcion import Funcion
from Instrucciones.Llamada import Llamada
from Instrucciones.Return import Return
from Instrucciones.For import  For
from Instrucciones.Decremento_incremento import Decremento_incremento
from Instrucciones.Case import  Case
from Instrucciones.Default import  Default
from Instrucciones.Switch import Switch
from Instrucciones.Continue import Continue

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t) :
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    
#///////////////////////////////////////INSTRUCCIONES//////////////////////////////////////////////////

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

#///////////////////////////////////////INSTRUCCION//////////////////////////////////////////////////

def p_instruccion(t) :
    '''instruccion      : imprimir_instr finins
                        | declaracion_instr
                        | asignacion_instr finins
                        | incre_decre_ins finins
                        | if_instr
                        | for_instr
                        | while_instr
                        | switch_instr
                        | break_instr finins
                        | main_instr
                        | funcion_instr
                        | llamada_instr finins
                        | return_instr finins'''
    t[0] = t[1]

def p_finins(t) :
    '''finins       : PUNTOCOMA
                    | '''
    t[0] = None

def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
    errores.append(Excepcion("Sintáctico","Error Sintáctico." + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""
#///////////////////////////////////////decre_incre//////////////////////////////////////////////////
def p_decremento_incremento(t):
    ''' incre_decre_ins : ID DECREMENTO
                        | ID INCREMENTO'''

    if t[2] == '--':
        t[0] = Decremento_incremento(t[1], OperadorAritmetico.DECREMENTO, t.lineno(1), find_column(input, t.slice[1]))
    elif t[2] == '++':
        t[0] = Decremento_incremento(t[1], OperadorAritmetico.INCREMENTO, t.lineno(1), find_column(input, t.slice[1]))


#///////////////////////////////////////IMPRIMIR//////////////////////////////////////////////////

def p_imprimir(t) :
    'imprimir_instr     : RPRINT PARA expresion PARC'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////DECLARACION//////////////////////////////////////////////////
#declaracion para nones
def p_declaracion(t) :
    ''' declaracion_instr : declaracion_none
                        | declaracion_entr finins'''
    t[0] = t[1]
def p_declaracion_none(t):
    '''declaracion_none  : tipo ID finins '''
    t[0] = Declaracion(t[1], t[2], t.lineno(2), find_column(input, t.slice[2]))

def p_declaracion_entr(t) :
    'declaracion_entr     : tipo ID IGUAL expresion'
    t[0] = Declaracion(t[1], t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])


#///////////////////////////////////////ASIGNACION//////////////////////////////////////////////////

def p_asignacion(t) :
    'asignacion_instr     : ID IGUAL expresion'
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////SWITCH//////////////////////////////////////////////////
def p_condicion_switch_case_list_default(t): # Aqui verifiac que la condicion venga  [<CASES_LIST>] [<DEFAULT>]
    'switch_instr   : RSWITCH PARA expresion PARC LLAVEA case_switch_ins default_switch LLAVEC'
    t[0] = Switch(t[3], t[6], t[7] ,t.lineno(1), find_column(input, t.slice[1]))

def p_condicion_switch_case_list(t): # Aqui verifiac que la condicion venga  [<CASES_LIST>]
    'switch_instr   : RSWITCH PARA expresion PARC LLAVEA case_switch_ins LLAVEC'
    t[0] = Switch(t[3], t[6], None, t.lineno(1), find_column(input, t.slice[1]))

def p_condicion_switch_default(t): # Aqui verifiac que la condicion venga   [<DEFAULT>]
    'switch_instr   : RSWITCH PARA expresion PARC LLAVEA default_switch LLAVEC'
    t[0] = Switch(t[3], None, t[6], t.lineno(1), find_column(input, t.slice[1]))

def p_casos_switch_ins_caso_switch(t): # Aqui hace a que sea recursivo y puedan venir infinitos [<CASES_LIST>]
    'case_switch_instr : case_switch_ins case_switch'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_caso_switch_(t):
    'case_switch_ins : case_switch'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_condicion_switch_case(t):
    'case_switch  : RCASE expresion DOSPUNTOS instrucciones'
    t[0] = Case(t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))

def p_condicion_default_switch(t):
    'default_switch : RDEFAULT DOSPUNTOS instrucciones'
    # t[0] = t[3]
    t[0] = Default(t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////IF//////////////////////////////////////////////////

def p_if1(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_if2(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], t[10], None, t.lineno(1), find_column(input, t.slice[1]))

def p_if3(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr'
    t[0] = If(t[3], t[6], None, t[9], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////FOR//////////////////////////////////////////////////
def p_declarar_asignar_for(t):
    '''declarar_asignar_for :   declaracion_instr
                            |   asignacion_instr

    '''
    t[0] = t[1]
def p_actualizacion_for(t):
    '''actualizacion_for    : asignacion_instr
                            | incre_decre_ins

    '''
    t[0] = t[1]
def p_for(t):
    'for_instr : RFOR PARA  declarar_asignar_for PUNTOCOMA expresion PUNTOCOMA actualizacion_for PARC LLAVEA  instrucciones LLAVEC'
    t[0] = For(t[3],t[5],t[7],t[10],t.lineno(1),find_column(input,t.slice[1]))
#///////////////////////////////////////WHILE//////////////////////////////////////////////////

def p_while(t) :
    'while_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = While(t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////BREAK//////////////////////////////////////////////////

def p_break(t) :
    'break_instr     : RBREAK'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))
#///////////////////////////////////////RETURN//////////////////////////////////////////////////
def p_return_instruccion(t):
    'return_ins     :  RRETURN expresion'
    t[0] = Return(t[2],t.lineno(1),find_column(input, t.slice[1]))
#///////////////////////////////////////CONTINUE//////////////////////////////////////////////////
def p_continue_instruccion(t):
    'continue_ins   :   RCONTINUE'
    t[0] = Continue(t.lineno(1),find_column(input,t.slice[1]))

#///////////////////////////////////////MAIN//////////////////////////////////////////////////

def p_main(t) :
    'main_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Main(t[5], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////FUNCION//////////////////////////////////////////////////

def p_funcion_1(t) :
    'funcion_instr     : RFUNC ID PARA parametros PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], t[4], t[7], t.lineno(1), find_column(input, t.slice[1]))

def p_funcion_2(t) :
    'funcion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], [], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////PARAMETROS//////////////////////////////////////////////////

def p_parametros_1(t) :
    'parametros     : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_parametros_2(t) :
    'parametros    : parametro'
    t[0] = [t[1]]

#///////////////////////////////////////PARAMETRO//////////////////////////////////////////////////

def p_parametro(t) :
    'parametro     : tipo ID'
    t[0] = {'tipo':t[1],'identificador':t[2]}

#///////////////////////////////////////LLAMADA A FUNCION//////////////////////////////////////////////////

def p_llamada1(t) :
    'llamada_instr     : ID PARA PARC'
    t[0] = Llamada(t[1], [], t.lineno(1), find_column(input, t.slice[1]))

def p_llamada2(t) :
    'llamada_instr     : ID PARA parametros_llamada PARC'
    t[0] = Llamada(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////PARAMETROS LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametrosLL_1(t) :
    'parametros_llamada     : parametros_llamada COMA parametro_llamada'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_parametrosLL_2(t) :
    'parametros_llamada    : parametro_llamada'
    t[0] = [t[1]]

#///////////////////////////////////////PARAMETRO LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametroLL(t) :
    'parametro_llamada     : expresion'
    t[0] = t[1]

#///////////////////////////////////////LLAMADA A FUNCION//////////////////////////////////////////////////

def p_return(t) :
    'return_instr     : RRETURN expresion'
    t[0] = Return(t[2], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////TIPO//////////////////////////////////////////////////

def p_tipo(t) :
    '''tipo     : RINT
                | RFLOAT
                | RSTRING
                | RBOOLEAN
                | RVAR
                '''
    if t[1].lower() == 'int':
        t[0] = TIPO.ENTERO
    elif t[1].lower() == 'float':
        t[0] = TIPO.DECIMAL
    elif t[1].lower() == 'string':
        t[0] = TIPO.CADENA
    elif t[1].lower() == 'boolean':
        t[0] = TIPO.BOOLEANO
    elif t[1].lower() == 'char':
        t[0] = TIPO.CHARACTER
    elif t[1].lower() == 'var':
        t[0] = TIPO.NULO

#///////////////////////////////////////EXPRESION//////////////////////////////////////////////////

def p_expresion_binaria(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIV expresion
            | expresion MOD expresion
            | expresion POT expresion
            | expresion MENORQUE expresion
            | expresion MAYORQUE expresion
            | expresion IGUALIGUAL expresion
            | expresion DIFERENTE expresion
            | expresion MENORIGUAL expresion
            | expresion MAYORIGUAL expresion
            | expresion AND expresion
            | expresion OR expresion
    '''
    if t[2] == '+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/':
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MOD, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '**':
        t[0] = Aritmetica(OperadorAritmetico.POT, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '!=':
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENORIGUAL, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))

def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS 
            | NOT expresion %prec UNOT 
    '''
    if t[1] == '-':
        t[0] = Aritmetica(OperadorAritmetico.UMENOS, t[2],None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Logica(OperadorLogico.NOT, t[2],None, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_agrupacion(t):
    '''
    expresion :   PARA expresion PARC 
    '''
    t[0] = t[2]

def p_expresion_llamada(t):
    '''expresion : llamada_instr'''
    t[0] = t[1]

def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(TIPO.ENTERO,t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(TIPO.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(TIPO.CADENA,str(t[1]), t.lineno(1), find_column(input, t.slice[1]))

def p_exprecion_character(t):
    '''expresion : CHARACTER'''
    t[0] = Primitivos(TIPO.CHARACTER, str(t[1]), t.lineno(1), find_column(input, t.slice[1]))
def p_expresion_true(t):
    '''expresion : RTRUE'''
    t[0] = Primitivos(TIPO.BOOLEANO, True, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_false(t):
    '''expresion : RFALSE'''
    t[0] = Primitivos(TIPO.BOOLEANO, False, t.lineno(1), find_column(input, t.slice[1]))
def p_expresion_null(t):
    '''expresion : RNULL'''
    t[0] = Primitivos(TIPO.NULO, None, t.lineno(1), find_column(input, t.slice[1]))


import ply.yacc as yacc
parser = yacc.yacc()

input = ''

def getErrores():
    return errores

def parse(inp) :
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex(reflags= re.IGNORECASE)
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

#INTERFAZ

def interprete_perron(cadena):

    entrada = cadena

    from TS.Arbol import Arbol
    from TS.TablaSimbolos import TablaSimbolos

    instrucciones = parse(entrada) # ARBOL AST
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolos()
    ast.setTSglobal(TSGlobal)
    for error in errores:                   # CAPTURA DE ERRORES LEXICOS Y SINTACTICOS
        ast.getExcepciones().append(error)
        ast.updateConsola(error.toString())

    for instruccion in ast.getInstrucciones():      # 1ERA PASADA (DECLARACIONES Y ASIGNACIONES)
        if isinstance(instruccion, Funcion):
            ast.addFuncion(instruccion)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
        if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion):
            value = instruccion.interpretar(ast,TSGlobal)
            if isinstance(value, Excepcion) :
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())
            if isinstance(value, Break):
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())

    for instruccion in ast.getInstrucciones():      # 2DA PASADA (MAIN)
        contador = 0
        if isinstance(instruccion, Main):
            contador += 1
            if contador == 2: # VERIFICAR LA DUPLICIDAD
                err = Excepcion("Semantico", "Existen 2 funciones Main", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
                break
            value = instruccion.interpretar(ast,TSGlobal)
            if isinstance(value, Excepcion) :
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())
            if isinstance(value, Break):
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
            if isinstance(value, Return):
                err = Excepcion("Semantico", "Sentencia RETURN fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())

    for instruccion in ast.getInstrucciones():    # 3ERA PASADA (SENTENCIAS FUERA DE MAIN)
        if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion, Funcion)):
            err = Excepcion("Semantico", "Sentencias fuera de Main", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())
    return ast

