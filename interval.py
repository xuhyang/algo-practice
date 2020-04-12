class Interval:
"""
641. Missing Ranges
https://www.lintcode.com/problem/missing-ranges/description
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper],
return its missing ranges.
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99 Output: ["2", "4->49", "51->74", "76->99"]
Explanation: in range[0,99],the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]
"""
    def findMissingRanges(self, a, lower, upper):

        if not a or a[0] != lower:
            a.insert(0, lower - 1)
        if a[-1] != upper:
            a.append(upper + 1)

        rslt = []
        for i in range(1, len(a)):
            s, e = a[i - 1] + 1, a[i] - 1

            if s == e:
                rslt.append(str(s))
            elif s < e:
                rslt.append(str(s) + '->' + str(e))

        return rslt
