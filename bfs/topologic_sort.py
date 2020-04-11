class topological_sort:
"""
605. Sequence Reconstruction
https://www.lintcode.com/problem/sequence-reconstruction/description
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 10^4. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
Input:org = [1,2,3], seqs = [[1,2],[1,3]] Output: false
Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Input: org = [1,2,3], seqs = [[1,2]] Output: false
Explanation: The reconstructed sequence can only be [1,2].
Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]] Output: true
Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]] Output:true
"""
    def sequenceReconstruction(self, org, seqs):
        d, g = {}, {}

        for s in seqs:
            for i in range(len(s)):
                g[s[i]], d[s[i]] = g.get(s[i], []), d.get(s[i], 0)
                if i > 0:
                    g[s[i - 1]].append(s[i])
                    d[s[i]] += 1

        q, rslt = collections.deque([k for k, v in d.items() if v == 0]), []

        while q:
            if len(q) > 1: # 出现了两条 top sort
                return False

            rslt.append(q[0])
            for n in g[q.popleft()]:
                d[n] -= 1
                if d[n] == 0:
                    q.append(n)

        return rslt == org
"""
615. Course Schedule
https://www.lintcode.com/problem/course-schedule/description
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Input: n = 2, prerequisites = [[1,0]] Output: true
Input: n = 2, prerequisites = [[1,0],[0,1]] Output: false
"""
    def canFinish(self, numCourses, prerequisites):
        n_to_indgrs, n_to_dpndnts = {i : 0 for i in range(numCourses)}, {i : [] for i in range(numCourses)}
        cnt = 0

        for prqst in prerequisites:
            n_to_indgrs[prqst[0]] += 1
            n_to_dpndnts[prqst[1]].append(prqst[0])

        queue = collections.deque([i for i in range(numCourses) if n_to_indgrs[i] == 0])

        while queue:
            cnt += 1

            for dpndnt in n_to_dpndnts[queue.popleft()]:
                n_to_indgrs[dpndnt] -= 1
                if n_to_indgrs[dpndnt] == 0:
                    queue.append(dpndnt)

        return numCourses == cnt
"""
616. Course Schedule II
https://www.lintcode.com/problem/course-schedule-ii/description
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
Input: n = 2, prerequisites = [[1,0]]  Output: [0,1]
Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] Output: [0,1,2,3] or [0,2,1,3]
"""
    def findOrder(self, numCourses, prerequisites):
        n_to_indgrs, n_to_dpndnts = {i : 0 for i in range(numCourses)}, {i : [] for i in range(numCourses)}

        for prqst in prerequisites:
            n_to_indgrs[prqst[0]] += 1
            n_to_dpndnts[prqst[1]].append(prqst[0])

        queue, order = collections.deque([i for i in range(numCourses) if n_to_indgrs[i] == 0]), []

        while queue:
            order.append(queue.popleft())

            for dpndnt in n_to_dpndnts[order[-1]]:
                n_to_indgrs[dpndnt] -= 1
                if n_to_indgrs[dpndnt] == 0:
                    queue.append(dpndnt)

        return order if numCourses == len(order) else []