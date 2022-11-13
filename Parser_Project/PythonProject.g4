grammar PythonProject;

/*Parser Rules */

//Start program
start: ((expr) (NEWLINE+))+;

expr: (arithmatic | concat);
variable: VARNAME;
arithmatic: ('+' | '-' | '*' | '/' | '%');
concat: variable (WS* '+' WS*) variable;
assignment: (variable WS* arithmatic WS*) (expr);

/*Lexer Rules */

//Added stuff that may/ may not need.
fragment LOWER: [a-z];
fragment UPPER: [A-Z];
fragment DIGIT: [0-9];

NUMBER: DIGIT+;
DECIMAL: NUMBER '.' NUMBER;
BOOL: 'Ture' | 'False';
LETTER: (LOWER | UPPER);
//Need to figure out how to do strings.

VARNAME: LETTER (LETTER | NUMBER)*;
WS: [\t\r\n]+ -> skip;
NEWLINE: ('\r'? '\r' | '\r')+;