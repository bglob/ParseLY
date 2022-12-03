grammar PythonProject;

/*Parser Rules */

//Start program
start: ((expr) (NEWLINE+ | EOF))+;

expr: (arithmetic | concat | assignment | ifStatement | whileStatement | forStatement | comment);
variable: VARNAME;
assignValue: (variable | NUMBER | BOOL | DECIMAL | STRING);
arithmetic: assignValue (WS* arithmetOP WS* assignValue)*;
arithmetOP: ('+' | '-' | '*' | '/' | '%');
concat: variable (WS* '+' WS*) variable;
assignment: (variable WS* assignOP WS*) (expr | NEWLINE);
assignOP: ('=' | '+=' | '-=' | '*=' | '/=');
ifStatement: 'if' WS+ conditional ':' (NEWLINE TAB expr)+ (NEWLINE TAB? elseStatement)?;
elseStatement: 'else' ':' (NEWLINE TAB expr)+;
whileStatement: 'while' WS+ conditional ':' (NEWLINE TAB expr)+;
forStatement: 'for' WS+ variable WS+ 'in' WS+ (variable | STRING) ':' (NEWLINE TAB expr)+;
conditional: NOT? WS* variable (WS* conditionOP WS* assignValue?)* (conditional)?;
conditionOP: ('<' | '<=' | '>' | '>=' | '==' | '!=' | 'and' | 'or');



comment: SingleLineComment | MultiLineComment;
/*Lexer Rules */

//Added stuff that may/ may not need.
fragment LOWER: [a-z];
fragment UPPER: [A-Z];
fragment DIGIT: [0-9];
fragment NEGATIVE: '-';

VARNAME: LETTER (LETTER | NUMBER)*;
SingleLineComment: '#' ~[\r\n]*;
MultiLineComment: '"""' ~[\\]* '"""';
NUMBER: NEGATIVE? DIGIT+;
DECIMAL: NUMBER '.' NUMBER;
BOOL: 'True' | 'False';
LETTER: (LOWER | UPPER);
STRING: ('"'~[\n\r]*'"') | ('\''~[\n\r]*'\'');
NOT: 'not';
TAB: ([\t] | '    ')+;


WS: [ ]+;
NEWLINE: ('\n' | '\r')+;
