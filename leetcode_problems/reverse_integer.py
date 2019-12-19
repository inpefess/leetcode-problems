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


class Solution:
    """ two passes through all digits """
    def reverse(self, x: int) -> int:
        """
        Given a 32-bit signed integer, reverse digits of an integer.

        :param x: an integer between -2^31 and 2^31 - 1
        :return: an integer with the same sign and digits reversed or 0 when
        the reversed integer overflows.
        """
        abs_x = abs(x)
        power = 1
        while abs_x >= 10:
            power *= 10
            abs_x //= 10
        reversed_x = 0
        abs_x = abs(x)
        while power > 0:
            reversed_x += abs_x % 10 * power
            abs_x //= 10
            power //= 10
        if x < 0:
            result = -reversed_x
            if result < -2147483648:
                result = 0
        else:
            result = reversed_x
            if result > 2147483647:
                result = 0
        return result
