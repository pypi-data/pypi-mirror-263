
from flowhigh.model.WFuncType import WFuncType
from flowhigh.model.WrappedExpr import WrappedExpr
from flowhigh.model.Sort import Sort
from flowhigh.model.Frame import Frame
from flowhigh.model.Direction import Direction
from flowhigh.model.BaseExpr import BaseExpr
from flowhigh.model.TypeCast import TypeCast
from flowhigh.model.Ordered import Ordered


class Wfunc(BaseExpr, TypeCast, Ordered):
    partition: list = []
    name: str = None
    expr: WrappedExpr = None
    sort: Sort = None
    type_: WFuncType = None
    frame: Frame = None
    

    def __init__(self):
        super().__init__()



from flowhigh.model.TreeNode import TreeNode

class WfuncBuilder (object):
    construction: Wfunc
    

    def __init__(self) -> None:
        super().__init__()
        self.construction = Wfunc()
    
    def with_partition(self, partition: list):
        child = partition
        for node in list(filter(lambda el: TreeNode in el.__class__.mro(), partition)):
            self.construction.add_child(node)
        self.construction.partition = child
    
    def with_pos(self, pos: str):
        child = pos
        self.construction.pos = child
    
    def with_name(self, name: str):
        child = name
        self.construction.name = child
    
    def with_alias(self, alias: str):
        child = alias
        self.construction.alias = child
    
    def with_expr(self, expr: WrappedExpr):
        child = expr
        if TreeNode in WrappedExpr.mro():
            self.construction.add_child(child)
        self.construction.expr = child
    
    def with_sort(self, sort: Sort):
        child = sort
        if TreeNode in Sort.mro():
            self.construction.add_child(child)
        self.construction.sort = child
    
    def with_type(self, type_: WFuncType):
        child = type_
        self.construction.type_ = child
    
    def with_frame(self, frame: Frame):
        child = frame
        if TreeNode in Frame.mro():
            self.construction.add_child(child)
        self.construction.frame = child
    
    def with_direction(self, direction: Direction):
        child = direction
        self.construction.direction = child

    def build(self):
        return self.construction
