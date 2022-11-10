# Generated from .\Python.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#program.
    def enterProgram(self, ctx:PythonParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonParser#program.
    def exitProgram(self, ctx:PythonParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonParser#declaration.
    def enterDeclaration(self, ctx:PythonParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PythonParser#declaration.
    def exitDeclaration(self, ctx:PythonParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PythonParser#statement.
    def enterStatement(self, ctx:PythonParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonParser#statement.
    def exitStatement(self, ctx:PythonParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonParser#ifstmt.
    def enterIfstmt(self, ctx:PythonParser.IfstmtContext):
        pass

    # Exit a parse tree produced by PythonParser#ifstmt.
    def exitIfstmt(self, ctx:PythonParser.IfstmtContext):
        pass


    # Enter a parse tree produced by PythonParser#printstmt.
    def enterPrintstmt(self, ctx:PythonParser.PrintstmtContext):
        pass

    # Exit a parse tree produced by PythonParser#printstmt.
    def exitPrintstmt(self, ctx:PythonParser.PrintstmtContext):
        pass


    # Enter a parse tree produced by PythonParser#assignstmt.
    def enterAssignstmt(self, ctx:PythonParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by PythonParser#assignstmt.
    def exitAssignstmt(self, ctx:PythonParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by PythonParser#expression.
    def enterExpression(self, ctx:PythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonParser#expression.
    def exitExpression(self, ctx:PythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonParser#term.
    def enterTerm(self, ctx:PythonParser.TermContext):
        pass

    # Exit a parse tree produced by PythonParser#term.
    def exitTerm(self, ctx:PythonParser.TermContext):
        pass


    # Enter a parse tree produced by PythonParser#identifier.
    def enterIdentifier(self, ctx:PythonParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PythonParser#identifier.
    def exitIdentifier(self, ctx:PythonParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PythonParser#integer.
    def enterInteger(self, ctx:PythonParser.IntegerContext):
        pass

    # Exit a parse tree produced by PythonParser#integer.
    def exitInteger(self, ctx:PythonParser.IntegerContext):
        pass



del PythonParser