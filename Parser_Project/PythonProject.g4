grammar PythonProject;

/*Parser Rules */

//Start program
start: ((expr) (NEWLINE+ | EOF))+;

expr: (arithmetic | concat | assignment | if);
variable: VARNAME;
assignValue: (variable | NUMBER | BOOL | DECIMAL | STRING);
arithmetic: assignValue (WS* arithmetOP WS* assignValue)*;
arithmetOP: ('+' | '-' | '*' | '/' | '%');
concat: variable (WS* '+' WS*) variable;
assignment: (variable WS* assignOP WS*) (expr | NEWLINE);
assignOP: ('=' | '+=' | '-=' | '*=' | '/=');
if: 'if' WS+ conditional ':' NEWLINE '\t' expr* else? 
else: 'else' '\t' expr*;
conditional: variable (WS* conditionOP WS* assignValue)* (andor conditional)?;
conditionOP: ('<' | '<=' | '>' | '>=' | '==' | '!=' | 'not');
andor: ('and' | 'or');

/*Lexer Rules */

//Added stuff that may/ may not need.
fragment LOWER: [a-z];
fragment UPPER: [A-Z];
fragment DIGIT: [0-9];
fragment NEGATIVE: '-';

NUMBER: NEGATIVE? DIGIT+;
DECIMAL: NUMBER '.' NUMBER;
BOOL: 'True' | 'False';
LETTER: (LOWER | UPPER);
STRING: ('"'(LETTER | NUMBER | WS)*'"') | ('\''(LETTER | NUMBER | WS)*'\'');

VARNAME: LETTER (LETTER | NUMBER)*;
WS: [ ]+;
NEWLINE: ('\n' | '\r')+;
