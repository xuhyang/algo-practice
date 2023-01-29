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


"""
524. Longest Word in Dictionary through Deleting
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
Input: s = "abpcplea", d = ["ale","apple","monkey","plea"] Output: "apple"
Input: s = "abpcplea", d = ["a","b","c"] Output: "a"
"""
   def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d, key = lambda e : (-len(e), e))

        for e in d:
            i = 0

            for c in s:
                if c == e[i]:
                    i += 1
                if i == len(e):
                    return e

        return ''
"""
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
"""
    def minRemoveToMakeValid(self, s: str) -> str:
        l, mtchd, a, ans = 0, 0, [], []

        for i, c in enumerate(s):
            if c == '(':
                l += 1
            elif c == ')':
                if not l - mtchd:
                    continue
                mtchd += 1
            a.append(c)

        for i, c in  enumerate(a):
            if c == '(':
                if not mtchd:
                    continue
                mtchd -= 1
            ans.append(c)

        return ''.join(ans)
