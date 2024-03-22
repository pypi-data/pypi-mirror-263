# copyright 2004-2021 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of rql.
#
# rql is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# rql is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with rql. If not, see <http://www.gnu.org/licenses/>.
"""Manages undos on RQL syntax trees."""

from rql.nodes import Exists, VariableRef, BinaryNode
from rql.stmts import Select

from typing import (
    List,
    Any,
    Optional,
    TYPE_CHECKING,
    Union as Union_,
)

if TYPE_CHECKING:
    import rql

__docformat__: str = "restructuredtext en"

Op = Union_[
    "NodeOperation",
    "MakeVarOperation",
    "UndefineVarOperation",
    "SelectVarOperation",
    "UnselectVarOperation",
    "AddNodeOperation",
    "ReplaceNodeOperation",
    "RemoveNodeOperation",
    "AddSortOperation",
    "RemoveSortOperation",
    "AddGroupOperation",
    "RemoveGroupOperation",
    "SetDistinctOperation",
    "SetOffsetOperation",
    "SetLimitOperation",
    "SetOptionalOperation",
    "SetHavingOperation",
    "AppendSelectOperation",
    "RemoveSelectOperation",
]


class SelectionManager:
    """Manage the operation stacks."""

    def __init__(self, selection: Union_["rql.stmts.ScopeNode", "rql.stmts.Union"]):
        self._selection = selection  # The selection tree
        self.op_list: List[Op] = []  # The operations we'll have to undo
        self.state_stack: List[int] = []  # The save_state()'s index stack

    def push_state(self) -> None:
        """defines current state as the new 'start' state"""
        self.state_stack.append(len(self.op_list))

    def recover(self) -> None:
        """recover to the latest pushed state"""
        last_state_index: int = self.state_stack.pop()
        # if last_index == 0, then there's no intermediate state => undo all !
        for i in self.op_list[:-last_state_index] or self.op_list[:]:
            self.undo()

    def add_operation(self, operation: Op) -> None:
        """add an operation to the current ones"""
        # stores operations in reverse order :
        self.op_list.insert(0, operation)

    def undo(self) -> None:
        """undo the latest operation"""
        assert len(self.op_list) > 0
        op: Op = self.op_list.pop(0)
        # Item "ScopeNode" of "Union[ScopeNode, rql.stmts.Union]"
        # has no attribute "undoing"
        # ignoring for now. Maybe we can add the attribute with the classes
        self._selection.undoing = 1  # type:ignore[union-attr]
        op.undo(self._selection)
        self._selection.undoing = 0  # type:ignore[union-attr]

    def flush(self) -> None:
        """flush the current operations"""
        self.op_list = []


class NodeOperation:
    """Abstract class for node manipulation operations."""

    def __init__(
        self,
        node: Union_[
            "rql.nodes.ColumnAlias",
            "rql.nodes.Variable",
            "rql.nodes.VariableRef",
            "rql.nodes.Relation",
            "rql.nodes.SortTerm",
        ],
        stmt: Optional["rql.stmts.Statement"] = None,
    ):
        self.node = node
        if stmt is None:
            stmt = node.stmt
        self.stmt = stmt

    def __str__(self) -> str:
        """undo the operation on the selection"""
        return f"{self.__class__.__name__} {self.node}"

    # and define this as abstract method?
    def undo(self, selection: Any) -> None:
        raise NotImplementedError


# Undo for variable manipulation operations  ##################################


class MakeVarOperation(NodeOperation):
    """Defines how to undo make_variable()."""

    def undo(self, selection):
        """undo the operation on the selection"""
        self.stmt.undefine_variable(self.node)


class UndefineVarOperation(NodeOperation):
    """Defines how to undo undefine_variable()."""

    def __init__(self, node, stmt, solutions):
        NodeOperation.__init__(self, node, stmt)
        self.solutions = solutions

    def undo(self, selection):
        """undo the operation on the selection"""
        var = self.node
        self.stmt.defined_vars[var.name] = var
        self.stmt.solutions = self.solutions


class SelectVarOperation(NodeOperation):
    """Defines how to undo add_selected()."""

    def undo(self, selection):
        """undo the operation on the selection"""
        self.stmt.remove_selected(self.node)


class UnselectVarOperation(NodeOperation):
    """Defines how to undo unselect_var()."""

    def __init__(self, var, pos):
        NodeOperation.__init__(self, var)
        self.index = pos

    def undo(self, selection):
        """undo the operation on the selection"""
        self.stmt.add_selected(self.node, self.index)


# Undo for node operations ####################################################


class AddNodeOperation(NodeOperation):
    """Defines how to undo add_node()."""

    def undo(self, selection):
        """undo the operation on the selection"""
        self.stmt.remove_node(self.node)


class ReplaceNodeOperation:
    """Defines how to undo 'replace node'."""

    def __init__(self, old_node, new_node):
        self.old_node = old_node
        self.new_node = new_node

    def undo(self, selection):
        """undo the operation on the selection"""
        # unregister reference from the inserted node
        for varref in self.new_node.iget_nodes(VariableRef):
            varref.unregister_reference()
        # register reference from the removed node
        for varref in self.old_node.iget_nodes(VariableRef):
            varref.register_reference()
        self.new_node.parent.replace(self.new_node, self.old_node)

    def __str__(self):
        return f"ReplaceNodeOperation {self.old_node} by {self.new_node}"


class RemoveNodeOperation(NodeOperation):
    """Defines how to undo remove_node()."""

    def __init__(self, node, parent, stmt, index):
        NodeOperation.__init__(self, node, stmt)
        self.node_parent = parent
        if index is None:
            assert isinstance(parent, (Exists, Select)), (node, parent)
        self.index = index
        # XXX FIXME : find a better way to do that
        self.binary_remove = isinstance(node, BinaryNode)

    def undo(self, selection):
        """undo the operation on the selection"""
        parent = self.node_parent
        if self.index is None:
            if isinstance(parent, Select):
                parent.where = self.node
            else:  # Exists
                parent.query = self.node
            sibling = self.node
        if self.binary_remove:
            # if 'parent' was a BinaryNode, then first reinsert the removed node
            # at the same pos in the original 'parent' Binary Node, and then
            # reinsert this BinaryNode in its parent's children list
            # WARNING : the removed node sibling's parent is no longer the
            # 'node_parent'. We must Reparent it manually !
            if self.index is not None:
                sibling = self.node_parent.children[self.index]
                parent.children[self.index] = self.node
            sibling.parent = self.node
        elif self.index is not None:
            parent.insert(self.index, self.node)
        # register reference from the removed node
        self.node.parent = parent
        for varref in self.node.iget_nodes(VariableRef):
            varref.register_reference()


class AddSortOperation(NodeOperation):
    """Defines how to undo 'add sort'."""

    def undo(self, selection):
        """undo the operation on the selection"""
        self.stmt.remove_sort_term(self.node)


class RemoveSortOperation(NodeOperation):
    """Defines how to undo 'remove sort'."""

    def __init__(self, node):
        NodeOperation.__init__(self, node)
        self.index = self.stmt.orderby.index(self.node)

    def undo(self, selection):
        """undo the operation on the selection"""
        self.stmt.add_sort_term(self.node, self.index)


class AddGroupOperation(NodeOperation):
    """Defines how to undo 'add group'."""

    def undo(self, selection):
        """undo the operation on the selection"""
        self.stmt.remove_group_term(self.node)


class RemoveGroupOperation(NodeOperation):
    """Defines how to undo 'remove group'."""

    def __init__(self, node):
        NodeOperation.__init__(self, node)
        self.index = self.stmt.groupby.index(self.node)

    def undo(self, selection):
        """undo the operation on the selection"""
        self.stmt.add_group_var(self.node, self.index)


# misc operations #############################################################


class ChangeValueOperation:
    def __init__(self, previous_value, node=None):
        self.value = previous_value
        self.node = node


class SetDistinctOperation(ChangeValueOperation):
    """Defines how to undo 'set_distinct'."""

    def undo(self, selection):
        """undo the operation on the selection"""
        self.node.distinct = self.value


class SetOffsetOperation(ChangeValueOperation):
    """Defines how to undo 'set_offset'."""

    def undo(self, selection):
        """undo the operation on the selection"""
        self.node.offset = self.value


class SetLimitOperation(ChangeValueOperation):
    """Defines how to undo 'set_limit'."""

    def undo(self, selection):
        """undo the operation on the selection"""
        self.node.limit = self.value


class SetOptionalOperation(ChangeValueOperation):
    """Defines how to undo 'set_limit'."""

    def __init__(self, rel, previous_value):
        self.rel = rel
        self.value = previous_value

    def undo(self, selection):
        """undo the operation on the selection"""
        self.rel.optional = self.value


class SetHavingOperation:
    """Defines how to undo 'set_having'."""

    def __init__(self, select, previous_value):
        self.select = select
        self.value = previous_value

    def undo(self, selection):
        """undo the operation on the selection"""
        for term in self.select.having:
            # Unregister any VariableRef in the HAVING clause which would
            # otherwise be attempted to be undefined whereas they are not
            # actually defined.
            for varref in term.iget_nodes(VariableRef):
                varref.unregister_reference()
        self.select.having = self.value


# Union operations ############################################################


class AppendSelectOperation:
    """Defines how to undo append_select()."""

    def __init__(self, union, select):
        self.union = union
        self.select = select

    def undo(self, selection):
        """undo the operation on the union's children"""
        self.select.parent = self.union
        self.union.children.remove(self.select)


class RemoveSelectOperation(AppendSelectOperation):
    """Defines how to undo append_select()."""

    def __init__(self, union, select, origindex):
        AppendSelectOperation.__init__(self, union, select)
        self.origindex = origindex

    def undo(self, selection):
        """undo the operation on the union's children"""
        self.union.insert(self.origindex, self.select)


__all__ = (
    "SelectionManager",
    "MakeVarOperation",
    "UndefineVarOperation",
    "SelectVarOperation",
    "UnselectVarOperation",
    "AddNodeOperation",
    "ReplaceNodeOperation",
    "RemoveNodeOperation",
    "AddSortOperation",
    "AddGroupOperation",
    "SetOptionalOperation",
    "SetDistinctOperation",
)
