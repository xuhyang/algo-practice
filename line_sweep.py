class line_sweep:
"""
391. Number of Airplanes in the Sky
https://www.lintcode.com/problem/number-of-airplanes-in-the-sky/description
Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?
Example Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
"""
    def countOfAirplanes(self, airplanes):
        a, cnt, max_cnt = [], 0, 0

        for airplane in airplanes:
            a.append((airplane.start, 1))
            a.append((airplane.end, -1))

        for t, state in sorted(a):
            cnt += state
            max_cnt = max(max_cnt, cnt)

        return max_cnt
"""
821: Time intersection
https://www.jiuzhang.com/solution/time-intersection/#tag-other-lang-python
Give two users' ordered online time series, and each section records the user's login time point x
and offline time point y. Find out the time periods when both users are online at the same time,
and output in ascending order.
Notice: we guarantee that the length of online time series meet 1 <= len <= 1e6.
For a user's online time series, any two of its sections do not intersect.
Example: Given a = [[1,2],[5,100]], b = [[1,6]], return [[1,2],[5,6]].
Explanation: In these two time periods [1,2],[5,6], both users are online at the same time.
Given a = [[1,2],[10,15]], b = [[3,5],[7,9]], return [].
其他做法： 同向双指针
"""
    def timeIntersection(self, seqA, seqB):
        points = []
        for a in seqA:
            points.append((a.start, 1))
            points.append((a.end, -1))
        for b in seqB:
            points.append((b.start, 1))
            points.append((b.end, -1))

        result = []
        start, end = 0, 0
        count = 0
        for time, delta_count in sorted(points):
            count += delta_count
            if count == 2:
                start = time

            if count == 1 and delta_count == -1:
                end = time
                result.append(Interval(start, end))
                start = 0
                end = 0
        return result
