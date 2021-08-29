'''
https://www.acmicpc.net/problem/5052
'''


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if curr_node.data != None:
                return False
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string
        return True


t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    yes = True
    string = [input() for _ in range(n)]

    for str in string:
        if not trie.insert(str):
            yes = False
            break
    if yes:
        print("YES")
    else:
        print("NO")
