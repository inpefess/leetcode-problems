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

from leetcode_problems.roman_to_integer import Solution


class TestSolution(TestCase):
    @parameterized.expand([
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994)
    ])
    def test_solution(self, roman, decimal):
        self.assertEqual(
            Solution().romanToInt(roman),
            decimal
        )
