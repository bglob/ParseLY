# Generated from PythonProject.g4 by ANTLR 4.11.1
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


    # Enter a parse tree produced by PythonProjectParser#assignValue.
    def enterAssignValue(self, ctx:PythonProjectParser.AssignValueContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#assignValue.
    def exitAssignValue(self, ctx:PythonProjectParser.AssignValueContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#arithmetic.
    def enterArithmetic(self, ctx:PythonProjectParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#arithmetic.
    def exitArithmetic(self, ctx:PythonProjectParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#arithmetOP.
    def enterArithmetOP(self, ctx:PythonProjectParser.ArithmetOPContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#arithmetOP.
    def exitArithmetOP(self, ctx:PythonProjectParser.ArithmetOPContext):
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


    # Enter a parse tree produced by PythonProjectParser#assignOP.
    def enterAssignOP(self, ctx:PythonProjectParser.AssignOPContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#assignOP.
    def exitAssignOP(self, ctx:PythonProjectParser.AssignOPContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#ifStatement.
    def enterIfStatement(self, ctx:PythonProjectParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#ifStatement.
    def exitIfStatement(self, ctx:PythonProjectParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#elseStatement.
    def enterElseStatement(self, ctx:PythonProjectParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#elseStatement.
    def exitElseStatement(self, ctx:PythonProjectParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#conditional.
    def enterConditional(self, ctx:PythonProjectParser.ConditionalContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#conditional.
    def exitConditional(self, ctx:PythonProjectParser.ConditionalContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#conditionOP.
    def enterConditionOP(self, ctx:PythonProjectParser.ConditionOPContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#conditionOP.
    def exitConditionOP(self, ctx:PythonProjectParser.ConditionOPContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#andor.
    def enterAndor(self, ctx:PythonProjectParser.AndorContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#andor.
    def exitAndor(self, ctx:PythonProjectParser.AndorContext):
        pass



del PythonProjectParser