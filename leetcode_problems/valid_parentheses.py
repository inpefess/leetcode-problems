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


# pylint: disable=too-few-public-methods
class Solution:
    """ one pass through the input string """
    # pylint: disable=invalid-name, no-self-use
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string is valid.
        An input string is valid if:
        * Open brackets must be closed by the same type of brackets.
        * Open brackets must be closed in the correct order.
        An empty string is also considered valid.

        :param s: a string containing just the characters
                  '(', ')', '{', '}', '[', and ']'
        :return: whether the input string has valid parentheses order or not
        """
        parentheses = []
        for c in s:
            if c in ("(", "{", "["):
                parentheses.append(c)
            else:
                if parentheses == list():
                    return False
                if c == ")":
                    if parentheses.pop() != "(":
                        return False
                elif c == "}":
                    if parentheses.pop() != "{":
                        return False
                elif c == "]":
                    if parentheses.pop() != "[":
                        return False
        return parentheses == list()
