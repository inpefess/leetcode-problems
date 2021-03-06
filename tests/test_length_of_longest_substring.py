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
from unittest import TestCase

from parameterized import parameterized

from leetcode_problems.length_of_longest_substring import Solution


class TestLengthOfLongestSubstring(TestCase):
    @parameterized.expand([
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        (" ", 1)
    ])
    def test_solution(self, substring, length):
        self.assertEqual(
            Solution().lengthOfLongestSubstring(substring),
            length
        )
