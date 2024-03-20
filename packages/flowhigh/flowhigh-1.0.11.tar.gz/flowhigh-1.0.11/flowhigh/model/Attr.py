
from flowhigh.model.Direction import Direction
from flowhigh.model.BaseExpr import BaseExpr
from flowhigh.model.ReferencableExpr import ReferencableExpr
from flowhigh.model.TreeNode import TreeNode


class Attr(BaseExpr, ReferencableExpr, TreeNode):
    oref: str = None
    refsch: str = None
    refvar: str = None
    fullref: str = None
    refdb: str = None
    sref: str = None
    refds: str = None
    refatt: str = None
    refoutidx: str = None
    

    def __init__(self):
        super().__init__()



from flowhigh.model.TreeNode import TreeNode

class AttrBuilder (object):
    construction: Attr
    

    def __init__(self) -> None:
        super().__init__()
        self.construction = Attr()
    
    def with_oref(self, oref: str):
        child = oref
        self.construction.oref = child
    
    def with_refsch(self, refsch: str):
        child = refsch
        self.construction.refsch = child
    
    def with_fullref(self, fullref: str):
        child = fullref
        self.construction.fullref = child
    
    def with_refvar(self, refvar: str):
        child = refvar
        self.construction.refvar = child
    
    def with_refdb(self, refdb: str):
        child = refdb
        self.construction.refdb = child
    
    def with_sref(self, sref: str):
        child = sref
        self.construction.sref = child
    
    def with_pos(self, pos: str):
        child = pos
        self.construction.pos = child
    
    def with_refds(self, refds: str):
        child = refds
        self.construction.refds = child
    
    def with_refatt(self, refatt: str):
        child = refatt
        self.construction.refatt = child
    
    def with_alias(self, alias: str):
        child = alias
        self.construction.alias = child
    
    def with_refoutidx(self, refoutidx: str):
        child = refoutidx
        self.construction.refoutidx = child
    
    def with_direction(self, direction: Direction):
        child = direction
        self.construction.direction = child

    def build(self):
        return self.construction
