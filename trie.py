class Solution:
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
