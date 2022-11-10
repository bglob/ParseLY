# Generated from .\Python.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2\16\2")
        buf.write("\33\13\2\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\5\4*\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5")
        buf.write("\63\n\5\f\5\16\5\66\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\bH\n\b\3\t\3\t\5")
        buf.write("\tL\n\t\3\n\3\n\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20")
        buf.write("\22\24\2\2\2N\2\31\3\2\2\2\4\"\3\2\2\2\6)\3\2\2\2\b+\3")
        buf.write("\2\2\2\n9\3\2\2\2\f=\3\2\2\2\16G\3\2\2\2\20K\3\2\2\2\22")
        buf.write("M\3\2\2\2\24O\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\33")
        buf.write("\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\37\3\2\2\2\33")
        buf.write("\31\3\2\2\2\34\36\5\6\4\2\35\34\3\2\2\2\36!\3\2\2\2\37")
        buf.write("\35\3\2\2\2\37 \3\2\2\2 \3\3\2\2\2!\37\3\2\2\2\"#\7\6")
        buf.write("\2\2#$\7\17\2\2$%\7\13\2\2%\5\3\2\2\2&*\5\b\5\2\'*\5\n")
        buf.write("\6\2(*\5\f\7\2)&\3\2\2\2)\'\3\2\2\2)(\3\2\2\2*\7\3\2\2")
        buf.write("\2+,\7\3\2\2,-\7\f\2\2-.\5\22\n\2./\7\b\2\2/\60\5\24\13")
        buf.write("\2\60\64\7\r\2\2\61\63\5\6\4\2\62\61\3\2\2\2\63\66\3\2")
        buf.write("\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\67\3\2\2\2\66\64\3")
        buf.write("\2\2\2\678\7\4\2\28\t\3\2\2\29:\7\5\2\2:;\5\20\t\2;<\7")
        buf.write("\13\2\2<\13\3\2\2\2=>\7\17\2\2>?\7\t\2\2?@\5\16\b\2@A")
        buf.write("\7\13\2\2A\r\3\2\2\2BH\5\20\t\2CD\5\20\t\2DE\7\7\2\2E")
        buf.write("F\5\20\t\2FH\3\2\2\2GB\3\2\2\2GC\3\2\2\2H\17\3\2\2\2I")
        buf.write("L\5\22\n\2JL\5\24\13\2KI\3\2\2\2KJ\3\2\2\2L\21\3\2\2\2")
        buf.write("MN\7\17\2\2N\23\3\2\2\2OP\7\16\2\2P\25\3\2\2\2\b\31\37")
        buf.write(")\64GK")
        return buf.getvalue()


class PythonParser ( Parser ):

    grammarFileName = "Python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'endif'", "'print'", "'int'", 
                     "'+'", "'=='", "'='", "'!='", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "IF", "ENDIF", "PRINT", "INT", "PLUS", 
                      "EQUAL", "ASSIGN", "NOTEQUAL", "SEMICOLON", "LPAREN", 
                      "RPAREN", "INTEGER", "NAME", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_statement = 2
    RULE_ifstmt = 3
    RULE_printstmt = 4
    RULE_assignstmt = 5
    RULE_expression = 6
    RULE_term = 7
    RULE_identifier = 8
    RULE_integer = 9

    ruleNames =  [ "program", "declaration", "statement", "ifstmt", "printstmt", 
                   "assignstmt", "expression", "term", "identifier", "integer" ]

    EOF = Token.EOF
    IF=1
    ENDIF=2
    PRINT=3
    INT=4
    PLUS=5
    EQUAL=6
    ASSIGN=7
    NOTEQUAL=8
    SEMICOLON=9
    LPAREN=10
    RPAREN=11
    INTEGER=12
    NAME=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(PythonParser.DeclarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParser.StatementContext,i)


        def getRuleIndex(self):
            return PythonParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PythonParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PythonParser.INT:
                self.state = 20
                self.declaration()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonParser.IF) | (1 << PythonParser.PRINT) | (1 << PythonParser.NAME))) != 0):
                self.state = 26
                self.statement()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PythonParser.INT, 0)

        def NAME(self):
            return self.getToken(PythonParser.NAME, 0)

        def SEMICOLON(self):
            return self.getToken(PythonParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = PythonParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(PythonParser.INT)
            self.state = 33
            self.match(PythonParser.NAME)
            self.state = 34
            self.match(PythonParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstmt(self):
            return self.getTypedRuleContext(PythonParser.IfstmtContext,0)


        def printstmt(self):
            return self.getTypedRuleContext(PythonParser.PrintstmtContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(PythonParser.AssignstmtContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PythonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PythonParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.ifstmt()
                pass
            elif token in [PythonParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.printstmt()
                pass
            elif token in [PythonParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.assignstmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PythonParser.IF, 0)

        def LPAREN(self):
            return self.getToken(PythonParser.LPAREN, 0)

        def identifier(self):
            return self.getTypedRuleContext(PythonParser.IdentifierContext,0)


        def EQUAL(self):
            return self.getToken(PythonParser.EQUAL, 0)

        def integer(self):
            return self.getTypedRuleContext(PythonParser.IntegerContext,0)


        def RPAREN(self):
            return self.getToken(PythonParser.RPAREN, 0)

        def ENDIF(self):
            return self.getToken(PythonParser.ENDIF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParser.StatementContext,i)


        def getRuleIndex(self):
            return PythonParser.RULE_ifstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstmt" ):
                listener.enterIfstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstmt" ):
                listener.exitIfstmt(self)




    def ifstmt(self):

        localctx = PythonParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(PythonParser.IF)
            self.state = 42
            self.match(PythonParser.LPAREN)
            self.state = 43
            self.identifier()
            self.state = 44
            self.match(PythonParser.EQUAL)
            self.state = 45
            self.integer()
            self.state = 46
            self.match(PythonParser.RPAREN)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonParser.IF) | (1 << PythonParser.PRINT) | (1 << PythonParser.NAME))) != 0):
                self.state = 47
                self.statement()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(PythonParser.ENDIF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(PythonParser.PRINT, 0)

        def term(self):
            return self.getTypedRuleContext(PythonParser.TermContext,0)


        def SEMICOLON(self):
            return self.getToken(PythonParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_printstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintstmt" ):
                listener.enterPrintstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintstmt" ):
                listener.exitPrintstmt(self)




    def printstmt(self):

        localctx = PythonParser.PrintstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(PythonParser.PRINT)
            self.state = 56
            self.term()
            self.state = 57
            self.match(PythonParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PythonParser.NAME, 0)

        def ASSIGN(self):
            return self.getToken(PythonParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(PythonParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(PythonParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_assignstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignstmt" ):
                listener.enterAssignstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignstmt" ):
                listener.exitAssignstmt(self)




    def assignstmt(self):

        localctx = PythonParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(PythonParser.NAME)
            self.state = 60
            self.match(PythonParser.ASSIGN)
            self.state = 61
            self.expression()
            self.state = 62
            self.match(PythonParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.TermContext)
            else:
                return self.getTypedRuleContext(PythonParser.TermContext,i)


        def PLUS(self):
            return self.getToken(PythonParser.PLUS, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PythonParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.term()
                self.state = 66
                self.match(PythonParser.PLUS)
                self.state = 67
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(PythonParser.IdentifierContext,0)


        def integer(self):
            return self.getTypedRuleContext(PythonParser.IntegerContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = PythonParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_term)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PythonParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.identifier()
                pass
            elif token in [PythonParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.integer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PythonParser.NAME, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = PythonParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(PythonParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(PythonParser.INTEGER, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = PythonParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(PythonParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





