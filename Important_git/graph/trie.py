class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head={}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch]={}
            cur=cur[ch]
        cur["*"]=True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur=self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if "*" in cur:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur=self.head
        for ch in prefix:
            if ch not in cur:
                return False
            cur=cur[ch]
        return True

s1="hello"
s2="ello"
s3="hear"

trie = Trie()
trie.add(s1)
trie.add(s2)
trie.add(s3)

print trie.search(s1)
