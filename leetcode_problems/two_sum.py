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
from typing import List


class Solution:
    """ constant additional memory, O(n^2) time """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        finds two items of a list which sum up to a given target

        :param nums: a list of integers
        :param target: a sum of two unknown list items
        :returns: a list of two indices
        """
        array_size = len(nums)
        for i in range(array_size):
            for j in range(i + 1, array_size):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
