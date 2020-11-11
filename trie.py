class Solution:
"""
132. Word Search II
https://www.lintcode.com/problem/word-search-ii/description
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. One character only be used once in one word. No same word in dictionary
Input：["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"] Output：["again","can","dad","dog"]
Explanation：
  d o a f
  a g a i
  d c a n
search in Matrix，so return ["again","can","dad","dog"].
Input：["a"]，["b"] Output：[] Explanation a
search in Matrix，return [].
Challenge Using trie to implement your algorithm.
"""
    class Node:
        def __init__(self):
            self.w, self.chldrn = None, {}

    def findWords(self, b: List[List[str]], wrds: List[str]) -> List[str]:
        r, ans = self.Node(), set()

        for w in wrds:
            n = r
            for c in w:
                n.chldrn[c] = n = n.chldrn.get(c, self.Node())
            n.w = w

        for i in range(len(b)):
            for j in range(len(b[0])):
                self.dfs(b, ans, set([(i, j)]), r, i, j)

        return list(ans)

    #dfs, trie剪枝
    def dfs(self, b, ans, s, n, ux, uy):
        n = n.chldrn.get(b[ux][uy])

        if not n:
            return

        if n.w:
            ans.add(n.w)

        for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            v = (vx, vy) = ux + dx, uy + dy

            if 0 <= vx < len(b) and 0 <= vy < len(b[0]) and v not in s:
                s.add(v)
                self.dfs(b, ans, s, n, vx, vy)
                s.remove(v)
"""
442. Implement Trie (Prefix Tree)
https://www.lintcode.com/problem/implement-trie-prefix-tree/description
Implement a Trie with insert, search, and startsWith methods.
"""
    class Trie:

        class Node: #node本身只是个壳子，用map表示 下一个char : 下一个node
            def __init__(self):
                self.chldrn, self.is_word = {}, False

    def __init__(self):
        self.r = self.Node()

    def insert(self, w):
        n = self.r

        for c in w:
            n.chldrn[c] = n = n.chldrn.get(c, self.Node())

        n.is_word = True

    def search(self, w):
        n = self.r
        for c in w:
            if c not in n.chldrn:
                return False
            n = n.chldrn[c]

        return n.is_word

    def startsWith(self, prefix):
        n = self.r
        for c in prefix:
            if c not in n.chldrn:
                return False
            n = n.chldrn[c]

        return len(n.chldrn) > 0 or n.is_word
"""
473. Add and Search Word - Data structure design
https://www.lintcode.com/problem/add-and-search-word-data-structure-design/description
Design a data structure that supports the following two operations: addWord(word) and search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or ..
A . means it can represent any one letter.
"""
    class WordDictionary:

        class Node:

            def __init__(self):
                self.is_word, self.chldrn = False, {}

        def __init__(self):
            self.root = self.Node()
        """
        @param: word: Adds a word into the data structure.
        @return: nothing
        """
        def addWord(self, word):
            n = self.root

            for c in word:
                n.chldrn[c] = n = n.chldrn.get(c, self.Node())

            n.is_word = True
        """
        @param: word: A word could contain the dot character '.' to represent any one letter.
        @return: if the word is in the data structure.
        """
        def search(self, word):
            return self.search_helper(self.root, word, 0)

        def search_helper(self, n, word, i):
            if n is None:
                return False

            if i == len(word):
                return n.is_word

            if word[i] != '.':
                return self.search_helper(n.chldrn.get(word[i]), word, i + 1)

            for c, c_n in n.chldrn.items():
                if self.search_helper(c_n, word, i + 1):
                    return True

            return False

        def search_util(self, w):
            n = self.root

            for c in w:
                if c == '.':
                    for c, c_n in n.chldrn.items():
                        self.search_util()
"""
559. Trie Service
Build tries from a list of <word, freq> pairs. Save top 10 for each node
Input:  <"abc", 2> <"ac", 4> <"ab", 9>
Output:<a[9,4,2]<b[9,2]<c[2]<>>c[4]<>>>
Explanation:
			Root
             /
           a(9,4,2)
          /    \
        b(9,2) c(4)
       /
     c(2)
"""
    class TrieService:

        def __init__(self):
            self.root = TrieNode()

        def get_root(self):
            # Return root of trie root, and
            # lintcode will print the tree struct.
            return self.root

        # @param {str} word a string
        # @param {int} frequency an integer
        # @return nothing
        def insert(self, word, frequency):
            # Write your your code here
            node = self.root
            for letter in word:
                child = node.children.get(letter, None)

                if child is None:
                    child = TrieNode()

                node.children[letter] = child
                self.add_frequency(child.top10, frequency)

                node = child

        def add_frequency(self, top10, frequency):
            top10.append(frequency)
            index = len(top10) - 1
            while index > 0:
                if top10[index] > top10[index - 1]:
                    top10[index], top10[index - 1] = top10[index - 1], top10[index]
                    index -= 1
                else:
                    break
            if len(top10) > 10:
                top10.pop()
"""
634. Word Squares
Given a set of words without duplicates, find all word squares you can build from them.
A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
b a l l
a r e a
l e a d
l a d y
Input: ["area","lead","wall","lady","ball"] Output: [["wall","area","lead","lady"],["ball","area","lead","lady"]]
Explanation: The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Input: ["abat","baba","atan","atal"] Output: [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
Notice:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
"""
    class Node:
        def __init__(self):
            self.strtWith, self.chldrn = set(), {}

    def wordSquares(self, wrds):
        r = self.Node()

        for w in wrds:
            r.strtWith.add(w)
            n = r
            for c in w:
                n.chldrn[c] = n = n.chldrn.get(c, self.Node())
                n.strtWith.add(w)

        rslts = []
        self.dfs(rslts,[], r)
        return rslts

    def dfs(self, rslts, rslt, r):
        i = len(rslt)

        if i > 0 and i == len(rslt[-1]):
            rslts.append(rslt[:])
            return

        n = r
        for w in rslt:
            if w[i] not in n.chldrn:
                return
            n = n.chldrn[w[i]]

        for w in n.strtWith:
            rslt.append(w)
            self.dfs(rslts, rslt, r)
            rslt.remove(w)
