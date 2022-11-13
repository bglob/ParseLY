import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from PythonProjectLexer import PythonProjectLexer
from PythonProjectParser import PythonProjectParser
from PythonProjectListener import PythonProjectListener

def main(argv):
    io_stream = FileStream(argv[1])
    lexer = PythonProjectLexer(io_stream)
    stream = CommonTokenStream(lexer)
    parser = PythonProjectParser(stream)
    tree = parser.start() 
    print(Trees.toStringTree(tree, None, parser))
    
if __name__ == "__main__":
    main(sys.argv)