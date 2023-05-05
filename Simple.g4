grammar Simple;
/*
 * Parser Rules
 */

start : methodDeclarations? EOF;
methodDeclarations : methodDeclaration+;
methodDeclaration : methodHeader methodBody;
methodHeader : 'public' 'static' 'void' methodName '(' ')';
methodBody : '{' statement* '}';
statement
	: forStatement
	| ifStatement
	| whileStatement
	| embeddedStatement ';'
	;
embeddedStatement
	: localVariableDeclaration
	| methodCall				
	| assignment				
	;
forStatement : forLoop ;


relationalExpression
	: ('<' | '>' | '<=' | '>=' | '==');

variable
	: (variableName | variableValue);

forInitializer
	: localVariableDeclaration;
forExpression
	: variableName relationalExpression variableValue;
forIterator
	: (INC | DEC) variableName;
forLoop
	: FOR '(' forInitializer ';' forExpression ';' forIterator ')' methodBody;

whileStatement
	: WHILE '(' ifClauses ')' methodBody;

ifClause
	: variable relationalExpression variable;
ifClauses
	: ifClause ((AND | OR) ifClause)*;
ifStatement
	: IF '(' ifClauses ')' methodBody (ELSE methodBody)?;


expression
	: variable (operations variable)*;
localVariableDeclaration 
	: variableType variableName ('=' variableValue)? ;
methodCall 
	: methodName '(' ')' ';'*;
assignment
	: variableName ASSIGNMENT expression; 

operations
	: '+' | '-' | '/' | '*' | '&' | '~' | '^';
variableType 
	: 'int' | 'byte' | 'string' | 'bool' | 'float' | 'double';
methodName : WORD;
variableName : WORD;
variableValue
	: BooleanLiteral	#pBooleanLiteral
	| IntegerLiteral	#pIntegerLiteral
	| FloatLiteral 		#pFloatLiteral
	| StringLiteral		#pStringLiteral
	| methodCall		#methodCall_
	;

BooleanLiteral : 'true' | 'false';
IntegerLiteral : '-'? [0-9]+;
StringLiteral : '"' .*? '"';
FloatLiteral : '-'? [0-9]+ '.' [0-9]+;


FOR 				: 'for';
WHILE				: 'while';
IF					: 'if';
ELSE				: 'else';
AND					: '&&';
OR 					: '||';
ASSIGNMENT			: '=';
INC					: '++';
DEC					: '--';
WORD                : [a-zA-Z_]+ ;
WHITESPACE          :  [ \t\n]+ -> skip;
NEWLINE             : ('\r'? '\n' | '\r')+ ;

