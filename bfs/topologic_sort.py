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
    def canFinish(self, n, p):
        ind, g, cnt = {i : 0 for i in range(n)}, collections.defaultdict(list), 0

        for u, v in p:
            ind[u], g[v] = ind[u] + 1, g[v] + [u]

        q = collections.deque([i for i in range(n) if ind[i] == 0])

        while q:
            cnt += 1

            for u in g[q.popleft()]:
                ind[u] -= 1
                if ind[u] == 0:
                    q.append(u)

        return cnt == n
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
    def findOrder(self, n, p):
        ind, g, ans = {i: 0 for i in range(n)}, collections.defaultdict(list), []

        for u, v in p:
            ind[u], g[v] = ind[u] + 1, g[v] + [u]

        q = collections.deque([i for i in range(n) if ind[i] == 0])

        while q:
            ans.append(q.popleft())

            for u in g[ans[-1]]:
                ind[u] -= 1
                if ind[u] == 0:
                    q.append(u)

        return ans if len(ans) == n else []
"""
892. Alien Dictionary
https://www.lintcode.com/problem/alien-dictionary/description
There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
Input：["wrt","wrf","er","ett","rftt"] Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
Input：["z","x"] Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"
Notice
You may assume all letters are in lowercase.
The dictionary is invalid, if a is prefix of b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order
"""
    def alienOrder(self, words):
        # Construct Graph
        in_degree = {ch: 0 for word in words for ch in word}
        neighbors = {ch: [] for word in words for ch in word}
        for pos in range(len(words) - 1):
            for i in range(min(len(words[pos]), len(words[pos+1]))):
                pre, next = words[pos][i], words[pos+1][i]
                if pre != next:
                    in_degree[next] += 1
                    neighbors[pre].append(next)
                    break

        # Topological Sort
        heap = [ch for ch in in_degree if in_degree[ch] == 0]
        heapify(heap)
        order = []
        while heap:
            ch = heappop(heap)
            order.append(ch)
            for child in neighbors[ch]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    heappush(heap, child)
        # order is invalid
        if len(order) != len(in_degree):
            return ""
        return ''.join(order)
