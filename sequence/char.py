class array:
"""
686. Repeated String Match
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.
Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 times is "abcabc".
Example 1: Input: a = "abcd", b = "cdabcdab" Output: 3 Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
Example 2: Input: a = "a", b = "aa" Output: 2
Example 3: Input: a = "a", b = "a" Output: 1
Example 4: Input: a = "abc", b = "wxyz" Output: -1
"""
    def repeatedStringMatch(self, a: str, b: str) -> int:

        for f in range(1, len(b) // len(a) + 3):
            if (a * f).find(b) != -1:
                return f

        return -1
"""
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR". Write the code that will take a string and make this conversion given a number of rows: string convert(string s, int numRows);
Example 1: Input: s = "PAYPALISHIRING", numRows = 3 Output: "PAHNAPLSIIGYIR"
Example 2: Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI" Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3: Input: s = "A", numRows = 1 Output: "A"
"""
    def convert(self, s: str, nr: int) -> str:
        z, i, d = [[] for _ in range(nr)], 0, 1

        for c in s:
            z[i].append(c)

            if nr == 1:
                continue
            if i == nr - 1:
                d = -1
            elif i == 0:
                d = 1

            i += d

        return ''.join([''.join(e) for e in z])
224. Basic Calculator
