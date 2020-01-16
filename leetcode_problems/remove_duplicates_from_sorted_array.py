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
from typing import List


# pylint: disable=too-few-public-methods
class Solution:
    """ Uses O(1) extra memory """
    # pylint: disable=invalid-name, no-self-use
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove the duplicates in-place such that each element appear only once
        and return the new length.

        :param nums: a sorted list
        :return: number of unique values in a list
        """
        if nums == list():
            return 0
        previous = nums[0]
        pos = 1
        length = len(nums)
        while pos < length:
            if nums[pos] != previous:
                previous = nums[pos]
                pos += 1
            else:
                previous = nums[pos]
                del nums[pos]
                length -= 1
        return pos
