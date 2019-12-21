"""
    leetcode-problems is a collection of Python 3 solutions for problems
    from https://leetcode.com/
    Copyright (C) 2019  Boris Shminke

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


# pylint: disable=too-few-public-methods
class Solution:
    # pylint: disable=invalid-name, no-self-use
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        one: Optional["ListNode"] = l1
        two: Optional["ListNode"] = l2
        three: Optional["ListNode"] = None
        current_node = three
        carry = 0
        while one or two or carry:
            three_val = carry
            if one:
                three_val += one.val
                one = one.next
            if two:
                three_val += two.val
                two = two.next
            if three_val > 9:
                carry = 1
                three_val -= 10
            else:
                carry = 0
            next_node = ListNode(three_val)
            if current_node:
                current_node.next = next_node
                current_node = next_node
            else:
                three = next_node
                current_node = three
        return three if three else ListNode(0)
