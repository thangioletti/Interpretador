import lex as lex

class Compiler:
    def __init__(self, sData=None):
        import lex as lex

        # List of token names.   This is always required
        reserved = {
           'VAR' : 'VAR',
           'PRINT': 'PRINT',
           'IF' : 'IF',
           'FOR' : 'FOR',      
           'WHILE' : 'WHILE',
           'FUNCTION' : 'FUNCTION',
           'ELSE' : 'ELSE',   
           'PROGRAM': 'PROGRAM',
           'TRUE' : 'TRUE',
           'FALSE' : 'FALSE',
           'END' : 'END',
           'AND' : 'AND',
           'OR' : 'OR'    
        }

        tokens = [
            #'COMANDO',
            'STRING',
            'ID',    
            'NUM',
            'DECIMAL',
            'SOMA',
            'SUBTRACAO',
            'MULTIPLICACAO',
            'DIVISAO',
            'LPAREN',
            'RPAREN',        
            'PONTOEVIRGULA',
            'POTENCIA',
            'MAIOR',
            'MENOR',
            'IGUAL',
            'DIFERENTE',
            'ATRIBUICAO',
            'VIRGULA'
        ] + list(reserved.values())

        # Regular expression rules for simple tokens
        t_SOMA        = r'\+'
        t_SUBTRACAO   = r'-'
        t_MULTIPLICACAO = r'\*'
        t_DIVISAO     = r'/'
        t_LPAREN      = r'\('
        t_RPAREN      = r'\)'
        t_PONTOEVIRGULA = r'\;'
        t_POTENCIA    = r'\^'
        t_MAIOR       = r'\>'
        t_MENOR       = r'\<'
        t_IGUAL       = r'\=='
        t_DIFERENTE   = r'\!='
        t_ATRIBUICAO  = r'\:='
        t_VIRGULA     = r'\,'

        def t_COMANDO(t):
            r'[A-Z_]+'
            t.type = reserved.get(t.value,'COMANDO')    # Check for reserved words
            return t

        def t_STRING(t):
            r'"[a-zA-Z_0-9]*"'        
            return t

        def t_ID(t):
            r'[i|s|b|f|d|c|o|p][a-zA-Z_][a-zA-Z_0-9]*'                    
            return t

        # A regular expression rule with some action code
        def t_NUM(t):
            r'\d+'
            t.value = int(t.value)    
            return t

        # Define a rule so we can track line numbers
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)

        # A string containing ignored characters (spaces and tabs)
        t_ignore  = ' \t'

        # Error handling rule
        def t_error(t):
            print("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)

        # Build the lexer
        lexer = lex.lex()

        # Test it out
        sCaminhoImg = 'runTesteLeandro.top'
        oArquivo = open(sCaminhoImg)

        # Give the lexer some input
        lexer.input(sData)

        oArquivo = open('tokens.ttop', 'w')

        # Tokenize
        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input

            oArquivo.write(str(tok)+'\n')

        oArquivo.close()

        import yacc as yacc
        import classes as classes
        import classes.pilha as Pilha
        import classes.id as Id
        import classes.factor as Factor
        import classes.term as Term
        import classes.expreg as Expreg
        import classes.explog as Explog
        import classes.atribuicao as Atribuicao
        import classes.declaracao as Declaracao
        import classes.condicao as Condicao
        import classes.escrever as Escrever
        import classes.comando as Comando
        import classes.bloco as Bloco
        import classes.function as Function
        import classes.parametro as Parametro
        import classes.parametros as Parametros
        import classes.repeticao as Repeticao
        import classes.program as Program

        pilha = Pilha.Pilha()

        def p_program(p):
            'program : PROGRAM ID function END'
            objetoFunction = pilha.desempilha()
            pilha.empilha(Program.Program(objetoFunction))

        def p_function_function(p):
            'function : function function'
            objetoFunction1 = pilha.desempilha()
            objetoFunction2 = pilha.desempilha()
            pilha.empilha(Function.Function(objetoFunction2, objetoFunction1))

        def p_function(p):
            'function : FUNCTION ID LPAREN parametros RPAREN bloco END'
            objetoBloco = pilha.desempilha()
            objetoParametros = pilha.desempilha()
            pilha.empilha(Function.Function(objetoParametros, objetoBloco))

        def p_bloco(p):
            'bloco : comando'
            objetoComando = pilha.desempilha()
            pilha.empilha(Bloco.Bloco(objetoComando))

        def p_comando_comando(p):
            'comando : comando comando'
            objetoComando1 = pilha.desempilha()
            objetoComando2 = pilha.desempilha()
            pilha.empilha(Comando.Comando(objetoComando2, objetoComando1))

        def p_comando_declaracao(p):
            'comando : declaracao'
            objetoDeclaracao = pilha.desempilha()
            pilha.empilha(Comando.Comando(objetoDeclaracao))

        def p_comando_explog(p):
            'comando : explog'
            objetoExplog = pilha.desempilha()
            pilha.empilha(Comando.Comando(objetoExplog))

        def p_comando_atribuicao(p):
            'comando : atribuicao'
            objetoAtribuicao = pilha.desempilha()
            pilha.empilha(Comando.Comando(objetoAtribuicao))

        def p_comando_condicao(p):
            'comando : condicao'
            objetoCondicao = pilha.desempilha()
            pilha.empilha(Comando.Comando(objetoCondicao))

        def p_comando_escrever(p):
            'comando : escrever'
            objetoEscrever = pilha.desempilha()
            pilha.empilha(Comando.Comando(objetoEscrever))

        def p_comando_repeticao(p):
            'comando : repeticao'
            objetoRepeticao = pilha.desempilha()
            pilha.empilha(Comando.Comando(objetoRepeticao))

        def p_repeticao_for(p):
            'repeticao : FOR LPAREN VAR ID ATRIBUICAO expreg PONTOEVIRGULA explog PONTOEVIRGULA ID ATRIBUICAO expreg RPAREN bloco END'
            objetoBloco = pilha.desempilha()
            objetoExpreg2 = pilha.desempilha()
            objetoExplog = pilha.desempilha()
            objetoExpreg1 = pilha.desempilha()
            pilha.empilha(Repeticao.Repeticao(objetoBloco, objetoExplog, Id.Id(p[4]), objetoExpreg1, Id.Id(p[10]), objetoExpreg2))

        def p_repeticao_while(p):
            'repeticao : WHILE LPAREN explog RPAREN bloco END'
            objetoBloco = pilha.desempilha()
            objetoExplog = pilha.desempilha()
            pilha.empilha(Repeticao.Repeticao(objetoBloco, objetoExplog))

        def p_condicao_else(p):
            'condicao : IF LPAREN explog RPAREN bloco ELSE bloco END'
            objetoElse = pilha.desempilha()
            objetoBloco = pilha.desempilha()
            objetoExplog = pilha.desempilha()
            pilha.empilha(Condicao.Condicao(objetoExplog, objetoBloco, objetoElse))

        def p_condicao(p):
            'condicao : IF LPAREN explog RPAREN bloco END'
            objetoBloco = pilha.desempilha()
            objetoExplog = pilha.desempilha()
            pilha.empilha(Condicao.Condicao(objetoExplog, objetoBloco))

        def p_atribuicao_explog(p):
            'atribuicao : ID ATRIBUICAO explog PONTOEVIRGULA'
            objetoExplog = pilha.desempilha()
            pilha.empilha(Atribuicao.Atribuicao(Id.Id(p[1]),objetoExplog, None))

        def p_atribuicao_expreg(p):
            'atribuicao : ID ATRIBUICAO expreg PONTOEVIRGULA'
            objetoExpreg = pilha.desempilha()
            pilha.empilha(Atribuicao.Atribuicao(Id.Id(p[1]),objetoExpreg, None))

        def p_atribuicao_string(p):
            'atribuicao : ID ATRIBUICAO STRING PONTOEVIRGULA'
            pilha.empilha(Atribuicao.Atribuicao(Id.Id(p[1]),None, p[3]))

        def p_explog_or(p):
            'explog : explog OR explog'
            objetoExplog1 = pilha.desempilha()
            objetoExplog2 = pilha.desempilha()
            pilha.empilha(Explog.Explog(objetoExplog2, "OR", objetoExplog1))

        def p_explog_and(p):
            'explog : explog AND explog'
            objetoExplog1 = pilha.desempilha()
            objetoExplog2 = pilha.desempilha()
            pilha.empilha(Explog.Explog(objetoExplog2, "AND", objetoExplog1))

        def p_explog_diferente_expreg(p):
            'explog : expreg DIFERENTE expreg'
            objetoExpreg1 = pilha.desempilha()
            objetoExpreg2 = pilha.desempilha()
            pilha.empilha(Explog.Explog(objetoExpreg2, "!=", objetoExpreg1))

        def p_explog_igual_expreg(p):
            'explog : expreg IGUAL expreg'
            objetoExpreg1 = pilha.desempilha()
            objetoExpreg2 = pilha.desempilha()
            pilha.empilha(Explog.Explog(objetoExpreg2, "==", objetoExpreg1))

        def p_explog_menor_expreg(p):
            'explog : expreg MENOR expreg'
            objetoExpreg1 = pilha.desempilha()
            objetoExpreg2 = pilha.desempilha()
            pilha.empilha(Explog.Explog(objetoExpreg2, "<", objetoExpreg1))

        def p_explog_maior_expreg(p):
            'explog : expreg MAIOR expreg'
            objetoExpreg1 = pilha.desempilha()
            objetoExpreg2 = pilha.desempilha()
            pilha.empilha(Explog.Explog(objetoExpreg2, ">", objetoExpreg1))

        def p_explog_true(p):
            'explog : TRUE'
            pilha.empilha(Explog.Explog(None,None,None,p[1]))

        def p_explog_false(p):
            'explog : FALSE'
            pilha.empilha(Explog.Explog(None,None,None,p[1]))

        def p_expreg_soma(p):
            'expreg : expreg SOMA term'
            objetoTerm = pilha.desempilha()
            objetoExpreg = pilha.desempilha()
            pilha.empilha(Expreg.Expreg(objetoExpreg, "+", objetoTerm))
           #p[0] = Expression(p[1], "+", p[3])

        def p_expreg_subtracao(p):
            'expreg : expreg SUBTRACAO term'
            objetoTerm = pilha.desempilha()
            objetoExpreg = pilha.desempilha()
            pilha.empilha(Expreg.Expreg(objetoExpreg, "-", objetoTerm))
            #p[0] = p[1] - p[3]

        def p_expreg_term(p):
            'expreg : term'
            objeto = pilha.desempilha()
            pilha.empilha(Expreg.Expreg(None,None,objeto))
            #p[0] = Expression(None, None, p[1]) 

        def p_term_multiplicacao(p):
            'term : term MULTIPLICACAO factor'
            objetoFactor = pilha.desempilha()
            objetoTerm = pilha.desempilha()
            pilha.empilha(Term.Term(objetoTerm, "*", objetoFactor))

        def p_term_divisao(p):
            'term : term DIVISAO factor'
            objetoFactor = pilha.desempilha()
            objetoTerm = pilha.desempilha()
            pilha.empilha(Term.Term(objetoTerm, "/", objetoFactor))

        def p_term_factor(p):
            'term : factor'
            objeto = pilha.desempilha()
            pilha.empilha(Term.Term(None, None, objeto))

        def p_factor_expreg(p):
            'factor : LPAREN expreg RPAREN'
            objetoExpreg = pilha.desempilha()
            pilha.empilha(Factor.Factor(None, None, objetoExpreg))

        def p_factor_id(p):
            'factor : ID'
            pilha.empilha(Factor.Factor(Id.Id(p[1]), None, None))

        def p_factor_num(p):
            'factor : NUM'
            pilha.empilha(Factor.Factor(None, p[1], None))
            #p[0] = Term(None, None, Factor(None, p[1], None))

        def p_parametros(p):
            'parametros : parametros VIRGULA parametro'
            objetoParametro = pilha.desempilha()
            objetoParametros = pilha.desempilha()
            pilha.empilha(Parametros.Parametros(objetoParametro, objetoParametros))

        def p_parametros_parametro(p):
            'parametros : parametro'
            objetoParametro = pilha.desempilha()
            pilha.empilha(Parametros.Parametros(objetoParametro))

        def p_parametro(p):
            'parametro : VAR ID'
            pilha.empilha(Parametro.Parametro(Id.Id(p[2])))

        def p_declaracao(p):
            'declaracao : VAR ID PONTOEVIRGULA'
            pilha.empilha(Declaracao.Declaracao(Id.Id(p[2])))

        def p_escrever(p):
            'escrever : PRINT LPAREN STRING RPAREN PONTOEVIRGULA'
            pilha.empilha(Escrever.Escrever(p[3]))

        def p_escrever_id(p):
            'escrever : PRINT LPAREN ID RPAREN PONTOEVIRGULA'
            pilha.empilha(Escrever.Escrever(None, p[3]))

        def p_error(p):
            print("Syntax error in input!")

        parser = yacc.yacc()

        # Test it out
        oArquivo = open('sintatico.stop', 'w')         
        
        parser.parse(sData)

        while not pilha.vazia():
            oArquivo.write(str(pilha.desempilha()))
        
        oArquivo.close()     

        #while not pilha.vazia():            
            #oObjetoAnalise = pilha.desempilha()        
            #oObjetoAnalise.semantico()
