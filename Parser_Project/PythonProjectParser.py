# Generated from .\PythonProject.g4 by ANTLR 4.11.1
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
        4,1,12,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,4,0,15,8,0,11,0,12,0,16,4,0,19,8,0,11,0,12,0,20,1,1,1,1,3,1,25,
        8,1,1,2,1,2,1,3,1,3,1,4,1,4,5,4,33,8,4,10,4,12,4,36,9,4,1,4,1,4,
        5,4,40,8,4,10,4,12,4,43,9,4,1,4,1,4,1,5,1,5,5,5,49,8,5,10,5,12,5,
        52,9,5,1,5,1,5,5,5,56,8,5,10,5,12,5,59,9,5,1,5,1,5,1,5,0,0,6,0,2,
        4,6,8,10,0,1,1,0,1,5,63,0,18,1,0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,
        28,1,0,0,0,8,30,1,0,0,0,10,46,1,0,0,0,12,14,3,2,1,0,13,15,5,12,0,
        0,14,13,1,0,0,0,15,16,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,19,
        1,0,0,0,18,12,1,0,0,0,19,20,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,
        21,1,1,0,0,0,22,25,3,6,3,0,23,25,3,8,4,0,24,22,1,0,0,0,24,23,1,0,
        0,0,25,3,1,0,0,0,26,27,5,10,0,0,27,5,1,0,0,0,28,29,7,0,0,0,29,7,
        1,0,0,0,30,34,3,4,2,0,31,33,5,11,0,0,32,31,1,0,0,0,33,36,1,0,0,0,
        34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,41,5,
        1,0,0,38,40,5,11,0,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,
        42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,3,4,2,0,45,9,1,0,0,
        0,46,50,3,4,2,0,47,49,5,11,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,
        1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,57,3,6,3,0,
        54,56,5,11,0,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,
        0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,3,2,1,0,61,11,1,0,0,0,7,
        16,20,24,34,41,50,57
    ]

class PythonProjectParser ( Parser ):

    grammarFileName = "PythonProject.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "DECIMAL", "BOOL", 
                      "LETTER", "VARNAME", "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_variable = 2
    RULE_arithmatic = 3
    RULE_concat = 4
    RULE_assignment = 5

    ruleNames =  [ "start", "expr", "variable", "arithmatic", "concat", 
                   "assignment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    DECIMAL=7
    BOOL=8
    LETTER=9
    VARNAME=10
    WS=11
    NEWLINE=12

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
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.expr()

                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 13
                    self.match(PythonProjectParser.NEWLINE)
                    self.state = 16 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==12):
                        break

                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 1086) != 0):
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

        def arithmatic(self):
            return self.getTypedRuleContext(PythonProjectParser.ArithmaticContext,0)


        def concat(self):
            return self.getTypedRuleContext(PythonProjectParser.ConcatContext,0)


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
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5]:
                self.state = 22
                self.arithmatic()
                pass
            elif token in [10]:
                self.state = 23
                self.concat()
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
            self.state = 26
            self.match(PythonProjectParser.VARNAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmaticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonProjectParser.RULE_arithmatic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmatic" ):
                listener.enterArithmatic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmatic" ):
                listener.exitArithmatic(self)




    def arithmatic(self):

        localctx = PythonProjectParser.ArithmaticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arithmatic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
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
        self.enterRule(localctx, 8, self.RULE_concat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.variable()

            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 31
                self.match(PythonProjectParser.WS)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(PythonProjectParser.T__0)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 38
                self.match(PythonProjectParser.WS)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
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


        def arithmatic(self):
            return self.getTypedRuleContext(PythonProjectParser.ArithmaticContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonProjectParser.ExprContext,0)


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
        self.enterRule(localctx, 10, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.variable()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 47
                self.match(PythonProjectParser.WS)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.arithmatic()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 54
                self.match(PythonProjectParser.WS)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            self.state = 60
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





