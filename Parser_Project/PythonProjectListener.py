# Generated from .\PythonProject.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonProjectParser import PythonProjectParser
else:
    from PythonProjectParser import PythonProjectParser

# This class defines a complete listener for a parse tree produced by PythonProjectParser.
class PythonProjectListener(ParseTreeListener):

    # Enter a parse tree produced by PythonProjectParser#start.
    def enterStart(self, ctx:PythonProjectParser.StartContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#start.
    def exitStart(self, ctx:PythonProjectParser.StartContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#expr.
    def enterExpr(self, ctx:PythonProjectParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#expr.
    def exitExpr(self, ctx:PythonProjectParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#variable.
    def enterVariable(self, ctx:PythonProjectParser.VariableContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#variable.
    def exitVariable(self, ctx:PythonProjectParser.VariableContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#arithmatic.
    def enterArithmatic(self, ctx:PythonProjectParser.ArithmaticContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#arithmatic.
    def exitArithmatic(self, ctx:PythonProjectParser.ArithmaticContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#concat.
    def enterConcat(self, ctx:PythonProjectParser.ConcatContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#concat.
    def exitConcat(self, ctx:PythonProjectParser.ConcatContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#assignment.
    def enterAssignment(self, ctx:PythonProjectParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#assignment.
    def exitAssignment(self, ctx:PythonProjectParser.AssignmentContext):
        pass



del PythonProjectParser