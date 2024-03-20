
from flowhigh.model.WrappedExpr import WrappedExpr
from flowhigh.model.Direction import Direction
from flowhigh.model.BaseExpr import BaseExpr


class Else(BaseExpr):
    expr: WrappedExpr = None
    

    def __init__(self):
        super().__init__()



from flowhigh.model.TreeNode import TreeNode

class ElseBuilder (object):
    construction: Else
    

    def __init__(self) -> None:
        super().__init__()
        self.construction = Else()
    
    def with_pos(self, pos: str):
        child = pos
        self.construction.pos = child
    
    def with_alias(self, alias: str):
        child = alias
        self.construction.alias = child
    
    def with_expr(self, expr: WrappedExpr):
        child = expr
        if TreeNode in WrappedExpr.mro():
            self.construction.add_child(child)
        self.construction.expr = child
    
    def with_direction(self, direction: Direction):
        child = direction
        self.construction.direction = child

    def build(self):
        return self.construction
