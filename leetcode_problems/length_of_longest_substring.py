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
from typing import Dict


# pylint: disable=too-few-public-methods
class Solution:
    """ Can be copied and pasted to LeetCode site. """

    # pylint: disable=invalid-name, no-self-use
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string, find the length of the longest substring without
        repeating characters.

        :param s: input string
        :returns: the length of the optimal substring
        """
        str_len = len(s)
        substr: Dict[str, int] = dict()
        max_len = 0
        start_index = 0
        for i in range(str_len):
            duplicate_index = substr.get(s[i], -1)
            if duplicate_index != -1:
                current_len = i - start_index
                if current_len > max_len:
                    max_len = current_len
                for j in range(start_index, duplicate_index + 1):
                    del substr[s[j]]
                start_index = duplicate_index + 1
            substr[s[i]] = i
        current_len = str_len - start_index
        if current_len > max_len:
            max_len = current_len
        return max_len
