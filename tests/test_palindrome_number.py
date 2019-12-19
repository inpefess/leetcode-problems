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

from leetcode_problems.palindrome_number import Solution


class TestSolution(TestCase):
    @parameterized.expand([
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (1, True),
        (22, True),
        (1991, True),
        (334, False)
    ])
    def test_reverse(self, x, is_palindrome):
        self.assertEqual(
            Solution().isPalindrome(x),
            is_palindrome
        )
