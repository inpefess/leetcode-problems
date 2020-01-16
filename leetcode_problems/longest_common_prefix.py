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
    """ linear time """
    # pylint: disable=invalid-name, no-self-use
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix string amongst an array of strings.

        :param strs: list of strings from lowercase letters a-z
        :returns: longest common prefix or an empty string if there is none
        """
        if strs == []:
            return ""
        lengths = [len(string) for string in strs]
        prefix = ""
        for i in range(min(lengths)):
            common_char = True
            current_char = strs[0][i]
            for string in strs:
                if string[i] != current_char:
                    common_char = False
                    break
            if common_char:
                prefix += current_char
            else:
                break
        return prefix
