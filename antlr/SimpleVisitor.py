# Generated from /home/Projects/antlr/Simple.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleParser import SimpleParser
else:
    from SimpleParser import SimpleParser

# This class defines a complete generic visitor for a parse tree produced by SimpleParser.

class SimpleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleParser#start.
    def visitStart(self, ctx:SimpleParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#methodDeclarations.
    def visitMethodDeclarations(self, ctx:SimpleParser.MethodDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:SimpleParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#methodHeader.
    def visitMethodHeader(self, ctx:SimpleParser.MethodHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#methodBody.
    def visitMethodBody(self, ctx:SimpleParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#statement.
    def visitStatement(self, ctx:SimpleParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#embeddedStatement.
    def visitEmbeddedStatement(self, ctx:SimpleParser.EmbeddedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#forStatement.
    def visitForStatement(self, ctx:SimpleParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#relationalExpression.
    def visitRelationalExpression(self, ctx:SimpleParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#variable.
    def visitVariable(self, ctx:SimpleParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#forInitializer.
    def visitForInitializer(self, ctx:SimpleParser.ForInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#forExpression.
    def visitForExpression(self, ctx:SimpleParser.ForExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#forIterator.
    def visitForIterator(self, ctx:SimpleParser.ForIteratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#forLoop.
    def visitForLoop(self, ctx:SimpleParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#whileStatement.
    def visitWhileStatement(self, ctx:SimpleParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#ifClause.
    def visitIfClause(self, ctx:SimpleParser.IfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#ifClauses.
    def visitIfClauses(self, ctx:SimpleParser.IfClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#ifStatement.
    def visitIfStatement(self, ctx:SimpleParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#expression.
    def visitExpression(self, ctx:SimpleParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:SimpleParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#methodCall.
    def visitMethodCall(self, ctx:SimpleParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#assignment.
    def visitAssignment(self, ctx:SimpleParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#operations.
    def visitOperations(self, ctx:SimpleParser.OperationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#variableType.
    def visitVariableType(self, ctx:SimpleParser.VariableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#methodName.
    def visitMethodName(self, ctx:SimpleParser.MethodNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#variableName.
    def visitVariableName(self, ctx:SimpleParser.VariableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#pBooleanLiteral.
    def visitPBooleanLiteral(self, ctx:SimpleParser.PBooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#pIntegerLiteral.
    def visitPIntegerLiteral(self, ctx:SimpleParser.PIntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#pFloatLiteral.
    def visitPFloatLiteral(self, ctx:SimpleParser.PFloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#pStringLiteral.
    def visitPStringLiteral(self, ctx:SimpleParser.PStringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleParser#methodCall_.
    def visitMethodCall_(self, ctx:SimpleParser.MethodCall_Context):
        return self.visitChildren(ctx)



del SimpleParser