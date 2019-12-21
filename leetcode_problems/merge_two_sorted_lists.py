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

from leetcode_problems.utils import ListNode


# pylint: disable=too-few-public-methods
class Solution:
    """ time complexity is O(m+n) """
    # pylint: disable=invalid-name, no-self-use
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Merge two sorted linked lists and return it as a new list.

        :param l1: one sorted list
        :param l2: another sorted list
        :return: merged sorted list
        """
        one: Optional["ListNode"] = l1
        two: Optional["ListNode"] = l2
        three = ListNode(0)
        current_node = three
        while one and two:
            if one.val <= two.val:
                current_node.next = ListNode(one.val)
                one = one.next
            else:
                current_node.next = ListNode(two.val)
                two = two.next
            current_node = current_node.next
        current_node.next = one if one else two
        return three.next
