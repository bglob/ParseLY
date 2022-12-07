grammar PythonProject;

/*Parser Rules */

//Start program
start: ((expr) (NEWLINE+ | EOF))+;

expr: (arithmetic | concat | assignment | ifStatement | whileStatement | forStatement | comment | function | functionCall);
variable: VARNAME;
assignValue: (variable | NUMBER | BOOL | DECIMAL | STRING);
arithmetic: assignValue (WS* arithmetOP WS* assignValue)*;
arithmetOP: ('+' | '-' | '*' | '/' | '%');
concat: variable (WS* '+' WS*) variable;
assignment: (variable WS* assignOP WS*) (expr | NEWLINE);
assignOP: ('=' | '+=' | '-=' | '*=' | '/=');
ifStatement: 'if' WS+ conditional ':' block (NEWLINE TAB? elseStatement)?;
elseStatement: 'else' ':' block;
whileStatement: 'while' WS+ conditional ':' block;
forStatement: 'for' WS+ variable WS+ 'in' WS+ (variable | STRING) ':' block;
conditional: NOT? WS* variable (WS* conditionOP WS* assignValue?)* (conditional)?;
conditionOP: ('<' | '<=' | '>' | '>=' | '==' | '!=' | 'and' | 'or');
block:(NEWLINE TAB expr)+;
function:'def' WS+ VARNAME '(' WS* parameters* WS*')' WS* ':' block ( NEWLINE TAB 'return' WS+ expr)?;
parameters: variable (',' WS* variable)*;
functionCall: VARNAME '(' WS* passing* WS* ')';
passing: assignValue (',' WS* assignValue)*;
comment: SINGLELINECOMMENT | MULTILINECOMMENT;


/*Lexer Rules */

//Added stuff that may/ may not need.
fragment LOWER: [a-z];
fragment UPPER: [A-Z];
fragment DIGIT: [0-9];
fragment NEGATIVE: '-';

VARNAME: LETTER (LETTER | NUMBER)*;
SINGLELINECOMMENT: '#' ~[\r\n]*;
MULTILINECOMMENT: '"""' ~[\\]* '"""';
NUMBER: NEGATIVE? DIGIT+;
DECIMAL: NUMBER '.' NUMBER;
BOOL: 'True' | 'False';
LETTER: (LOWER | UPPER);
STRING: ('"'~[\n\r]*'"') | ('\''~[\n\r]*'\'');
NOT: 'not';
TAB: ([\t] | '    ')+;


WS: [ ]+;
NEWLINE: ('\n' | '\r')+;
