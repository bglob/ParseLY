# Generated from Hello.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#NumberExpr.
    def enterNumberExpr(self, ctx:HelloParser.NumberExprContext):
        pass

    # Exit a parse tree produced by HelloParser#NumberExpr.
    def exitNumberExpr(self, ctx:HelloParser.NumberExprContext):
        pass


    # Enter a parse tree produced by HelloParser#ByeExpr.
    def enterByeExpr(self, ctx:HelloParser.ByeExprContext):
        pass

    # Exit a parse tree produced by HelloParser#ByeExpr.
    def exitByeExpr(self, ctx:HelloParser.ByeExprContext):
        pass


    # Enter a parse tree produced by HelloParser#HelloExpr.
    def enterHelloExpr(self, ctx:HelloParser.HelloExprContext):
        pass

    # Exit a parse tree produced by HelloParser#HelloExpr.
    def exitHelloExpr(self, ctx:HelloParser.HelloExprContext):
        pass


    # Enter a parse tree produced by HelloParser#ParenExpr.
    def enterParenExpr(self, ctx:HelloParser.ParenExprContext):
        pass

    # Exit a parse tree produced by HelloParser#ParenExpr.
    def exitParenExpr(self, ctx:HelloParser.ParenExprContext):
        pass


    # Enter a parse tree produced by HelloParser#InfixExpr.
    def enterInfixExpr(self, ctx:HelloParser.InfixExprContext):
        pass

    # Exit a parse tree produced by HelloParser#InfixExpr.
    def exitInfixExpr(self, ctx:HelloParser.InfixExprContext):
        pass



del HelloParser