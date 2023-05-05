# Generated from /home/Projects/antlr/Simple.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleParser import SimpleParser
else:
    from SimpleParser import SimpleParser

# This class defines a complete listener for a parse tree produced by SimpleParser.
class SimpleListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleParser#start.
    def enterStart(self, ctx:SimpleParser.StartContext):
        pass

    # Exit a parse tree produced by SimpleParser#start.
    def exitStart(self, ctx:SimpleParser.StartContext):
        pass


    # Enter a parse tree produced by SimpleParser#methodDeclarations.
    def enterMethodDeclarations(self, ctx:SimpleParser.MethodDeclarationsContext):
        pass

    # Exit a parse tree produced by SimpleParser#methodDeclarations.
    def exitMethodDeclarations(self, ctx:SimpleParser.MethodDeclarationsContext):
        pass


    # Enter a parse tree produced by SimpleParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:SimpleParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:SimpleParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleParser#methodHeader.
    def enterMethodHeader(self, ctx:SimpleParser.MethodHeaderContext):
        pass

    # Exit a parse tree produced by SimpleParser#methodHeader.
    def exitMethodHeader(self, ctx:SimpleParser.MethodHeaderContext):
        pass


    # Enter a parse tree produced by SimpleParser#methodBody.
    def enterMethodBody(self, ctx:SimpleParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by SimpleParser#methodBody.
    def exitMethodBody(self, ctx:SimpleParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by SimpleParser#statement.
    def enterStatement(self, ctx:SimpleParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleParser#statement.
    def exitStatement(self, ctx:SimpleParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleParser#embeddedStatement.
    def enterEmbeddedStatement(self, ctx:SimpleParser.EmbeddedStatementContext):
        pass

    # Exit a parse tree produced by SimpleParser#embeddedStatement.
    def exitEmbeddedStatement(self, ctx:SimpleParser.EmbeddedStatementContext):
        pass


    # Enter a parse tree produced by SimpleParser#forStatement.
    def enterForStatement(self, ctx:SimpleParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SimpleParser#forStatement.
    def exitForStatement(self, ctx:SimpleParser.ForStatementContext):
        pass


    # Enter a parse tree produced by SimpleParser#relationalExpression.
    def enterRelationalExpression(self, ctx:SimpleParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by SimpleParser#relationalExpression.
    def exitRelationalExpression(self, ctx:SimpleParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by SimpleParser#variable.
    def enterVariable(self, ctx:SimpleParser.VariableContext):
        pass

    # Exit a parse tree produced by SimpleParser#variable.
    def exitVariable(self, ctx:SimpleParser.VariableContext):
        pass


    # Enter a parse tree produced by SimpleParser#forInitializer.
    def enterForInitializer(self, ctx:SimpleParser.ForInitializerContext):
        pass

    # Exit a parse tree produced by SimpleParser#forInitializer.
    def exitForInitializer(self, ctx:SimpleParser.ForInitializerContext):
        pass


    # Enter a parse tree produced by SimpleParser#forExpression.
    def enterForExpression(self, ctx:SimpleParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by SimpleParser#forExpression.
    def exitForExpression(self, ctx:SimpleParser.ForExpressionContext):
        pass


    # Enter a parse tree produced by SimpleParser#forIterator.
    def enterForIterator(self, ctx:SimpleParser.ForIteratorContext):
        pass

    # Exit a parse tree produced by SimpleParser#forIterator.
    def exitForIterator(self, ctx:SimpleParser.ForIteratorContext):
        pass


    # Enter a parse tree produced by SimpleParser#forLoop.
    def enterForLoop(self, ctx:SimpleParser.ForLoopContext):
        pass

    # Exit a parse tree produced by SimpleParser#forLoop.
    def exitForLoop(self, ctx:SimpleParser.ForLoopContext):
        pass


    # Enter a parse tree produced by SimpleParser#whileStatement.
    def enterWhileStatement(self, ctx:SimpleParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SimpleParser#whileStatement.
    def exitWhileStatement(self, ctx:SimpleParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SimpleParser#ifClause.
    def enterIfClause(self, ctx:SimpleParser.IfClauseContext):
        pass

    # Exit a parse tree produced by SimpleParser#ifClause.
    def exitIfClause(self, ctx:SimpleParser.IfClauseContext):
        pass


    # Enter a parse tree produced by SimpleParser#ifClauses.
    def enterIfClauses(self, ctx:SimpleParser.IfClausesContext):
        pass

    # Exit a parse tree produced by SimpleParser#ifClauses.
    def exitIfClauses(self, ctx:SimpleParser.IfClausesContext):
        pass


    # Enter a parse tree produced by SimpleParser#ifStatement.
    def enterIfStatement(self, ctx:SimpleParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SimpleParser#ifStatement.
    def exitIfStatement(self, ctx:SimpleParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SimpleParser#expression.
    def enterExpression(self, ctx:SimpleParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SimpleParser#expression.
    def exitExpression(self, ctx:SimpleParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SimpleParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:SimpleParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:SimpleParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleParser#methodCall.
    def enterMethodCall(self, ctx:SimpleParser.MethodCallContext):
        pass

    # Exit a parse tree produced by SimpleParser#methodCall.
    def exitMethodCall(self, ctx:SimpleParser.MethodCallContext):
        pass


    # Enter a parse tree produced by SimpleParser#assignment.
    def enterAssignment(self, ctx:SimpleParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimpleParser#assignment.
    def exitAssignment(self, ctx:SimpleParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimpleParser#operations.
    def enterOperations(self, ctx:SimpleParser.OperationsContext):
        pass

    # Exit a parse tree produced by SimpleParser#operations.
    def exitOperations(self, ctx:SimpleParser.OperationsContext):
        pass


    # Enter a parse tree produced by SimpleParser#variableType.
    def enterVariableType(self, ctx:SimpleParser.VariableTypeContext):
        pass

    # Exit a parse tree produced by SimpleParser#variableType.
    def exitVariableType(self, ctx:SimpleParser.VariableTypeContext):
        pass


    # Enter a parse tree produced by SimpleParser#methodName.
    def enterMethodName(self, ctx:SimpleParser.MethodNameContext):
        pass

    # Exit a parse tree produced by SimpleParser#methodName.
    def exitMethodName(self, ctx:SimpleParser.MethodNameContext):
        pass


    # Enter a parse tree produced by SimpleParser#variableName.
    def enterVariableName(self, ctx:SimpleParser.VariableNameContext):
        pass

    # Exit a parse tree produced by SimpleParser#variableName.
    def exitVariableName(self, ctx:SimpleParser.VariableNameContext):
        pass


    # Enter a parse tree produced by SimpleParser#pBooleanLiteral.
    def enterPBooleanLiteral(self, ctx:SimpleParser.PBooleanLiteralContext):
        pass

    # Exit a parse tree produced by SimpleParser#pBooleanLiteral.
    def exitPBooleanLiteral(self, ctx:SimpleParser.PBooleanLiteralContext):
        pass


    # Enter a parse tree produced by SimpleParser#pIntegerLiteral.
    def enterPIntegerLiteral(self, ctx:SimpleParser.PIntegerLiteralContext):
        pass

    # Exit a parse tree produced by SimpleParser#pIntegerLiteral.
    def exitPIntegerLiteral(self, ctx:SimpleParser.PIntegerLiteralContext):
        pass


    # Enter a parse tree produced by SimpleParser#pFloatLiteral.
    def enterPFloatLiteral(self, ctx:SimpleParser.PFloatLiteralContext):
        pass

    # Exit a parse tree produced by SimpleParser#pFloatLiteral.
    def exitPFloatLiteral(self, ctx:SimpleParser.PFloatLiteralContext):
        pass


    # Enter a parse tree produced by SimpleParser#pStringLiteral.
    def enterPStringLiteral(self, ctx:SimpleParser.PStringLiteralContext):
        pass

    # Exit a parse tree produced by SimpleParser#pStringLiteral.
    def exitPStringLiteral(self, ctx:SimpleParser.PStringLiteralContext):
        pass


    # Enter a parse tree produced by SimpleParser#methodCall_.
    def enterMethodCall_(self, ctx:SimpleParser.MethodCall_Context):
        pass

    # Exit a parse tree produced by SimpleParser#methodCall_.
    def exitMethodCall_(self, ctx:SimpleParser.MethodCall_Context):
        pass



del SimpleParser