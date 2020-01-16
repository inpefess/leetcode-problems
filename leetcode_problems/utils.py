"""
    leetcode-problems is a collection of Python 3 solutions for problems
    from https://leetcode.com/
    Copyright (C) 2019-2020  Boris Shminke

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from typing import Optional


class ListNode:
    """ Definition for singly-linked list. """
    # pylint: disable=redefined-builtin
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        """

        :param val: integer value at a node
        :param next: link to the next node if any
        """
        self.val = val
        self.next = next

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return NotImplemented
        one: Optional["ListNode"] = self
        two: Optional["ListNode"] = other
        equal = True
        while one and two:
            if one.val == two.val:
                one = one.next
                two = two.next
            else:
                equal = False
                break
        return not (one or two) and equal

    def __repr__(self):
        node = self
        list_repr = list()
        while node:
            list_repr.append(node.val)
            node = node.next
        return str(list_repr if list_repr else [0])
