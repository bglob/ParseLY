import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor

def main(argv):
    io_stream = FileStream(argv[1])
    lexer = MyGrammerLexer(io_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammerParser(stream)
    tree = parser.start() 
    print(Trees.toStringTree(tree, None, parser))
    
if __name__ == "__main__":
    main(sys.argv)