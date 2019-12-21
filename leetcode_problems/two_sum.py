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
from typing import Dict, List, Set


# pylint: disable=too-few-public-methods
class Solution:
    """ linear additional memory, linear time """

    # pylint: disable=invalid-name, no-self-use
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        finds two items of a list which sum up to a given target

        :param nums: a list of integers
        :param target: a sum of two unknown list items
        :returns: a list of two indices
        """
        list_len = len(nums)
        dict_nums: Dict[int, Set[int]] = dict()
        for i in range(list_len):
            num = nums[i]
            if num in dict_nums:
                dict_nums[num].add(i)
            else:
                dict_nums[num] = {i}
        for i in range(list_len):
            remainder = target - nums[i]
            set_of_indices = dict_nums.get(remainder, set()) - {i}
            if set_of_indices:
                return [i, set_of_indices.pop()]
        return [-1, -1]


# pylint: disable=too-few-public-methods
class Solution2:
    """ constant additional memory, quadratic time """

    # pylint: disable=invalid-name, no-self-use
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        finds two items of a list which sum up to a given target

        :param nums: a list of integers
        :param target: a sum of two unknown list items
        :returns: a list of two indices
        """
        list_len = len(nums)
        for i in range(list_len):
            for j in range(i + 1, list_len):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
