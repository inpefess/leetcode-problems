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


# pylint: disable=too-few-public-methods
class Solution:
    """ Goes through the digits twice. """

    # pylint: disable=invalid-name, no-self-use
    def isPalindrome(self, x: int) -> bool:
        """
        Determine whether an integer is a palindrome. An integer is a
        palindrome when it reads the same backward as forward.

        :param x: an integer to check
        :returns: is `x` palindrome or not
        """
        if x < 0:
            return False
        abs_x = x
        power = 1
        while abs_x >= 10:
            power *= 10
            abs_x //= 10
        abs_x = x
        while power > 0:
            if abs_x // power != abs_x % 10:
                return False
            abs_x %= power
            abs_x //= 10
            power //= 100
        return True
