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

from parameterized import parameterized

from leetcode_problems.reverse_integer import Solution


class TestSolution(TestCase):
    @parameterized.expand([
        (123, 321),
        (-123, -321),
        (120, 21),
        (90000, 9),
        (1123456789, 0),
        (-1123456789, 0)
    ])
    def test_reverse(self, x, reversed_x):
        self.assertEqual(
            Solution().reverse(x),
            reversed_x
        )
