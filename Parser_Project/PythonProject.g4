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
ifStatement: IF WS+ conditional ':' (NEWLINE TAB expr)+ (NEWLINE TAB? elseStatement)?;
elseStatement: ELSE ':' (NEWLINE TAB expr)+;
whileStatement: 'while' WS+ conditional ':' (NEWLINE TAB expr)+ (NEWLINE elseStatement)?;
forStatement: 'for' WS+ variable WS+ 'in' WS+ (variable | STRING) ':' (NEWLINE TAB expr)+ (NEWLINE elseStatement)?;
conditional: NOT? WS* variable (WS* conditionOP WS* assignValue?)* (conditional)?;
conditionOP: ('<' | '<=' | '>' | '>=' | '==' | '!=' | 'and' | 'or');

singleLineComment: '#' (SENTENCE | SPECIAL)*;
multiLineComment: '"""' ~[\\]* '"""';
comment: singleLineComment | multiLineComment;
/*Lexer Rules */

//Added stuff that may/ may not need.
fragment LOWER: [a-z];
fragment UPPER: [A-Z];
fragment DIGIT: [0-9];
fragment NEGATIVE: '-';
fragment SPECIALCHAR: '!'..'/' | ':'..'@' | '['..'`' | '{'..'~';

NUMBER: NEGATIVE? DIGIT+;
DECIMAL: NUMBER '.' NUMBER;
BOOL: 'True' | 'False';
SPECIAL: SPECIALCHAR;
LETTER: (LOWER | UPPER)+;
SENTENCE: (LETTER | NUMBER | WS)+;
STRING: ('"'SENTENCE*'"') | ('\''SENTENCE*'\'');
NOT: 'not';
TAB: ([\t] | '    ')+;
IF: 'if';
ELSE: 'else';

VARNAME: LETTER (LETTER | NUMBER)*;
WS: [ ]+;
NEWLINE: ('\n' | '\r')+;
