grammar MyGrammer;
start: (expr NEWLINE)*;
expr: expr ('*' | '/' | '%') expr
    | expr ('+' | '-') expr
    | INT
    | '(' expr ')';

NEWLINE : [\n]+;
INT     : [0-9]+;