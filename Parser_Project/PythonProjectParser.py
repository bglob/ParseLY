# Generated from PythonProject.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,177,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        4,0,29,8,0,11,0,12,0,30,1,0,3,0,34,8,0,4,0,36,8,0,11,0,12,0,37,1,
        1,1,1,1,1,1,1,3,1,44,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,53,8,3,
        1,4,1,4,5,4,57,8,4,10,4,12,4,60,9,4,1,4,1,4,5,4,64,8,4,10,4,12,4,
        67,9,4,1,4,1,4,5,4,71,8,4,10,4,12,4,74,9,4,1,5,1,5,1,6,1,6,5,6,80,
        8,6,10,6,12,6,83,9,6,1,6,1,6,5,6,87,8,6,10,6,12,6,90,9,6,1,6,1,6,
        1,7,1,7,5,7,96,8,7,10,7,12,7,99,9,7,1,7,1,7,5,7,103,8,7,10,7,12,
        7,106,9,7,1,7,1,7,3,7,110,8,7,1,8,1,8,1,9,1,9,4,9,116,8,9,11,9,12,
        9,117,1,9,1,9,1,9,1,9,1,9,4,9,125,8,9,11,9,12,9,126,1,9,3,9,130,
        8,9,1,10,1,10,1,10,1,10,1,10,4,10,137,8,10,11,10,12,10,138,1,11,
        3,11,142,8,11,1,11,5,11,145,8,11,10,11,12,11,148,9,11,1,11,1,11,
        5,11,152,8,11,10,11,12,11,155,9,11,1,11,1,11,5,11,159,8,11,10,11,
        12,11,162,9,11,1,11,3,11,165,8,11,5,11,167,8,11,10,11,12,11,170,
        9,11,1,11,3,11,173,8,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,
        16,18,20,22,24,0,3,1,0,1,5,1,0,6,10,1,0,14,21,192,0,35,1,0,0,0,2,
        43,1,0,0,0,4,45,1,0,0,0,6,52,1,0,0,0,8,54,1,0,0,0,10,75,1,0,0,0,
        12,77,1,0,0,0,14,93,1,0,0,0,16,111,1,0,0,0,18,113,1,0,0,0,20,131,
        1,0,0,0,22,141,1,0,0,0,24,174,1,0,0,0,26,33,3,2,1,0,27,29,5,31,0,
        0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,34,
        1,0,0,0,32,34,5,0,0,1,33,28,1,0,0,0,33,32,1,0,0,0,34,36,1,0,0,0,
        35,26,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,1,1,0,
        0,0,39,44,3,8,4,0,40,44,3,12,6,0,41,44,3,14,7,0,42,44,3,18,9,0,43,
        39,1,0,0,0,43,40,1,0,0,0,43,41,1,0,0,0,43,42,1,0,0,0,44,3,1,0,0,
        0,45,46,5,29,0,0,46,5,1,0,0,0,47,53,3,4,2,0,48,53,5,22,0,0,49,53,
        5,24,0,0,50,53,5,23,0,0,51,53,5,26,0,0,52,47,1,0,0,0,52,48,1,0,0,
        0,52,49,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,7,1,0,0,0,54,72,3,
        6,3,0,55,57,5,30,0,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,
        59,1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,65,3,10,5,0,62,64,5,30,
        0,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,
        1,0,0,0,67,65,1,0,0,0,68,69,3,6,3,0,69,71,1,0,0,0,70,58,1,0,0,0,
        71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,9,1,0,0,0,74,72,1,0,
        0,0,75,76,7,0,0,0,76,11,1,0,0,0,77,81,3,4,2,0,78,80,5,30,0,0,79,
        78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,
        0,83,81,1,0,0,0,84,88,5,1,0,0,85,87,5,30,0,0,86,85,1,0,0,0,87,90,
        1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,
        91,92,3,4,2,0,92,13,1,0,0,0,93,97,3,4,2,0,94,96,5,30,0,0,95,94,1,
        0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,
        97,1,0,0,0,100,104,3,16,8,0,101,103,5,30,0,0,102,101,1,0,0,0,103,
        106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,109,1,0,0,0,106,
        104,1,0,0,0,107,110,3,2,1,0,108,110,5,31,0,0,109,107,1,0,0,0,109,
        108,1,0,0,0,110,15,1,0,0,0,111,112,7,1,0,0,112,17,1,0,0,0,113,115,
        5,11,0,0,114,116,5,30,0,0,115,114,1,0,0,0,116,117,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,120,3,22,11,0,120,124,
        5,12,0,0,121,122,5,31,0,0,122,123,5,28,0,0,123,125,3,2,1,0,124,121,
        1,0,0,0,125,126,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,129,
        1,0,0,0,128,130,3,20,10,0,129,128,1,0,0,0,129,130,1,0,0,0,130,19,
        1,0,0,0,131,132,5,13,0,0,132,136,5,12,0,0,133,134,5,31,0,0,134,135,
        5,28,0,0,135,137,3,2,1,0,136,133,1,0,0,0,137,138,1,0,0,0,138,136,
        1,0,0,0,138,139,1,0,0,0,139,21,1,0,0,0,140,142,5,27,0,0,141,140,
        1,0,0,0,141,142,1,0,0,0,142,146,1,0,0,0,143,145,5,30,0,0,144,143,
        1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,149,
        1,0,0,0,148,146,1,0,0,0,149,168,3,4,2,0,150,152,5,30,0,0,151,150,
        1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,156,
        1,0,0,0,155,153,1,0,0,0,156,160,3,24,12,0,157,159,5,30,0,0,158,157,
        1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,164,
        1,0,0,0,162,160,1,0,0,0,163,165,3,6,3,0,164,163,1,0,0,0,164,165,
        1,0,0,0,165,167,1,0,0,0,166,153,1,0,0,0,167,170,1,0,0,0,168,166,
        1,0,0,0,168,169,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,171,173,
        3,22,11,0,172,171,1,0,0,0,172,173,1,0,0,0,173,23,1,0,0,0,174,175,
        7,2,0,0,175,25,1,0,0,0,24,30,33,37,43,52,58,65,72,81,88,97,104,109,
        117,126,129,138,141,146,153,160,164,168,172
    ]

class PythonProjectParser ( Parser ):

    grammarFileName = "PythonProject.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
                     "'+='", "'-='", "'*='", "'/='", "'if'", "':'", "'else'", 
                     "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", "'and'", 
                     "'or'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "DECIMAL", "BOOL", 
                      "LETTER", "STRING", "NOT", "TAB", "VARNAME", "WS", 
                      "NEWLINE" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_variable = 2
    RULE_assignValue = 3
    RULE_arithmetic = 4
    RULE_arithmetOP = 5
    RULE_concat = 6
    RULE_assignment = 7
    RULE_assignOP = 8
    RULE_ifStatement = 9
    RULE_elseStatement = 10
    RULE_conditional = 11
    RULE_conditionOP = 12

    ruleNames =  [ "start", "expr", "variable", "assignValue", "arithmetic", 
                   "arithmetOP", "concat", "assignment", "assignOP", "ifStatement", 
                   "elseStatement", "conditional", "conditionOP" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    NUMBER=22
    DECIMAL=23
    BOOL=24
    LETTER=25
    STRING=26
    NOT=27
    TAB=28
    VARNAME=29
    WS=30
    NEWLINE=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonProjectParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonProjectParser.ExprContext,i)


        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.EOF)
            else:
                return self.getToken(PythonProjectParser.EOF, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.NEWLINE)
            else:
                return self.getToken(PythonProjectParser.NEWLINE, i)

        def getRuleIndex(self):
            return PythonProjectParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = PythonProjectParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.expr()
                self.state = 33
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [31]:
                    self.state = 28 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 27
                        self.match(PythonProjectParser.NEWLINE)
                        self.state = 30 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==31):
                            break

                    pass
                elif token in [-1]:
                    self.state = 32
                    self.match(PythonProjectParser.EOF)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 633341952) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self):
            return self.getTypedRuleContext(PythonProjectParser.ArithmeticContext,0)


        def concat(self):
            return self.getTypedRuleContext(PythonProjectParser.ConcatContext,0)


        def assignment(self):
            return self.getTypedRuleContext(PythonProjectParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(PythonProjectParser.IfStatementContext,0)


        def getRuleIndex(self):
            return PythonProjectParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = PythonProjectParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 39
                self.arithmetic()
                pass

            elif la_ == 2:
                self.state = 40
                self.concat()
                pass

            elif la_ == 3:
                self.state = 41
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 42
                self.ifStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(PythonProjectParser.VARNAME, 0)

        def getRuleIndex(self):
            return PythonProjectParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = PythonProjectParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(PythonProjectParser.VARNAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PythonProjectParser.VariableContext,0)


        def NUMBER(self):
            return self.getToken(PythonProjectParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(PythonProjectParser.BOOL, 0)

        def DECIMAL(self):
            return self.getToken(PythonProjectParser.DECIMAL, 0)

        def STRING(self):
            return self.getToken(PythonProjectParser.STRING, 0)

        def getRuleIndex(self):
            return PythonProjectParser.RULE_assignValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignValue" ):
                listener.enterAssignValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignValue" ):
                listener.exitAssignValue(self)




    def assignValue(self):

        localctx = PythonProjectParser.AssignValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.state = 47
                self.variable()
                pass
            elif token in [22]:
                self.state = 48
                self.match(PythonProjectParser.NUMBER)
                pass
            elif token in [24]:
                self.state = 49
                self.match(PythonProjectParser.BOOL)
                pass
            elif token in [23]:
                self.state = 50
                self.match(PythonProjectParser.DECIMAL)
                pass
            elif token in [26]:
                self.state = 51
                self.match(PythonProjectParser.STRING)
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


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonProjectParser.AssignValueContext)
            else:
                return self.getTypedRuleContext(PythonProjectParser.AssignValueContext,i)


        def arithmetOP(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonProjectParser.ArithmetOPContext)
            else:
                return self.getTypedRuleContext(PythonProjectParser.ArithmetOPContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.WS)
            else:
                return self.getToken(PythonProjectParser.WS, i)

        def getRuleIndex(self):
            return PythonProjectParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)




    def arithmetic(self):

        localctx = PythonProjectParser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.assignValue()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1073741886) != 0:
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 55
                    self.match(PythonProjectParser.WS)
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 61
                self.arithmetOP()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 62
                    self.match(PythonProjectParser.WS)
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 68
                self.assignValue()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmetOPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonProjectParser.RULE_arithmetOP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetOP" ):
                listener.enterArithmetOP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetOP" ):
                listener.exitArithmetOP(self)




    def arithmetOP(self):

        localctx = PythonProjectParser.ArithmetOPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arithmetOP)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonProjectParser.VariableContext)
            else:
                return self.getTypedRuleContext(PythonProjectParser.VariableContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.WS)
            else:
                return self.getToken(PythonProjectParser.WS, i)

        def getRuleIndex(self):
            return PythonProjectParser.RULE_concat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)




    def concat(self):

        localctx = PythonProjectParser.ConcatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_concat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.variable()

            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 78
                self.match(PythonProjectParser.WS)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(PythonProjectParser.T__0)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 85
                self.match(PythonProjectParser.WS)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PythonProjectParser.VariableContext,0)


        def assignOP(self):
            return self.getTypedRuleContext(PythonProjectParser.AssignOPContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonProjectParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(PythonProjectParser.NEWLINE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.WS)
            else:
                return self.getToken(PythonProjectParser.WS, i)

        def getRuleIndex(self):
            return PythonProjectParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = PythonProjectParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.variable()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 94
                self.match(PythonProjectParser.WS)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.assignOP()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 101
                self.match(PythonProjectParser.WS)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 22, 23, 24, 26, 29]:
                self.state = 107
                self.expr()
                pass
            elif token in [31]:
                self.state = 108
                self.match(PythonProjectParser.NEWLINE)
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


    class AssignOPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonProjectParser.RULE_assignOP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignOP" ):
                listener.enterAssignOP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignOP" ):
                listener.exitAssignOP(self)




    def assignOP(self):

        localctx = PythonProjectParser.AssignOPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignOP)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1984) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self):
            return self.getTypedRuleContext(PythonProjectParser.ConditionalContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.WS)
            else:
                return self.getToken(PythonProjectParser.WS, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.NEWLINE)
            else:
                return self.getToken(PythonProjectParser.NEWLINE, i)

        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.TAB)
            else:
                return self.getToken(PythonProjectParser.TAB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonProjectParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonProjectParser.ExprContext,i)


        def elseStatement(self):
            return self.getTypedRuleContext(PythonProjectParser.ElseStatementContext,0)


        def getRuleIndex(self):
            return PythonProjectParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = PythonProjectParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(PythonProjectParser.T__10)
            self.state = 115 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 114
                    self.match(PythonProjectParser.WS)

                else:
                    raise NoViableAltException(self)
                self.state = 117 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 119
            self.conditional()
            self.state = 120
            self.match(PythonProjectParser.T__11)
            self.state = 124 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 121
                    self.match(PythonProjectParser.NEWLINE)
                    self.state = 122
                    self.match(PythonProjectParser.TAB)
                    self.state = 123
                    self.expr()

                else:
                    raise NoViableAltException(self)
                self.state = 126 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 128
                self.elseStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.NEWLINE)
            else:
                return self.getToken(PythonProjectParser.NEWLINE, i)

        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.TAB)
            else:
                return self.getToken(PythonProjectParser.TAB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonProjectParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonProjectParser.ExprContext,i)


        def getRuleIndex(self):
            return PythonProjectParser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)




    def elseStatement(self):

        localctx = PythonProjectParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(PythonProjectParser.T__12)
            self.state = 132
            self.match(PythonProjectParser.T__11)
            self.state = 136 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 133
                    self.match(PythonProjectParser.NEWLINE)
                    self.state = 134
                    self.match(PythonProjectParser.TAB)
                    self.state = 135
                    self.expr()

                else:
                    raise NoViableAltException(self)
                self.state = 138 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PythonProjectParser.VariableContext,0)


        def NOT(self):
            return self.getToken(PythonProjectParser.NOT, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(PythonProjectParser.WS)
            else:
                return self.getToken(PythonProjectParser.WS, i)

        def conditionOP(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonProjectParser.ConditionOPContext)
            else:
                return self.getTypedRuleContext(PythonProjectParser.ConditionOPContext,i)


        def conditional(self):
            return self.getTypedRuleContext(PythonProjectParser.ConditionalContext,0)


        def assignValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonProjectParser.AssignValueContext)
            else:
                return self.getTypedRuleContext(PythonProjectParser.AssignValueContext,i)


        def getRuleIndex(self):
            return PythonProjectParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = PythonProjectParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 140
                self.match(PythonProjectParser.NOT)


            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 143
                self.match(PythonProjectParser.WS)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.variable()
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 153
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==30:
                        self.state = 150
                        self.match(PythonProjectParser.WS)
                        self.state = 155
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 156
                    self.conditionOP()
                    self.state = 160
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 157
                            self.match(PythonProjectParser.WS) 
                        self.state = 162
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                    self.state = 164
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        self.state = 163
                        self.assignValue()

             
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 1744830464) != 0:
                self.state = 171
                self.conditional()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionOPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonProjectParser.RULE_conditionOP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionOP" ):
                listener.enterConditionOP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionOP" ):
                listener.exitConditionOP(self)




    def conditionOP(self):

        localctx = PythonProjectParser.ConditionOPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_conditionOP)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 4177920) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





