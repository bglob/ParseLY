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


    # Enter a parse tree produced by PythonProjectParser#whileStatement.
    def enterWhileStatement(self, ctx:PythonProjectParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#whileStatement.
    def exitWhileStatement(self, ctx:PythonProjectParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#forStatement.
    def enterForStatement(self, ctx:PythonProjectParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#forStatement.
    def exitForStatement(self, ctx:PythonProjectParser.ForStatementContext):
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


    # Enter a parse tree produced by PythonProjectParser#block.
    def enterBlock(self, ctx:PythonProjectParser.BlockContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#block.
    def exitBlock(self, ctx:PythonProjectParser.BlockContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#function.
    def enterFunction(self, ctx:PythonProjectParser.FunctionContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#function.
    def exitFunction(self, ctx:PythonProjectParser.FunctionContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#parameters.
    def enterParameters(self, ctx:PythonProjectParser.ParametersContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#parameters.
    def exitParameters(self, ctx:PythonProjectParser.ParametersContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#functionCall.
    def enterFunctionCall(self, ctx:PythonProjectParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#functionCall.
    def exitFunctionCall(self, ctx:PythonProjectParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#passing.
    def enterPassing(self, ctx:PythonProjectParser.PassingContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#passing.
    def exitPassing(self, ctx:PythonProjectParser.PassingContext):
        pass


    # Enter a parse tree produced by PythonProjectParser#comment.
    def enterComment(self, ctx:PythonProjectParser.CommentContext):
        pass

    # Exit a parse tree produced by PythonProjectParser#comment.
    def exitComment(self, ctx:PythonProjectParser.CommentContext):
        pass



del PythonProjectParser