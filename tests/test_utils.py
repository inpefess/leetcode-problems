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
from unittest import TestCase

from leetcode_problems.utils import ListNode


class TestAddTwoNumbers(TestCase):
    def setUp(self):
        self.one = ListNode(2, ListNode(4, ListNode(5)))
        self.two = ListNode(5, ListNode(6, ListNode(4)))

    def test_equal(self):
        self.assertEqual(self.one, self.one)
        self.assertNotEqual(self.one, self.two)
        self.assertNotEqual(self.one, 1)

    def test_repr(self):
        self.assertEqual(
            str(self.one),
            "[2, 4, 5]"
        )
