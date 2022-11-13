grammar PythonProject;

/*Parser Rules */

//Start program
start: ((expr) (NEWLINE+ | EOF))+;

expr: (arithmetic | concat);
variable: VARNAME;
assignValue: (variable | NUMBER | BOOL | DECIMAL);
arithmetic: assignValue (WS* arithmetOP WS* assignValue)+;
arithmetOP: ('+' | '-' | '*' | '/' | '%');
concat: variable (WS* '+' WS*) variable;
assignment: (variable WS* assignOP WS*) (expr);
assignOP: ('=' | '+=' | '-=' | '*=' | '/=');

/*Lexer Rules */

//Added stuff that may/ may not need.
fragment LOWER: [a-z];
fragment UPPER: [A-Z];
fragment DIGIT: [0-9];

NUMBER: DIGIT+;
DECIMAL: NUMBER '.' NUMBER;
BOOL: 'True' | 'False';
LETTER: (LOWER | UPPER);
//Need to figure out how to do strings.

VARNAME: LETTER (LETTER | NUMBER)*;
WS: [ ]+;
NEWLINE: ('\n' | '\r')+;
