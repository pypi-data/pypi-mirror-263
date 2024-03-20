import json
import requests
import urllib.parse

from requests import RequestException, Timeout
from typing import Tuple, Union

from flowhigh.auth import Authentication
from flowhigh.model.TreeNode import RegistryBase
from flowhigh.model import *
from flowhigh.model.Cast import CastBuilder
from flowhigh.model.CreateStageStatement import CreateStageStatementBuilder
from flowhigh.model.Op import OpBuilder
from flowhigh.model.Frame import FrameBuilder
from flowhigh.model.AlterTableStatement import AlterTableStatementBuilder
from flowhigh.model.Rotate import RotateBuilder
from flowhigh.model.Func import FuncBuilder
from flowhigh.model.In import InBuilder
from flowhigh.model.Page import PageBuilder
from flowhigh.model.DeleteStatement import DeleteStatementBuilder
from flowhigh.model.Attr import AttrBuilder
from flowhigh.model.InsertStatement import InsertStatementBuilder
from flowhigh.model.Case import CaseBuilder
from flowhigh.model.DBO import DBOBuilder
from flowhigh.model.StructRef import StructRefBuilder
from flowhigh.model.AntiPatterns import AntiPatternsBuilder
from flowhigh.model.Sort import SortBuilder
from flowhigh.model.Then import ThenBuilder
from flowhigh.model.DBOHier import DBOHierBuilder
from flowhigh.model.MatchRecognize import MatchRecognizeBuilder
from flowhigh.model.Asterisk import AsteriskBuilder
from flowhigh.model.MergeStatement import MergeStatementBuilder
from flowhigh.model.Agg import AggBuilder
from flowhigh.model.AntiPattern import AntiPatternBuilder
from flowhigh.model.UpdateStatement import UpdateStatementBuilder
from flowhigh.model.CreateViewStatement import CreateViewStatementBuilder
from flowhigh.model.QueryingStage import QueryingStageBuilder
from flowhigh.model.CopyStatement import CopyStatementBuilder
from flowhigh.model.Position import PositionBuilder
from flowhigh.model.Statement import StatementBuilder
from flowhigh.model.Const import ConstBuilder
from flowhigh.model.CreateTableStatement import CreateTableStatementBuilder
from flowhigh.model.ParSeQL import ParSeQLBuilder
from flowhigh.model.Join import JoinBuilder
from flowhigh.model.TableSample import TableSampleBuilder
from flowhigh.model.WrappedExpr import WrappedExprBuilder
from flowhigh.model.Ds import DsBuilder
from flowhigh.model.Out import OutBuilder
from flowhigh.model.Array import ArrayBuilder
from flowhigh.model.When import WhenBuilder
from flowhigh.model.Filter import FilterBuilder
from flowhigh.model.TableFunc import TableFuncBuilder
from flowhigh.model.Else import ElseBuilder
from flowhigh.model.Row import RowBuilder
from flowhigh.model.Current import CurrentBuilder
from flowhigh.model.Edge import EdgeBuilder


class FlowHighSubmissionClass (object):

    _message: dict

    @property
    def json_message(self):
        return json.dumps({k: v for k, v in self._message.items() if k != 'xml'}, indent=4)

    @property
    def xml_message(self):
        return self._message['xml']

    def __init__(self, response: dict):
        self._message = response
        self._parsed_tree = self._convert_node(response)

    @classmethod
    def from_txt_response(cls, res: str):
        json_data = json.loads(res)
        return cls(response=json_data)

    @classmethod
    def make_api_request(cls, method, url, headers, data=None, timeout=5):
        access_token = Authentication.authenticate_user()
        assert access_token, "UNAUTHENTICATED!"
        try:
            headers["Authorization"] = "Bearer " + access_token
            response = requests.request(method, url, json=data, headers=headers, timeout=timeout)
            if response.status_code == 401:
                access_token = Authentication.request_device_code()
                headers["Authorization"] = "Bearer " + access_token
                response = requests.request(method, url, json=data, headers=headers, timeout=timeout)
            if response.status_code == 204:
                raise RequestException("API is not available")
            # status code >= 400
            response.raise_for_status()
            return json.loads(response.content)
        except Timeout as e:
            raise RequestException("API is not available") from e

    @classmethod
    def from_file(cls, name: str, realm_id: str = None, query_id: str = None, query_name : str = None):
        if not name.endswith(".sql"):
            name = name + ".sql"
        with open(name, "r") as fp:
            txt = "".join(fp.readlines())
        return cls.from_sql(sql=txt, realm_id=realm_id, query_id=query_id, query_name=query_name)

    @classmethod
    def from_sql(cls, sql: str, realm_id: str = None, query_id: str = None, query_name : str = None):
        json_data = cls.make_api_request(
            method="POST",
            headers={"User-Agent": "python/flowhigh-1.0.11", "Content-type": "application/json"},
            url="https://flowhigh.io/api/process",
            data={"sql": sql,
                  "realmID": realm_id,
                  "queryID": query_id,
                  "queryName": urllib.parse.quote(query_name, safe='') if query_name else None,
                  "json": True, "xml": True}
        )
        return cls(response=json_data)

    @classmethod
    def get_realm_queries(cls, realm_id: str):
        return cls.make_api_request(
            method="POST",
            headers={"User-Agent": "python/flowhigh-1.0.11"},
            url="https://flowhigh.io/api/realm?realmID=" + realm_id
        )

    def get_statements(self):
        return self._parsed_tree.statement

    @classmethod
    def get_main_dataset(cls, statement: Statement):
        return next(filter(lambda ds: ds.type_ == "root", statement.ds))

    def get_input(self, statement: Statement):
        return self.get_main_dataset(statement).in_

    def get_antipattern_of_statement(self, statement: Statement):
        """
        Returns the Anti-patterns for a statement
        :param statement: The Statement object whose Anti-patterns needs to be returned
        :return: Anti-patterns of the Statement object
        """
        return statement.antiPatterns

    def get_all_antipatterns(self):
        """
        Returns Anti-Patterns of all the statements
        :return: List of Anti-patterns of all the statements
        """
        antipatterns: list = []
        statements = self.get_statements()
        for statement in statements:
            antipatterns.extend(statement.antiPatterns)

        return antipatterns

    @classmethod
    def get_nodes_by_types(cls, types: Union[str, Tuple]):
        """
        Get the list of nodes in tree of a given type
        :param types: the type or the tuple of types
        :return: list of nodes that match the given types
        """
        return list(filter(lambda x: isinstance(x, types), RegistryBase.get_registry()))

    @classmethod
    def get_raw_query(cls, statement: Statement):
        """
        Get the raw query text
        :param statement:
        :return: the sql input
        """
        return statement.rawInput

    @classmethod
    def get_node_raw_text(cls, node):
        """
        Get the sql text at the node's coordinates in query
        :param node:
        :return: the sql at the node's coordinates
        """
        raw = ''
        if getattr(node, 'pos', None):
            stat = cls.find_ancestor_of_type(node, Statement)
            source_lower_bound, length = node.pos.split('-')  # NOQA
            raw = cls.get_raw_query(stat)[int(source_lower_bound): int(source_lower_bound) + int(length)]
        return " ".join(raw.split())

    @classmethod
    def search_node_by_id(cls, node_id: int):
        """
        Find a node in the tree based on its id
        :param node_id:
        :return: a node with the given id or None
        """
        return RegistryBase.search(node_id)

    @classmethod
    def search_node_by_pos(cls, pos: str):
        """
        Find a node based on its position in query
        :param pos:
        :return: the node at the given coordinates or None
        """
        return next(filter(lambda x: getattr(x, 'pos', None) and x.pos == pos, RegistryBase.get_registry()), None)

    @classmethod
    def search_origin_reference(cls, sref: str):
        """
        Find a node based on its origin reference
        :param sref: the coordinates of the referenced node
        :return: the node at the given coordinates or None
        """
        return cls.search_node_by_pos(sref)

    @classmethod
    def get_out_columns(cls, statement):
        """
        Get the set of columns returned by the input query
        :param statement:
        :return: the set of columns returned by the input query
        """
        out = cls.get_main_dataset(statement).out
        return out.exprs

    def get_DBO_hierarchy(self):
        """
        Get the DBO hierarchy
        :return: the hierarchy with all the DBOs
        """
        return self._parsed_tree.DBOHier_.dbo

    def get_tables(self):
        """
        Returns the list of table used in query
        :return: the set of tables used by the input query
        """
        return [dbo for dbo in self.get_DBO_hierarchy() if dbo.type_ == "TABLE"]

    def get_table_columns(self, table: DBO):
        """
        Returns the list of given table's columns
        :param table: the DBO representing the physical table
        :return: its set of columns
        """
        return table.dbo

    def get_where_cols(self, statement: Statement):
        """
        List the attributes used in filters
        :param statement: The input statement object with the submitted SQL
        :return the Set of attributes
        """
        def _get_where_cols(node: TreeNode, accum: set):
            if not node:
                return
            if isinstance(node, Ds) and node.modifiers:
                cols = [self.find_descendants_of_type(f.op, (Attr,)) for f in node.modifiers
                        if isinstance(f, Filter) and f.type_ == 'filtreg']
                accum.update(*cols)
            for child in node.get_children():
                _get_where_cols(child, accum)

        l = set()
        _get_where_cols(statement, l)
        return set(map(lambda attr: self.get_object_from_dbohier(attr.oref), l))

    def get_having_cols(self, statement: Statement):
        """
        List the attributes used in HAVING clause
        :param statement: The input statement object with the submitted SQL
        :return: the Set of attributes
        """
        def _get_having_cols(node: TreeNode, accum: set):
            if not node:
                return
            if isinstance(node, Ds) and node.modifiers:
                exprs = [f.op for f in node.modifiers if isinstance(f, Filter) and f.type_ == 'filtagg']
                for e in exprs:
                    for attr in self.find_descendants_of_type(e, (Attr,)):
                        # e.g. select department_id, count(department_id) x
                        # from employees group by department_id having x < 10;
                        if attr.sref:
                            exprs.append(self.search_origin_reference(attr.sref))
                            continue
                        accum.add(self.get_object_from_dbohier(attr.oref))
            for child in node.get_children():
                _get_having_cols(child, accum)

        l = set()
        _get_having_cols(statement, l)
        return l

    def get_groupby_cols(self, statement: Statement):
        """
        List the attributes used in GROUP BY
        :param statement: The input statement object with the submitted SQL
        :return: the Set of attributes
        """
        def _get_groupby_cols(node: TreeNode, accum: set):
            if not node:
                return
            if isinstance(node, Agg):
                out_ds: Out = self.find_ancestor_of_type(node, (Ds,)).out
                exprs = node.exprs
                for e in exprs:
                    for attr in self.find_descendants_of_type(e, (Attr,)):
                        if attr.refoutidx:
                            exprs.append(out_ds.exprs[int(attr.refoutidx) - 1])
                            continue
                        if attr.sref:
                            exprs.append(self.search_origin_reference(attr.sref))
                            continue
                        oref = self.get_object_from_dbohier(attr.oref)
                        accum.add(oref) if oref else None
            for child in node.get_children():
                _get_groupby_cols(child, accum)

        l = set()
        _get_groupby_cols(statement, l)
        return l

    def get_orderby_cols(self, statement: Statement):
        """
        List the attributes used in ORDER BY
        :param statement: The input statement object with the submitted SQL
        :return: the Set of attributes
        """
        def _get_sort_cols(node: TreeNode, accum: set):
            if not node:
                return
            if isinstance(node, Sort):
                out_ds: Out = self.find_ancestor_of_type(node, (Ds,)).out
                exprs = node.exprs
                for e in exprs:
                    for attr in self.find_descendants_of_type(e, (Attr,)):
                        if attr.refoutidx:
                            exprs.append(out_ds.exprs[int(attr.refoutidx) - 1])
                            continue
                        if attr.sref:
                            exprs.append(self.search_origin_reference(attr.sref))
                            continue
                        oref = self.get_object_from_dbohier(attr.oref)
                        accum.add(oref) if oref else None
            for child in node.get_children():
                _get_sort_cols(child, accum)

        l = set()
        _get_sort_cols(statement, l)
        return l

    def get_object_from_dbohier(self, oref: str):
        """
        Look up the DBO element in the hierarchy based on the oid
        :param oref: DBO reference
        :return: the DBO matching the oref if any
        """
        def _get_obj_from_dbohier(dbo: DBO):
            if not dbo:
                return
            if dbo.oid == oref:
                return dbo
            for child in dbo.dbo:
                res = _get_obj_from_dbohier(child)
                if res:
                    return res

        for d in self.get_DBO_hierarchy():
            match = _get_obj_from_dbohier(d)
            if match:
                return match

    @classmethod
    def get_DBO_fullref(cls, dbo: DBO):
        """
        Return the DBO's fully qualified name
        :param dbo: the DBO object whose name needs to be calculated
        :return: the DBO's fully qualified name
        """
        if not dbo:
            return
        parent = dbo.get_parent()
        if parent and isinstance(parent, DBOHier):
            return dbo.name
        if parent and isinstance(dbo, DBO):
            return ".".join(filter(None, (cls.get_DBO_fullref(parent), dbo.name.casefold())))

    @classmethod
    def find_ancestor_of_type(cls, node: TreeNode, clazz: Union[TreeNode, Tuple]):
        """
        Find the node's immediate ancestor by its type
        :param node: the node whose ancestor needs to be returned
        :param clazz: the type to match
        :return: the node's ancestor or None
        """
        if node.get_parent() is None:
            return None
        parent_obj = node.get_parent()
        if isinstance(parent_obj, clazz):
            return parent_obj
        return cls.find_ancestor_of_type(parent_obj, clazz)

    @classmethod
    def find_descendants_of_type(cls, node: TreeNode, clazz: Union[TreeNode, Tuple], all=True):
        """
        Find the list of children based on their type
        :param node: the node whose ancestor needs to be returned
        :param clazz: the type to match
        :param all: if False, don't continue searching in sub-levels after a matching node is found. Collect all otherwise. Default: True
        :return: the set of descendants
        """
        def _find_descendants_of_type(source_obj, accum):
            if not source_obj:
                return
            if isinstance(source_obj, clazz):
                accum.add(source_obj)
                if not all:
                    return
            for child in source_obj.get_children():
                _find_descendants_of_type(child, accum)

        l = set()
        _find_descendants_of_type(node, l)
        return l

    
    def _convert_Cast(self, kwargs):
        obj = CastBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "dataType" in kwargs:
            obj.with_dataType(self._convert_node(kwargs["dataType"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "expr" in kwargs:
            obj.with_expr(self._convert_node(kwargs["expr"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_CreateStageStatement(self, kwargs):
        obj = CreateStageStatementBuilder()
        
        if "dialExt" in kwargs:
            obj.with_dialExt(self._convert_node(kwargs["dialExt"]))
        
        if "clusterTopologyHiID" in kwargs:
            obj.with_clusterTopologyHiID(self._convert_node(kwargs["clusterTopologyHiID"]))
        
        if "clusterTopologyLoID" in kwargs:
            obj.with_clusterTopologyLoID(self._convert_node(kwargs["clusterTopologyLoID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "clusterLogicalID" in kwargs:
            obj.with_clusterLogicalID(self._convert_node(kwargs["clusterLogicalID"]))
        
        if "antiPatterns" in kwargs:
            obj.with_antiPatterns([self._convert_node(f) for f in kwargs["antiPatterns"]])
        
        if "rawInput" in kwargs:
            obj.with_rawInput(self._convert_node(kwargs["rawInput"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "clusterRawID" in kwargs:
            obj.with_clusterRawID(self._convert_node(kwargs["clusterRawID"]))
        
        if "ds" in kwargs:
            obj.with_ds([self._convert_node(f) for f in kwargs["ds"]])
        return obj.build()
    
    def _convert_Op(self, kwargs):
        obj = OpBuilder()
        
        if "nonANSI" in kwargs:
            obj.with_nonANSI(self._convert_node(kwargs["nonANSI"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "exprs" in kwargs:
            obj.with_exprs([self._convert_node(f) for f in kwargs["exprs"]])
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_Frame(self, kwargs):
        obj = FrameBuilder()
        
        if "low_val" in kwargs:
            obj.with_low_val(self._convert_node(kwargs["low_val"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "hi_rel" in kwargs:
            obj.with_hi_rel(self._convert_node(kwargs["hi_rel"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "exprs" in kwargs:
            obj.with_exprs([self._convert_node(f) for f in kwargs["exprs"]])
        
        if "low_rel" in kwargs:
            obj.with_low_rel(self._convert_node(kwargs["low_rel"]))
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        
        if "hi_val" in kwargs:
            obj.with_hi_val(self._convert_node(kwargs["hi_val"]))
        return obj.build()
    
    def _convert_AlterTableStatement(self, kwargs):
        obj = AlterTableStatementBuilder()
        
        if "dialExt" in kwargs:
            obj.with_dialExt(self._convert_node(kwargs["dialExt"]))
        
        if "clusterTopologyHiID" in kwargs:
            obj.with_clusterTopologyHiID(self._convert_node(kwargs["clusterTopologyHiID"]))
        
        if "clusterTopologyLoID" in kwargs:
            obj.with_clusterTopologyLoID(self._convert_node(kwargs["clusterTopologyLoID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "clusterLogicalID" in kwargs:
            obj.with_clusterLogicalID(self._convert_node(kwargs["clusterLogicalID"]))
        
        if "antiPatterns" in kwargs:
            obj.with_antiPatterns([self._convert_node(f) for f in kwargs["antiPatterns"]])
        
        if "rawInput" in kwargs:
            obj.with_rawInput(self._convert_node(kwargs["rawInput"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "clusterRawID" in kwargs:
            obj.with_clusterRawID(self._convert_node(kwargs["clusterRawID"]))
        
        if "ds" in kwargs:
            obj.with_ds([self._convert_node(f) for f in kwargs["ds"]])
        return obj.build()
    
    def _convert_Rotate(self, kwargs):
        obj = RotateBuilder()
        
        if "nameColumn" in kwargs:
            obj.with_nameColumn(self._convert_node(kwargs["nameColumn"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "valueColumn" in kwargs:
            obj.with_valueColumn(self._convert_node(kwargs["valueColumn"]))
        
        if "columnList" in kwargs:
            obj.with_columnList([self._convert_node(f) for f in kwargs["columnList"]])
        
        if "pivotColumn" in kwargs:
            obj.with_pivotColumn(self._convert_node(kwargs["pivotColumn"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "columnAlias" in kwargs:
            obj.with_columnAlias([self._convert_node(f) for f in kwargs["columnAlias"]])
        
        if "aggregate" in kwargs:
            obj.with_aggregate(self._convert_node(kwargs["aggregate"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_Func(self, kwargs):
        obj = FuncBuilder()
        
        if "partition" in kwargs:
            obj.with_partition([self._convert_node(f) for f in kwargs["partition"]])
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "withinGroup" in kwargs:
            obj.with_withinGroup(self._convert_node(kwargs["withinGroup"]))
        
        if "name" in kwargs:
            obj.with_name(self._convert_node(kwargs["name"]))
        
        if "exprs" in kwargs:
            obj.with_exprs([self._convert_node(f) for f in kwargs["exprs"]])
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "expr" in kwargs:
            obj.with_expr(self._convert_node(kwargs["expr"]))
        
        if "subType" in kwargs:
            obj.with_subType(kwargs["subType"])
        
        if "sort" in kwargs:
            obj.with_sort(self._convert_node(kwargs["sort"]))
        
        if "quantifier" in kwargs:
            obj.with_quantifier(kwargs["quantifier"])
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
        
        if "frame" in kwargs:
            obj.with_frame(self._convert_node(kwargs["frame"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_In(self, kwargs):
        obj = InBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "exprs" in kwargs:
            obj.with_exprs([self._convert_node(f) for f in kwargs["exprs"]])
        return obj.build()
    
    def _convert_Page(self, kwargs):
        obj = PageBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
        
        if "value" in kwargs:
            obj.with_value(self._convert_node(kwargs["value"]))
        return obj.build()
    
    def _convert_DeleteStatement(self, kwargs):
        obj = DeleteStatementBuilder()
        
        if "clusterTopologyHiID" in kwargs:
            obj.with_clusterTopologyHiID(self._convert_node(kwargs["clusterTopologyHiID"]))
        
        if "clusterTopologyLoID" in kwargs:
            obj.with_clusterTopologyLoID(self._convert_node(kwargs["clusterTopologyLoID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "clusterLogicalID" in kwargs:
            obj.with_clusterLogicalID(self._convert_node(kwargs["clusterLogicalID"]))
        
        if "antiPatterns" in kwargs:
            obj.with_antiPatterns([self._convert_node(f) for f in kwargs["antiPatterns"]])
        
        if "rawInput" in kwargs:
            obj.with_rawInput(self._convert_node(kwargs["rawInput"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "clusterRawID" in kwargs:
            obj.with_clusterRawID(self._convert_node(kwargs["clusterRawID"]))
        
        if "ds" in kwargs:
            obj.with_ds([self._convert_node(f) for f in kwargs["ds"]])
        return obj.build()
    
    def _convert_Attr(self, kwargs):
        obj = AttrBuilder()
        
        if "oref" in kwargs:
            obj.with_oref(self._convert_node(kwargs["oref"]))
        
        if "refsch" in kwargs:
            obj.with_refsch(self._convert_node(kwargs["refsch"]))
        
        if "fullref" in kwargs:
            obj.with_fullref(self._convert_node(kwargs["fullref"]))
        
        if "refvar" in kwargs:
            obj.with_refvar(self._convert_node(kwargs["refvar"]))
        
        if "refdb" in kwargs:
            obj.with_refdb(self._convert_node(kwargs["refdb"]))
        
        if "sref" in kwargs:
            obj.with_sref(self._convert_node(kwargs["sref"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "refds" in kwargs:
            obj.with_refds(self._convert_node(kwargs["refds"]))
        
        if "refatt" in kwargs:
            obj.with_refatt(self._convert_node(kwargs["refatt"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "refoutidx" in kwargs:
            obj.with_refoutidx(self._convert_node(kwargs["refoutidx"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_InsertStatement(self, kwargs):
        obj = InsertStatementBuilder()
        
        if "dialExt" in kwargs:
            obj.with_dialExt(self._convert_node(kwargs["dialExt"]))
        
        if "clusterTopologyHiID" in kwargs:
            obj.with_clusterTopologyHiID(self._convert_node(kwargs["clusterTopologyHiID"]))
        
        if "clusterTopologyLoID" in kwargs:
            obj.with_clusterTopologyLoID(self._convert_node(kwargs["clusterTopologyLoID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "clusterLogicalID" in kwargs:
            obj.with_clusterLogicalID(self._convert_node(kwargs["clusterLogicalID"]))
        
        if "antiPatterns" in kwargs:
            obj.with_antiPatterns([self._convert_node(f) for f in kwargs["antiPatterns"]])
        
        if "rawInput" in kwargs:
            obj.with_rawInput(self._convert_node(kwargs["rawInput"]))
        
        if "subType" in kwargs:
            obj.with_subType(self._convert_node(kwargs["subType"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "clusterRawID" in kwargs:
            obj.with_clusterRawID(self._convert_node(kwargs["clusterRawID"]))
        
        if "ds" in kwargs:
            obj.with_ds([self._convert_node(f) for f in kwargs["ds"]])
        return obj.build()
    
    def _convert_Case(self, kwargs):
        obj = CaseBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "Else" in kwargs:
            obj.with_Else(self._convert_node(kwargs["Else"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "expr" in kwargs:
            obj.with_expr(self._convert_node(kwargs["expr"]))
        
        if "when" in kwargs:
            obj.with_when([self._convert_node(f) for f in kwargs["when"]])
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_DBO(self, kwargs):
        obj = DBOBuilder()
        
        if "dbo" in kwargs:
            obj.with_dbo([self._convert_node(f) for f in kwargs["dbo"]])
        
        if "name" in kwargs:
            obj.with_name(self._convert_node(kwargs["name"]))
        
        if "index" in kwargs:
            obj.with_index(self._convert_node(kwargs["index"]))
        
        if "dtype" in kwargs:
            obj.with_dtype(self._convert_node(kwargs["dtype"]))
        
        if "constraint" in kwargs:
            obj.with_constraint(self._convert_node(kwargs["constraint"]))
        
        if "oid" in kwargs:
            obj.with_oid(self._convert_node(kwargs["oid"]))
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
        return obj.build()
    
    def _convert_StructRef(self, kwargs):
        obj = StructRefBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "refpath" in kwargs:
            obj.with_refpath(self._convert_node(kwargs["refpath"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "expr" in kwargs:
            obj.with_expr(self._convert_node(kwargs["expr"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_AntiPatterns(self, kwargs):
        obj = AntiPatternsBuilder()
        
        if "antiPattern" in kwargs:
            obj.with_antiPattern([self._convert_node(f) for f in kwargs["antiPattern"]])
        return obj.build()
    
    def _convert_Sort(self, kwargs):
        obj = SortBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "exprs" in kwargs:
            obj.with_exprs([self._convert_node(f) for f in kwargs["exprs"]])
        return obj.build()
    
    def _convert_Then(self, kwargs):
        obj = ThenBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "expr" in kwargs:
            obj.with_expr(self._convert_node(kwargs["expr"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_DBOHier(self, kwargs):
        obj = DBOHierBuilder()
        
        if "dbo" in kwargs:
            obj.with_dbo([self._convert_node(f) for f in kwargs["dbo"]])
        return obj.build()
    
    def _convert_MatchRecognize(self, kwargs):
        obj = MatchRecognizeBuilder()
        
        if "partitionBy" in kwargs:
            obj.with_partitionBy(self._convert_node(kwargs["partitionBy"]))
        
        if "measures" in kwargs:
            obj.with_measures(self._convert_node(kwargs["measures"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "define" in kwargs:
            obj.with_define(self._convert_node(kwargs["define"]))
        
        if "pattern" in kwargs:
            obj.with_pattern(self._convert_node(kwargs["pattern"]))
        
        if "rowMatchAction" in kwargs:
            obj.with_rowMatchAction(self._convert_node(kwargs["rowMatchAction"]))
        
        if "orderBy" in kwargs:
            obj.with_orderBy(self._convert_node(kwargs["orderBy"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "rowMatchCondition" in kwargs:
            obj.with_rowMatchCondition(self._convert_node(kwargs["rowMatchCondition"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_Asterisk(self, kwargs):
        obj = AsteriskBuilder()
        
        if "refsch" in kwargs:
            obj.with_refsch(self._convert_node(kwargs["refsch"]))
        
        if "fullref" in kwargs:
            obj.with_fullref(self._convert_node(kwargs["fullref"]))
        
        if "refdb" in kwargs:
            obj.with_refdb(self._convert_node(kwargs["refdb"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "refds" in kwargs:
            obj.with_refds(self._convert_node(kwargs["refds"]))
        
        if "refatt" in kwargs:
            obj.with_refatt(self._convert_node(kwargs["refatt"]))
        
        if "exprs" in kwargs:
            obj.with_exprs([self._convert_node(f) for f in kwargs["exprs"]])
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_MergeStatement(self, kwargs):
        obj = MergeStatementBuilder()
        
        if "clusterTopologyHiID" in kwargs:
            obj.with_clusterTopologyHiID(self._convert_node(kwargs["clusterTopologyHiID"]))
        
        if "clusterTopologyLoID" in kwargs:
            obj.with_clusterTopologyLoID(self._convert_node(kwargs["clusterTopologyLoID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "clusterLogicalID" in kwargs:
            obj.with_clusterLogicalID(self._convert_node(kwargs["clusterLogicalID"]))
        
        if "antiPatterns" in kwargs:
            obj.with_antiPatterns([self._convert_node(f) for f in kwargs["antiPatterns"]])
        
        if "rawInput" in kwargs:
            obj.with_rawInput(self._convert_node(kwargs["rawInput"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "clusterRawID" in kwargs:
            obj.with_clusterRawID(self._convert_node(kwargs["clusterRawID"]))
        
        if "ds" in kwargs:
            obj.with_ds([self._convert_node(f) for f in kwargs["ds"]])
        return obj.build()
    
    def _convert_Agg(self, kwargs):
        obj = AggBuilder()
        
        if "filter" in kwargs:
            obj.with_filter([self._convert_node(f) for f in kwargs["filter"]])
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "exprs" in kwargs:
            obj.with_exprs([self._convert_node(f) for f in kwargs["exprs"]])
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
        return obj.build()
    
    def _convert_AntiPattern(self, kwargs):
        obj = AntiPatternBuilder()
        
        if "severity" in kwargs:
            obj.with_severity(self._convert_node(kwargs["severity"]))
        
        if "readability" in kwargs:
            obj.with_readability(self._convert_node(kwargs["readability"]))
        
        if "correctness" in kwargs:
            obj.with_correctness(self._convert_node(kwargs["correctness"]))
        
        if "performance" in kwargs:
            obj.with_performance(self._convert_node(kwargs["performance"]))
        
        if "pos" in kwargs:
            obj.with_pos([self._convert_node(f) for f in kwargs["pos"]])
        
        if "link" in kwargs:
            obj.with_link(self._convert_node(kwargs["link"]))
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
            obj.with_link(kwargs["type"])
            obj.with_severity(kwargs["type"])
            obj.with_readability(kwargs["type"])
            obj.with_correctness(kwargs["type"])
            obj.with_performance(kwargs["type"])
            obj.with_name(kwargs["type"])
        return obj.build()
    
    def _convert_UpdateStatement(self, kwargs):
        obj = UpdateStatementBuilder()
        
        if "clusterTopologyHiID" in kwargs:
            obj.with_clusterTopologyHiID(self._convert_node(kwargs["clusterTopologyHiID"]))
        
        if "clusterTopologyLoID" in kwargs:
            obj.with_clusterTopologyLoID(self._convert_node(kwargs["clusterTopologyLoID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "clusterLogicalID" in kwargs:
            obj.with_clusterLogicalID(self._convert_node(kwargs["clusterLogicalID"]))
        
        if "antiPatterns" in kwargs:
            obj.with_antiPatterns([self._convert_node(f) for f in kwargs["antiPatterns"]])
        
        if "rawInput" in kwargs:
            obj.with_rawInput(self._convert_node(kwargs["rawInput"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "clusterRawID" in kwargs:
            obj.with_clusterRawID(self._convert_node(kwargs["clusterRawID"]))
        
        if "ds" in kwargs:
            obj.with_ds([self._convert_node(f) for f in kwargs["ds"]])
        return obj.build()
    
    def _convert_CreateViewStatement(self, kwargs):
        obj = CreateViewStatementBuilder()
        
        if "dialExt" in kwargs:
            obj.with_dialExt(self._convert_node(kwargs["dialExt"]))
        
        if "clusterTopologyHiID" in kwargs:
            obj.with_clusterTopologyHiID(self._convert_node(kwargs["clusterTopologyHiID"]))
        
        if "clusterTopologyLoID" in kwargs:
            obj.with_clusterTopologyLoID(self._convert_node(kwargs["clusterTopologyLoID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "clusterLogicalID" in kwargs:
            obj.with_clusterLogicalID(self._convert_node(kwargs["clusterLogicalID"]))
        
        if "antiPatterns" in kwargs:
            obj.with_antiPatterns([self._convert_node(f) for f in kwargs["antiPatterns"]])
        
        if "rawInput" in kwargs:
            obj.with_rawInput(self._convert_node(kwargs["rawInput"]))
        
        if "subType" in kwargs:
            obj.with_subType(self._convert_node(kwargs["subType"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "clusterRawID" in kwargs:
            obj.with_clusterRawID(self._convert_node(kwargs["clusterRawID"]))
        
        if "ds" in kwargs:
            obj.with_ds([self._convert_node(f) for f in kwargs["ds"]])
        return obj.build()
    
    def _convert_QueryingStage(self, kwargs):
        obj = QueryingStageBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "pattern" in kwargs:
            obj.with_pattern(self._convert_node(kwargs["pattern"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "location" in kwargs:
            obj.with_location(self._convert_node(kwargs["location"]))
        
        if "fileFormat" in kwargs:
            obj.with_fileFormat(kwargs["fileFormat"])
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_CopyStatement(self, kwargs):
        obj = CopyStatementBuilder()
        
        if "dialExt" in kwargs:
            obj.with_dialExt(self._convert_node(kwargs["dialExt"]))
        
        if "clusterTopologyHiID" in kwargs:
            obj.with_clusterTopologyHiID(self._convert_node(kwargs["clusterTopologyHiID"]))
        
        if "clusterTopologyLoID" in kwargs:
            obj.with_clusterTopologyLoID(self._convert_node(kwargs["clusterTopologyLoID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "clusterLogicalID" in kwargs:
            obj.with_clusterLogicalID(self._convert_node(kwargs["clusterLogicalID"]))
        
        if "antiPatterns" in kwargs:
            obj.with_antiPatterns([self._convert_node(f) for f in kwargs["antiPatterns"]])
        
        if "rawInput" in kwargs:
            obj.with_rawInput(self._convert_node(kwargs["rawInput"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "clusterRawID" in kwargs:
            obj.with_clusterRawID(self._convert_node(kwargs["clusterRawID"]))
        
        if "ds" in kwargs:
            obj.with_ds([self._convert_node(f) for f in kwargs["ds"]])
        return obj.build()
    
    def _convert_Position(self, kwargs):
        obj = PositionBuilder()
        
        if "string" in kwargs:
            obj.with_string(self._convert_node(kwargs["string"]))
        
        if "subString" in kwargs:
            obj.with_subString(self._convert_node(kwargs["subString"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_Statement(self, kwargs):
        obj = StatementBuilder()
        
        if "clusterTopologyLoID" in kwargs:
            obj.with_clusterTopologyLoID(self._convert_node(kwargs["clusterTopologyLoID"]))
        
        if "clusterTopologyHiID" in kwargs:
            obj.with_clusterTopologyHiID(self._convert_node(kwargs["clusterTopologyHiID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "rawInput" in kwargs:
            obj.with_rawInput(self._convert_node(kwargs["rawInput"]))
        
        if "antiPatterns" in kwargs:
            obj.with_antiPatterns([self._convert_node(f) for f in kwargs["antiPatterns"]])
        
        if "clusterLogicalID" in kwargs:
            obj.with_clusterLogicalID(self._convert_node(kwargs["clusterLogicalID"]))
        
        if "clusterRawID" in kwargs:
            obj.with_clusterRawID(self._convert_node(kwargs["clusterRawID"]))
        
        if "ds" in kwargs:
            obj.with_ds([self._convert_node(f) for f in kwargs["ds"]])
        return obj.build()
    
    def _convert_Const(self, kwargs):
        obj = ConstBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "value" in kwargs:
            obj.with_value(kwargs["value"])
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_CreateTableStatement(self, kwargs):
        obj = CreateTableStatementBuilder()
        
        if "dialExt" in kwargs:
            obj.with_dialExt(self._convert_node(kwargs["dialExt"]))
        
        if "clusterTopologyHiID" in kwargs:
            obj.with_clusterTopologyHiID(self._convert_node(kwargs["clusterTopologyHiID"]))
        
        if "clusterTopologyLoID" in kwargs:
            obj.with_clusterTopologyLoID(self._convert_node(kwargs["clusterTopologyLoID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "clusterLogicalID" in kwargs:
            obj.with_clusterLogicalID(self._convert_node(kwargs["clusterLogicalID"]))
        
        if "antiPatterns" in kwargs:
            obj.with_antiPatterns([self._convert_node(f) for f in kwargs["antiPatterns"]])
        
        if "rawInput" in kwargs:
            obj.with_rawInput(self._convert_node(kwargs["rawInput"]))
        
        if "subType" in kwargs:
            obj.with_subType(self._convert_node(kwargs["subType"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "clusterRawID" in kwargs:
            obj.with_clusterRawID(self._convert_node(kwargs["clusterRawID"]))
        
        if "ds" in kwargs:
            obj.with_ds([self._convert_node(f) for f in kwargs["ds"]])
        return obj.build()
    
    def _convert_ParSeQL(self, kwargs):
        obj = ParSeQLBuilder()
        
        if "realmID" in kwargs:
            obj.with_realmID(self._convert_node(kwargs["realmID"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "statement" in kwargs:
            obj.with_statement([self._convert_node(f) for f in kwargs["statement"]])
        
        if "namespace" in kwargs:
            obj.with_namespace(self._convert_node(kwargs["namespace"]))
        
        if "location" in kwargs:
            obj.with_location(self._convert_node(kwargs["location"]))
        
        if "DBOHier" in kwargs:
            obj.with_DBOHier(self._convert_node(kwargs["DBOHier"]))
        
        if "error" in kwargs:
            obj.with_error([self._convert_node(f) for f in kwargs["error"]])
        
        if "version" in kwargs:
            obj.with_version(self._convert_node(kwargs["version"]))
        
        if "ts" in kwargs:
            obj.with_ts(self._convert_node(kwargs["ts"]))
        
        if "status" in kwargs:
            obj.with_status(kwargs["status"])
        return obj.build()
    
    def _convert_Join(self, kwargs):
        obj = JoinBuilder()
        
        if "op" in kwargs:
            obj.with_op(self._convert_node(kwargs["op"]))
        
        if "definedAs" in kwargs:
            obj.with_definedAs(kwargs["definedAs"])
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "subType" in kwargs:
            obj.with_subType(kwargs["subType"])
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
        
        if "ds" in kwargs:
            obj.with_ds(self._convert_node(kwargs["ds"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_TableSample(self, kwargs):
        obj = TableSampleBuilder()
        
        if "sampleMethod" in kwargs:
            obj.with_sampleMethod(self._convert_node(kwargs["sampleMethod"]))
        
        if "seed" in kwargs:
            obj.with_seed(self._convert_node(kwargs["seed"]))
        
        if "seedType" in kwargs:
            obj.with_seedType(self._convert_node(kwargs["seedType"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "probability" in kwargs:
            obj.with_probability(self._convert_node(kwargs["probability"]))
        
        if "num" in kwargs:
            obj.with_num(self._convert_node(kwargs["num"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "sampleType" in kwargs:
            obj.with_sampleType(self._convert_node(kwargs["sampleType"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_WrappedExpr(self, kwargs):
        obj = WrappedExprBuilder()
        
        if "expr" in kwargs:
            obj.with_expr(self._convert_node(kwargs["expr"]))
        return obj.build()
    
    def _convert_Ds(self, kwargs):
        obj = DsBuilder()
        
        if "refsch" in kwargs:
            obj.with_refsch(self._convert_node(kwargs["refsch"]))
        
        if "fullref" in kwargs:
            obj.with_fullref(self._convert_node(kwargs["fullref"]))
        
        if "refdb" in kwargs:
            obj.with_refdb(self._convert_node(kwargs["refdb"]))
        
        if "in" in kwargs:
            obj.with_in(self._convert_node(kwargs["in"]))
        
        if "matchRecognize" in kwargs:
            obj.with_matchRecognize(self._convert_node(kwargs["matchRecognize"]))
        
        if "setOp" in kwargs:
            obj.with_setOp([self._convert_node(f) for f in kwargs["setOp"]])
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
        
        if "modifiers" in kwargs:
            obj.with_modifiers([self._convert_node(f) for f in kwargs["modifiers"]])
        
        if "out" in kwargs:
            obj.with_out(self._convert_node(kwargs["out"]))
        
        if "oref" in kwargs:
            obj.with_oref(self._convert_node(kwargs["oref"]))
        
        if "tableSample" in kwargs:
            obj.with_tableSample(self._convert_node(kwargs["tableSample"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "sref" in kwargs:
            obj.with_sref(self._convert_node(kwargs["sref"]))
        
        if "refds" in kwargs:
            obj.with_refds(self._convert_node(kwargs["refds"]))
        
        if "name" in kwargs:
            obj.with_name(self._convert_node(kwargs["name"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "action" in kwargs:
            obj.with_action(kwargs["action"])
        
        if "subType" in kwargs:
            obj.with_subType(kwargs["subType"])
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_Out(self, kwargs):
        obj = OutBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "exprs" in kwargs:
            obj.with_exprs([self._convert_node(f) for f in kwargs["exprs"]])
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        return obj.build()
    
    def _convert_Array(self, kwargs):
        obj = ArrayBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "items" in kwargs:
            obj.with_items([self._convert_node(f) for f in kwargs["items"]])
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_When(self, kwargs):
        obj = WhenBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "expr" in kwargs:
            obj.with_expr(self._convert_node(kwargs["expr"]))
        
        if "then" in kwargs:
            obj.with_then(self._convert_node(kwargs["then"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_Filter(self, kwargs):
        obj = FilterBuilder()
        
        if "op" in kwargs:
            obj.with_op(self._convert_node(kwargs["op"]))
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
        return obj.build()
    
    def _convert_TableFunc(self, kwargs):
        obj = TableFuncBuilder()
        
        if "type" in kwargs:
            obj.with_type(kwargs["type"])
        
        if "modifiers" in kwargs:
            obj.with_modifiers([self._convert_node(f) for f in kwargs["modifiers"]])
        
        if "out" in kwargs:
            obj.with_out(self._convert_node(kwargs["out"]))
        
        if "partition" in kwargs:
            obj.with_partition([self._convert_node(f) for f in kwargs["partition"]])
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "refds" in kwargs:
            obj.with_refds(self._convert_node(kwargs["refds"]))
        
        if "options" in kwargs:
            obj.with_options([self._convert_node(f) for f in kwargs["options"]])
        
        if "action" in kwargs:
            obj.with_action(kwargs["action"])
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "tableFuncType" in kwargs:
            obj.with_tableFuncType(self._convert_node(kwargs["tableFuncType"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        
        if "refsch" in kwargs:
            obj.with_refsch(self._convert_node(kwargs["refsch"]))
        
        if "fullref" in kwargs:
            obj.with_fullref(self._convert_node(kwargs["fullref"]))
        
        if "refdb" in kwargs:
            obj.with_refdb(self._convert_node(kwargs["refdb"]))
        
        if "in" in kwargs:
            obj.with_in(self._convert_node(kwargs["in"]))
        
        if "matchRecognize" in kwargs:
            obj.with_matchRecognize(self._convert_node(kwargs["matchRecognize"]))
        
        if "setOp" in kwargs:
            obj.with_setOp([self._convert_node(f) for f in kwargs["setOp"]])
        
        if "sort" in kwargs:
            obj.with_sort(self._convert_node(kwargs["sort"]))
        
        if "subQuery" in kwargs:
            obj.with_subQuery(self._convert_node(kwargs["subQuery"]))
        
        if "oref" in kwargs:
            obj.with_oref(self._convert_node(kwargs["oref"]))
        
        if "tableSample" in kwargs:
            obj.with_tableSample(self._convert_node(kwargs["tableSample"]))
        
        if "names" in kwargs:
            obj.with_names([self._convert_node(f) for f in kwargs["names"]])
        
        if "sref" in kwargs:
            obj.with_sref(self._convert_node(kwargs["sref"]))
        
        if "name" in kwargs:
            obj.with_name(self._convert_node(kwargs["name"]))
        
        if "unnestExpressions" in kwargs:
            obj.with_unnestExpressions([self._convert_node(f) for f in kwargs["unnestExpressions"]])
        
        if "subType" in kwargs:
            obj.with_subType(kwargs["subType"])
        
        if "frame" in kwargs:
            obj.with_frame(self._convert_node(kwargs["frame"]))
        return obj.build()
    
    def _convert_Else(self, kwargs):
        obj = ElseBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "expr" in kwargs:
            obj.with_expr(self._convert_node(kwargs["expr"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_Row(self, kwargs):
        obj = RowBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "exprs" in kwargs:
            obj.with_exprs([self._convert_node(f) for f in kwargs["exprs"]])
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_Current(self, kwargs):
        obj = CurrentBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    
    def _convert_Edge(self, kwargs):
        obj = EdgeBuilder()
        
        if "pos" in kwargs:
            obj.with_pos(self._convert_node(kwargs["pos"]))
        
        if "exprs" in kwargs:
            obj.with_exprs([self._convert_node(f) for f in kwargs["exprs"]])
        
        if "generator" in kwargs:
            obj.with_generator(self._convert_node(kwargs["generator"]))
        
        if "alias" in kwargs:
            obj.with_alias(self._convert_node(kwargs["alias"]))
        
        if "type" in kwargs:
            obj.with_type(self._convert_node(kwargs["type"]))
        
        if "columnAlias" in kwargs:
            obj.with_columnAlias([self._convert_node(f) for f in kwargs["columnAlias"]])
        
        if "direction" in kwargs:
            obj.with_direction(kwargs["direction"])
        return obj.build()
    

    def _convert_node(self, kwargs):
        if not is_iterable(kwargs):
            return kwargs
        if "eltype" not in kwargs:
            return kwargs
        if kwargs["eltype"].lower() == "cast":
            return self._convert_Cast(kwargs)
        if kwargs["eltype"].lower() == "createstagestatement":
            return self._convert_CreateStageStatement(kwargs)
        if kwargs["eltype"].lower() == "op":
            return self._convert_Op(kwargs)
        if kwargs["eltype"].lower() == "frame":
            return self._convert_Frame(kwargs)
        if kwargs["eltype"].lower() == "altertablestatement":
            return self._convert_AlterTableStatement(kwargs)
        if kwargs["eltype"].lower() == "rotate":
            return self._convert_Rotate(kwargs)
        if kwargs["eltype"].lower() == "func":
            return self._convert_Func(kwargs)
        if kwargs["eltype"].lower() == "in":
            return self._convert_In(kwargs)
        if kwargs["eltype"].lower() == "page":
            return self._convert_Page(kwargs)
        if kwargs["eltype"].lower() == "deletestatement":
            return self._convert_DeleteStatement(kwargs)
        if kwargs["eltype"].lower() == "attr":
            return self._convert_Attr(kwargs)
        if kwargs["eltype"].lower() == "insertstatement":
            return self._convert_InsertStatement(kwargs)
        if kwargs["eltype"].lower() == "case":
            return self._convert_Case(kwargs)
        if kwargs["eltype"].lower() == "dbo":
            return self._convert_DBO(kwargs)
        if kwargs["eltype"].lower() == "structref":
            return self._convert_StructRef(kwargs)
        if kwargs["eltype"].lower() == "antipatterns":
            return self._convert_AntiPatterns(kwargs)
        if kwargs["eltype"].lower() == "sort":
            return self._convert_Sort(kwargs)
        if kwargs["eltype"].lower() == "then":
            return self._convert_Then(kwargs)
        if kwargs["eltype"].lower() == "dbohier":
            return self._convert_DBOHier(kwargs)
        if kwargs["eltype"].lower() == "matchrecognize":
            return self._convert_MatchRecognize(kwargs)
        if kwargs["eltype"].lower() == "asterisk":
            return self._convert_Asterisk(kwargs)
        if kwargs["eltype"].lower() == "mergestatement":
            return self._convert_MergeStatement(kwargs)
        if kwargs["eltype"].lower() == "agg":
            return self._convert_Agg(kwargs)
        if kwargs["eltype"].lower() == "antipattern":
            return self._convert_AntiPattern(kwargs)
        if kwargs["eltype"].lower() == "updatestatement":
            return self._convert_UpdateStatement(kwargs)
        if kwargs["eltype"].lower() == "createviewstatement":
            return self._convert_CreateViewStatement(kwargs)
        if kwargs["eltype"].lower() == "queryingstage":
            return self._convert_QueryingStage(kwargs)
        if kwargs["eltype"].lower() == "copystatement":
            return self._convert_CopyStatement(kwargs)
        if kwargs["eltype"].lower() == "position":
            return self._convert_Position(kwargs)
        if kwargs["eltype"].lower() == "statement":
            return self._convert_Statement(kwargs)
        if kwargs["eltype"].lower() == "const":
            return self._convert_Const(kwargs)
        if kwargs["eltype"].lower() == "createtablestatement":
            return self._convert_CreateTableStatement(kwargs)
        if kwargs["eltype"].lower() == "parseql":
            return self._convert_ParSeQL(kwargs)
        if kwargs["eltype"].lower() == "join":
            return self._convert_Join(kwargs)
        if kwargs["eltype"].lower() == "tablesample":
            return self._convert_TableSample(kwargs)
        if kwargs["eltype"].lower() == "wrappedexpr":
            return self._convert_WrappedExpr(kwargs)
        if kwargs["eltype"].lower() == "ds":
            return self._convert_Ds(kwargs)
        if kwargs["eltype"].lower() == "out":
            return self._convert_Out(kwargs)
        if kwargs["eltype"].lower() == "array":
            return self._convert_Array(kwargs)
        if kwargs["eltype"].lower() == "when":
            return self._convert_When(kwargs)
        if kwargs["eltype"].lower() == "filter":
            return self._convert_Filter(kwargs)
        if kwargs["eltype"].lower() == "tablefunc":
            return self._convert_TableFunc(kwargs)
        if kwargs["eltype"].lower() == "else":
            return self._convert_Else(kwargs)
        if kwargs["eltype"].lower() == "row":
            return self._convert_Row(kwargs)
        if kwargs["eltype"].lower() == "current":
            return self._convert_Current(kwargs)
        if kwargs["eltype"].lower() == "edge":
            return self._convert_Edge(kwargs)

def is_iterable(obj):
    try:
        it = iter(obj)
    except TypeError:
        return False
    return True
