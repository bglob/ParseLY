grammar PythonProject;

/*Parser Rules */

//Start program
start: ((expr) (NEWLINE+ | EOF))+;

expr: (arithmetic | concat | assignment | ifStatement | singleLineComment | multiLineComment);
variable: VARNAME;
assignValue: (variable | NUMBER | BOOL | DECIMAL | STRING);
arithmetic: assignValue (WS* arithmetOP WS* assignValue)*;
arithmetOP: ('+' | '-' | '*' | '/' | '%');
concat: variable (WS* '+' WS*) variable;
assignment: (variable WS* assignOP WS*) (expr | NEWLINE);
assignOP: ('=' | '+=' | '-=' | '*=' | '/=');
ifStatement: IF WS+ conditional ':' (NEWLINE TAB expr)+ (NEWLINE TAB? elseStatement)?;
elseStatement: ELSE ':' (NEWLINE TAB expr)+;
conditional: NOT? WS* variable (WS* conditionOP WS* assignValue?)* (conditional)?;
conditionOP: ('<' | '<=' | '>' | '>=' | '==' | '!=' | 'and' | 'or');

singleLineComment: '#' (WS | LETTER | NUMBER | arithmetOP | assignOP | conditionOP)* NEWLINE;
multiLineComment: '"""' (WS | LETTER | NUMBER | arithmetOP | assignOP | conditionOP | NEWLINE)* '"""';

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
NOT: 'not';
TAB: ([\t] | '    ')+;
IF: 'if';
ELSE: 'else';

VARNAME: LETTER (LETTER | NUMBER)*;
WS: [ ]+;
NEWLINE: ('\n' | '\r')+;
