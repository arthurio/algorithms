# Generalized Trie
class TrieNode(object):

    def __init__(self, key, value):
        self._key = None
        self.key = key
        self._value = None
        self.value = value
        self._children = dict()
        self._is_leaf = False

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def is_leaf(self):
        return self._is_leaf

    def set_is_leaf(self):
        self._is_leaf = True

    def add_child_node(self, node):
        self._children[node.key] = node

    def get_child_node(self, node):
        return self._children.get(node.key)

    def get_children_nodes(self):
        return self._children.values()

    def has_children(self):
        return len(self._children) > 0

    def __str__(self):
        return (self.key, self.value)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()


class RootTrieNode(TrieNode):
    def __init__(self, key=None, value=None):
        super(RootTrieNode, self).__init__(key, value)

    def __str__(self):
        return 'Root'


class Trie(object):
    def __init__(self, root=None):
        if not root:
            root = RootTrieNode(None, None)
        self._root = root

    def add(self, nodes):
        current_node = self._root
        for node in nodes:
            if current_node.get_child_node(node) is None:
                current_node.add_child_node(node)

            current_node = current_node.get_child_node(node)

        current_node.set_is_leaf()

    def is_valid(self, nodes):
        current_node = self._root
        for node in nodes:
            current_node = current_node.get_child_node(node)
            if not current_node:
                return False
        return current_node.is_leaf()

    def get_leafs_with_value(self):
        stack = [(self._root, self._root.key)]
        leafs = []
        while stack:
            node, key = stack.pop()

            if node.is_leaf():
                leafs.append((key, node.value))

            if node.has_children():
                for child_node in node.get_children_nodes():
                    stack.append((
                        child_node,
                        key + child_node.key,
                    ))

        return leafs


# Specialized Trie
class WordCountTrieNode(TrieNode):

    def __init__(self, key):
        return super(WordCountTrieNode, self).__init__(key, 0)

    def set_is_leaf(self):
        super(WordCountTrieNode, self).set_is_leaf()
        self.value += 1


class WordCountRootTrieNode(RootTrieNode):
    def __init__(self):
        super(WordCountRootTrieNode, self).__init__("", 0)

    def set_is_word(self):
        raise Exception("The root node can't be a word")


class WordCountTrie(Trie):
    def __init__(self):
        self._root = WordCountRootTrieNode()

    def get_letters_as_nodes(self, word):
        for letter in word:
            yield WordCountTrieNode(letter.lower())

    def add(self, word):
        super(WordCountTrie, self).add(self.get_letters_as_nodes(word))

    def is_valid(self, word):
        return super(WordCountTrie, self).is_valid(self.get_letters_as_nodes(word))

    def get_all_words(self):
        words = self.get_leafs_with_value()
        return sorted(words)
