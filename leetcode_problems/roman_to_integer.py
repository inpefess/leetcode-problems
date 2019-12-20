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
    """ goes through symbols only once """
    roman_digits = {
        "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1,
    }

    # pylint: disable=invalid-name, no-self-use
    def romanToInt(self, s: str) -> int:
        """
        Given a roman numeral, convert it to an integer.

        :param s: a Roman numeral within the range from 1 to 3999
        :return: a corresponding decimal number
        """
        decimal = 0
        previous_value = 10000
        for current_char in s:
            current_value = self.roman_digits[current_char]
            if current_value <= previous_value:
                decimal += current_value
            else:
                decimal += current_value - 2 * previous_value
            previous_value = current_value
        return decimal
