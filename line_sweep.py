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
919. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.
Input: intervals = [(0,30),(5,10),(15,20)] Output: 2
Explanation: We need two meeting rooms
room1: (0,30) room2: (5,10),(15,20)
Input: intervals = [(2,7)] Output: 1
Explanation: Only need one meeting room
"""
    def minMeetingRooms(self, intervals):
        a, cnt, max_cnt = [], 0, 0

        for i in intervals:
            a.append((i.start, 1))
            a.append((i.end, -1))

        for t, d in sorted(a):
            cnt += d
            max_cnt = max(max_cnt, cnt)

        return max_cnt
"""
920. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
Input: intervals = [(0,30),(5,10),(15,20)] Output: false Explanation: (0,30), (5,10) and (0,30),(15,20) will conflict
Input: intervals = [(5,8),(9,15)] Output: true Explanation: Two times will not conflict
Notice: (0,8),(8,10) is not conflict at 8
"""
    def canAttendMeetings(self, i):
        a = []

        for e in i:
            a.append((e.start, 1))
            a.append((e.end, -1))

        cnt = 0
        for t, state in sorted(a):
            cnt += state

            if cnt > 1:
                return False

        return True
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
        pnts = []
        for a in seqA:
            pnts.append((a.start, 1))
            pnts.append((a.end, -1))
        for b in seqB:
            pnts.append((b.start, 1))
            pnts.append((b.end, -1))

        result = []
        start, end = 0, 0
        count = 0
        for time, delta_count in sorted(pnts):
            count += delta_count
            if count == 2:
                start = time

            if count == 1 and delta_count == -1:
                end = time
                result.append(Interval(start, end))
                start = 0
                end = 0
        return results
"""
636. Exclusive Time of Functions
https://leetcode.com/problems/exclusive-time-of-functions/
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.
Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.
You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.
A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.
Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.
Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"] Output: [3,4]
Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"] Output: [8]
Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"] Output: [7,1]
Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"] Output: [8,1]
Input: n = 1, logs = ["0:start:0","0:end:0"] Output: [1]
"""
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        s, ans, prv_t = [], [0] * n, 0

        for log in logs:
            fn, typ, t = log.split(':')
            fn, t = int(fn), int(t)

            if typ == 'start':
                if s:
                    ans[s[-1]] += t - prv_t
                s.append(fn)
                prv_t = t
            else:
                ans[s.pop()] += t - prv_t + 1
                prv_t = t + 1

        return ans
