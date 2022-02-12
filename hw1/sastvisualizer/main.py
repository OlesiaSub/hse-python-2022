import ast
import inspect
import networkx as nx
from .my_ast_visitor import MyASTVisitor


def fib_seq(n: int):
    nxt = 1
    cur = 0
    if n == 1:
        print(0)
    for i in range(n):
        print(cur)
        prev = cur
        cur = nxt
        nxt = prev + cur


def generate_ast(path):
    visitor = MyASTVisitor()
    visitor.visit(ast.parse(inspect.getsource(fib_seq)))
    G = visitor.ast_graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    p = nx.drawing.nx_pydot.to_pydot(G)
    p.write_png(path)


if __name__ == '__main__':
    generate_ast('fib_ast.png')
