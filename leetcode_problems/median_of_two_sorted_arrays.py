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
from heapq import merge
from typing import List


class Solution:
    def median(self, nums: List[int]) -> float:
        nums_len = len(nums)
        if nums_len % 2 == 0:
            middle_index = nums_len // 2
            return (nums[middle_index - 1] +
                    nums[middle_index]) / 2
        else:
            return float(nums[(nums_len - 1) // 2])

    def findMedianSortedArrays(
            self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of the two sorted arrays.

        :param nums1: first sorted list
        :param nums2: second sorted list
        :returns: median of a combined list
        """
        return self.median(list(merge(nums1, nums2)))
        median1 = self.median(nums1) if nums1 else None
        median2 = self.median(nums2) if nums2 else None
        if median1 is None:
            return median2
        if median2 is None:
            return median1
        if nums1[-1] <= nums2[0]:
            return self.median(nums1 + nums2)
        if nums2[-1] <= nums1[0]:
            return self.median(nums2 + nums1)       
        return (median1 + median2) / 2
