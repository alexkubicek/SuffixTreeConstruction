import sys
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def TrieConstruction(Patterns):
    count = 0
    root = TrieNode("", count)
    count += 1
    for pattern in Patterns:
        currentNode = root
        for c in pattern:
            if c not in currentNode.children.keys():
                currentNode.children[c] = TrieNode(c,count)
                count += 1
            currentNode = currentNode.children.get(c)
        currentNode.is_end = True
    return root


#class from github
class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char, count):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many nodes have been inserted
        self.counter = count

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

    def print(self, prev):

        print(self.char, end=" ")
        for n in self.children.values():
            n.print(self.counter)


def get_suffixes(text):
    suffixes = []
    while len(text) > 0:
        suffixes.append(text)
        text = text[1:]
    return suffixes


def condense_tree(tree):
    for edge in tree.children.values():
        while len(edge.children) == 1:
            for key in edge.children.keys():
                next_char = key
            edge.char += edge.children[next_char].char
            edge.is_end = [edge.children[next_char]][0].is_end
            edge.children = [edge.children[next_char]][0].children
        condense_tree(edge)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filePath = input()
    inFile = open(filePath)
    for line in inFile:
        input_text = line
    inFile.close()
    patterns = get_suffixes(input_text)
    trie = TrieConstruction(patterns)
    condense_tree(trie)
    f = open("output.txt", 'w')
    sys.stdout = f
    for node in trie.children.values():
        node.print(0)
    f.close()
