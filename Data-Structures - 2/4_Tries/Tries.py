class Trie:
    def __init__(self):
        self.a = {}
        self.b = False

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.a:
                node.a[char] = Trie()
            node = node.a[char]
        node.b = True

    def search(self, word):
        node = self
        for char in word:
            if char not in node.a:
                return False
            node = node.a[char]
        return node.b

trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

print(trie.search("app"))  
print(trie.search("orange")) 