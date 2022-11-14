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
        4,1,17,104,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,4,0,21,8,0,11,0,12,0,22,1,0,3,0,26,8,0,
        4,0,28,8,0,11,0,12,0,29,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,3,1,3,1,
        3,1,3,3,3,43,8,3,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,1,4,1,4,5,4,
        54,8,4,10,4,12,4,57,9,4,1,4,1,4,5,4,61,8,4,10,4,12,4,64,9,4,1,5,
        1,5,1,6,1,6,5,6,70,8,6,10,6,12,6,73,9,6,1,6,1,6,5,6,77,8,6,10,6,
        12,6,80,9,6,1,6,1,6,1,7,1,7,5,7,86,8,7,10,7,12,7,89,9,7,1,7,1,7,
        5,7,93,8,7,10,7,12,7,96,9,7,1,7,1,7,3,7,100,8,7,1,8,1,8,1,8,0,0,
        9,0,2,4,6,8,10,12,14,16,0,2,1,0,1,5,1,0,6,10,110,0,27,1,0,0,0,2,
        34,1,0,0,0,4,36,1,0,0,0,6,42,1,0,0,0,8,44,1,0,0,0,10,65,1,0,0,0,
        12,67,1,0,0,0,14,83,1,0,0,0,16,101,1,0,0,0,18,25,3,2,1,0,19,21,5,
        17,0,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,
        26,1,0,0,0,24,26,5,0,0,1,25,20,1,0,0,0,25,24,1,0,0,0,26,28,1,0,0,
        0,27,18,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,1,1,
        0,0,0,31,35,3,8,4,0,32,35,3,12,6,0,33,35,3,14,7,0,34,31,1,0,0,0,
        34,32,1,0,0,0,34,33,1,0,0,0,35,3,1,0,0,0,36,37,5,15,0,0,37,5,1,0,
        0,0,38,43,3,4,2,0,39,43,5,11,0,0,40,43,5,13,0,0,41,43,5,12,0,0,42,
        38,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,7,1,0,0,
        0,44,62,3,6,3,0,45,47,5,16,0,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,
        1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,55,3,10,5,0,
        52,54,5,16,0,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,
        0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,3,6,3,0,59,61,1,0,0,0,60,
        48,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,9,1,0,0,
        0,64,62,1,0,0,0,65,66,7,0,0,0,66,11,1,0,0,0,67,71,3,4,2,0,68,70,
        5,16,0,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,
        72,74,1,0,0,0,73,71,1,0,0,0,74,78,5,1,0,0,75,77,5,16,0,0,76,75,1,
        0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,
        78,1,0,0,0,81,82,3,4,2,0,82,13,1,0,0,0,83,87,3,4,2,0,84,86,5,16,
        0,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,
        1,0,0,0,89,87,1,0,0,0,90,94,3,16,8,0,91,93,5,16,0,0,92,91,1,0,0,
        0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,99,1,0,0,0,96,94,
        1,0,0,0,97,100,3,2,1,0,98,100,5,17,0,0,99,97,1,0,0,0,99,98,1,0,0,
        0,100,15,1,0,0,0,101,102,7,1,0,0,102,17,1,0,0,0,13,22,25,29,34,42,
        48,55,62,71,78,87,94,99
    ]

class PythonProjectParser ( Parser ):

    grammarFileName = "PythonProject.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
                     "'+='", "'-='", "'*='", "'/='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "DECIMAL", 
                      "BOOL", "LETTER", "VARNAME", "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_variable = 2
    RULE_assignValue = 3
    RULE_arithmetic = 4
    RULE_arithmetOP = 5
    RULE_concat = 6
    RULE_assignment = 7
    RULE_assignOP = 8

    ruleNames =  [ "start", "expr", "variable", "assignValue", "arithmetic", 
                   "arithmetOP", "concat", "assignment", "assignOP" ]

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
    NUMBER=11
    DECIMAL=12
    BOOL=13
    LETTER=14
    VARNAME=15
    WS=16
    NEWLINE=17

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
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.expr()
                self.state = 25
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17]:
                    self.state = 20 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 19
                        self.match(PythonProjectParser.NEWLINE)
                        self.state = 22 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==17):
                            break

                    pass
                elif token in [-1]:
                    self.state = 24
                    self.match(PythonProjectParser.EOF)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 47104) != 0):
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
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 31
                self.arithmetic()
                pass

            elif la_ == 2:
                self.state = 32
                self.concat()
                pass

            elif la_ == 3:
                self.state = 33
                self.assignment()
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
            self.state = 36
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
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 38
                self.variable()
                pass
            elif token in [11]:
                self.state = 39
                self.match(PythonProjectParser.NUMBER)
                pass
            elif token in [13]:
                self.state = 40
                self.match(PythonProjectParser.BOOL)
                pass
            elif token in [12]:
                self.state = 41
                self.match(PythonProjectParser.DECIMAL)
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
            self.state = 44
            self.assignValue()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 65598) != 0:
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 45
                    self.match(PythonProjectParser.WS)
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 51
                self.arithmetOP()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 52
                    self.match(PythonProjectParser.WS)
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 58
                self.assignValue()
                self.state = 64
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
            self.state = 65
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
            self.state = 67
            self.variable()

            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 68
                self.match(PythonProjectParser.WS)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(PythonProjectParser.T__0)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 75
                self.match(PythonProjectParser.WS)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
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
            self.state = 83
            self.variable()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 84
                self.match(PythonProjectParser.WS)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.assignOP()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 91
                self.match(PythonProjectParser.WS)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 15]:
                self.state = 97
                self.expr()
                pass
            elif token in [17]:
                self.state = 98
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
            self.state = 101
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





