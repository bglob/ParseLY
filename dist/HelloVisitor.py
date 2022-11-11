# Generated from Hello.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete generic visitor for a parse tree produced by HelloParser.

class HelloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloParser#NumberExpr.
    def visitNumberExpr(self, ctx:HelloParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#ByeExpr.
    def visitByeExpr(self, ctx:HelloParser.ByeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#HelloExpr.
    def visitHelloExpr(self, ctx:HelloParser.HelloExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#ParenExpr.
    def visitParenExpr(self, ctx:HelloParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#InfixExpr.
    def visitInfixExpr(self, ctx:HelloParser.InfixExprContext):
        return self.visitChildren(ctx)



del HelloParser