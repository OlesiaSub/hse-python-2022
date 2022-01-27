import _ast
import ast
import inspect
from typing import Any
import networkx as nx


class MyASTVisitor(ast.NodeVisitor):
    def __init__(self):
        self.ast_graph = nx.DiGraph()
        self.store = self.load = None
        self.store_cnt = self.load_cnt = 0

    def increase_cnt(self):
        self.store_cnt += 1
        self.load_cnt += 1

    def process_visit_result(self, node, node_to_visit):
        visit_res = self.visit(node_to_visit)
        if visit_res is not None:
            for i in visit_res:
                if i is not None:
                    self.ast_graph.add_edge(str(node), i)

    def visit_FunctionDef(self, node: _ast.FunctionDef) -> Any:
        self.ast_graph.add_node(str(node), label=f'function: {node.name}', color='#CD8C95', style='bold')
        for a in node.args.args:
            self.ast_graph.add_node(a, label=f'arg: {a.arg}', color='#8B3E2F', style='bold')
            self.ast_graph.add_edge(str(node), a)
        for b in node.body:
            self.process_visit_result(node, b)

    def visit_Assign(self, node: _ast.Assign) -> Any:
        self.increase_cnt()
        self.ast_graph.add_node(str(node), label="assignment", color='#53868B', style='bold')
        self.process_visit_result(node, node.targets[0])
        self.process_visit_result(node, node.value)
        return [str(node)]

    def visit_Name(self, node: _ast.Name) -> Any:
        ret_list = [str(node)]
        self.ast_graph.add_node(str(node), label=node.id, color='#009ACD', style='bold')
        ast.NodeVisitor.generic_visit(self, node)
        if self.store is not None:
            ret_list.append(str(self.store))
        if self.load is not None:
            ret_list.append(str(self.load))
        self.load = self.store = None
        return ret_list

    def visit_Expr(self, node: _ast.Expr) -> Any:
        self.ast_graph.add_node(str(node), label="expr", color='#00C957', style='bold')
        self.process_visit_result(node, node.value)
        return [str(node)]

    def visit_Call(self, node: _ast.Call) -> Any:
        self.ast_graph.add_node(str(node), label="call", color='#00C957', style='bold')
        self.process_visit_result(node, node.func)
        self.process_visit_result(node, node.args[0])
        return [str(node)]

    def visit_For(self, node: _ast.For) -> Any:
        self.increase_cnt()
        self.ast_graph.add_node(str(node), label="for", color='#8B6914', style='bold')
        node.body.extend((node.iter, node.target))
        for b in node.body:
            self.increase_cnt()
            self.process_visit_result(node, b)
        return [str(node)]

    def visit_If(self, node: _ast.If) -> Any:
        self.ast_graph.add_node(str(node), label="if", color='#8B6914', style='bold')
        node.body.append(node.test)
        for b in node.body:
            self.process_visit_result(node, b)
        return [str(node)]

    def visit_BinOp(self, node: _ast.BinOp) -> Any:
        self.ast_graph.add_node(str(node), label="BinOp", color='#8A2BE2', style='bold')
        self.process_visit_result(node, node.left)
        self.process_visit_result(node, node.op)
        self.process_visit_result(node, node.right)
        return [str(node)]

    def visit_Compare(self, node: _ast.Compare) -> Any:
        self.increase_cnt()
        self.ast_graph.add_node(str(node), label="comparison", color='#00C957', style='bold')
        self.process_visit_result(node, node.left)
        self.process_visit_result(node, node.comparators[0])
        self.process_visit_result(node, node.ops[0])
        return [str(node)]

    def visit_Load(self, node: _ast.Load) -> Any:
        self.ast_graph.add_node(str(node) + str(self.load_cnt), label="op=Load", color='#808080', style='bold')
        self.load = str(node) + str(self.load_cnt)
        return [self.load]

    def visit_Store(self, node: _ast.Store) -> Any:
        self.ast_graph.add_node(str(node) + str(self.store_cnt), label="op=Store", color='#808080', style='bold')
        self.store = str(node) + str(self.store_cnt)
        return [self.store]

    def visit_Add(self, node: _ast.Add) -> Any:
        self.ast_graph.add_node(str(node), label="op=Add", color='#8A2BE2', style='bold')
        return [str(node)]

    def visit_Eq(self, node: _ast.Eq) -> Any:
        self.ast_graph.add_node(str(node), label="cond=Eq", color='#8A2BE2', style='bold')
        return [str(node)]

    def visit_Constant(self, node: _ast.Constant) -> Any:
        self.ast_graph.add_node(str(node), label="const: " + str(node.value), color='#009ACD', style='bold')
        return [str(node)]


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


if __name__ == '__main__':
    visitor = MyASTVisitor()
    visitor.visit(ast.parse(inspect.getsource(fib_seq)))
    G = visitor.ast_graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    p = nx.drawing.nx_pydot.to_pydot(G)
    p.write_png('artifacts/fib_ast.png')
