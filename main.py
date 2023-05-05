import sys
from antlr4 import *
from antlr.SimpleLexer import SimpleLexer
from antlr.SimpleParser import SimpleParser
from antlr.SimpleVisitor import SimpleVisitor


def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[ 0 ]

  
class MyVisitor(SimpleVisitor):
    def __init__(self):
        self.contextLevel = 0

    def getIndentation(self, contextLevel):
        return "    " * contextLevel

    def visitStart(self, ctx):
        return self.visit(ctx.methodDeclarations())
    
    def visitMethodDeclarations(self, ctx):
        pythonMethods = [self.getIndentation(self.contextLevel) + self.visit(ctx.methodDeclaration(i)) for i in range(len(ctx.methodDeclaration()))]
        return "\n\n".join(pythonMethods)
    
    def visitMethodDeclaration(self, ctx):
        pythonMethodHeader = self.getIndentation(self.contextLevel) + self.visit(ctx.methodHeader())
        self.contextLevel += 1
        pythonMethodBody = self.visit(ctx.methodBody())
        return f"{pythonMethodHeader}\n{pythonMethodBody}"

    def visitMethodBody(self, ctx):
        pythonLines = [self.getIndentation(self.contextLevel) + self.visit(ctx.statement(i)) for i in range(len(ctx.statement()))]
        self.contextLevel -= 1
        return "\n".join(pythonLines)
    
    def visitStatement(self, ctx):
        for c in ctx.getChildren():
            if c is not None:
                return self.visit(c)

    def visitLocalVariableDeclaration(self, ctx):
        varName = ctx.variableName().getText()
        varType = ctx.variableType().getText()
        varType = varType.replace('string', 'str')
        varType = varType.replace('double', 'float')
        result = f"{varName} : {varType}"

        variableValueContext = ctx.variableValue()
        if variableValueContext is not None:
            temp = self.visit(variableValueContext)
            temp = temp.replace('true', 'True')
            temp = temp.replace('false', 'False')
            result += f" = {temp}"

        return result
    
    def visitPBooleanLiteral(self, ctx):
        return ctx.getText()

    def visitPIntegerLiteral(self, ctx):
        return ctx.getText()
    
    def visitPFloatLiteral(self, ctx):
        return ctx.getText()

    def visitPStringLiteral(self, ctx):
        return ctx.getText()
    
    def visitMethodCall(self, ctx):
        methodName = ctx.methodName().getText()
        return f"{methodName.lower()}()"

    def visitMethodHeader(self, ctx):
        return f"def {ctx.methodName().getText().lower()}():"
    
    def visitForLoop(self, ctx):
        forLoopInitialized = ctx.forInitializer().localVariableDeclaration().variableValue().getText()
        forLoopVariable = ctx.forIterator().variableName().getText()
        forLoopBound = self.visit(ctx.forExpression().variableValue())
        forLoopOperator = ctx.forExpression().relationalExpression().getText() in ["<=", ">="]
        pythonRange = int(forLoopBound) - int(forLoopInitialized) + 1 * forLoopOperator
        pythonForLoopHeader = f"for {forLoopVariable} in range({pythonRange}):"
        self.contextLevel += 1
        pythonMethodBody = self.visit(ctx.methodBody())
        return f"{pythonForLoopHeader}\n{pythonMethodBody}"

    def visitIfStatement(self, ctx):
        pythonIf = "if "
        pythonIfOperands = []
        pythonIfLogicals = []
        for clause in ctx.ifClauses().getChildren():
            if clause.getChildCount() == 0:
                logicalSharp = clause.getText()
                logicalPython = {'&&': 'and', '||': 'or'}[logicalSharp]
                pythonIfLogicals.append(logicalPython)
                continue
            lhs = clause.variable()[0].getText()
            op = clause.relationalExpression().getText()
            rhs = clause.variable()[1].getText()
            pythonIfOperands.append(f"{lhs} {op} {rhs}")
        for i, operand in enumerate(pythonIfOperands):
            pythonIf += operand
            if i != len(pythonIfOperands) - 1:
                pythonIf += f" {pythonIfLogicals[i]} "
        pythonIf += ":"
        self.contextLevel += 1
        ifBody = ctx.methodBody()[0]
        pythonIfMethodBody = self.visit(ifBody)
        if ctx.ELSE() is not None:
            pythonElse = self.getIndentation(self.contextLevel) + "else:"
            self.contextLevel += 1
            elseBody = ctx.methodBody()[1]
            pythonElseMethodBody = self.visit(elseBody)
            return f"{pythonIf}\n{pythonIfMethodBody}\n{pythonElse}\n{pythonElseMethodBody}"
        return f"{pythonIf}\n{pythonIfMethodBody}"

    def visitWhileStatement(self, ctx):
        pythonWhile= "while "
        pythonIfOperands = []
        pythonIfLogicals = []
        for clause in ctx.ifClauses().getChildren():
            if clause.getChildCount() == 0:
                logicalSharp = clause.getText()
                logicalPython = {'&&': 'and', '||': 'or'}[logicalSharp]
                pythonIfLogicals.append(logicalPython)
                continue
            lhs = clause.variable()[0].getText()
            op = clause.relationalExpression().getText()
            rhs = clause.variable()[1].getText()
            pythonIfOperands.append(f"{lhs} {op} {rhs}")
        for i, operand in enumerate(pythonIfOperands):
            pythonWhile += operand
            if i != len(pythonIfOperands) - 1:
                pythonWhile += f" {pythonIfLogicals[i]} "
        pythonWhile += ":"
        self.contextLevel += 1
        pythonMethodBody = self.visit(ctx.methodBody())
        return f"{pythonWhile}\n{pythonMethodBody}"
    
    def visitAssignment(self, ctx):
        lhs = ctx.variableName().getText()
        rhs = ""
        for child in ctx.expression().getChildren():
            rhs += f" {child.getText()}"
        return f"{lhs} ={rhs}"



if __name__ == "__main__":
    with open("code_csharp.txt") as f:
        file = f.read()
    data = InputStream(file)
    # lexer
    lexer = SimpleLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = SimpleParser(stream)
    tree = parser.start()
    # evaluator
    visitor = MyVisitor()
    output = visitor.visit(tree)
    with open("output.py", 'w') as f:
        f.write(output)