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

from leetcode_problems.median_of_two_sorted_arrays import Solution


class TestSolution(TestCase):
    @parameterized.expand([
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([1, 2, 3], [2, 3, 4], 2.5),
        ([1, 2, 3], [3, 4, 5], 3.0),
        ([3], [-2, -1], -1.0),
        ([], [1], 1.0),
        ([1, 2], [-1, 3], 1.5)
    ])
    def test_solution(self, nums1, nums2, median):
        self.assertEqual(
            Solution().findMedianSortedArrays(nums1, nums2),
            median
        )