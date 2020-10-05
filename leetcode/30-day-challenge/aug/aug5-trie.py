class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie={}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        ch=self.trie
        for i in word:
            if i not in ch:
                ch[i]={}
            ch=ch[i]
        ch["*"] = True

    def dot(self,word):
        if word[index] == ".":
            for k in ch.keys():
                ch=ch[k]
                print ch
                if  not in ch:
                    return continue
                while(ch[i]!="*"):
                    ch=ch[i]
                if "*" in ch:
                    return True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        index = 0
        ch = self.trie
        for index in range(len(word)):
            if word[index] not in ch:
                return False
            ch = ch[word[index]]
        if "*" not in ch:
            return False
        return True


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()

obj.addWord("bad")
obj.addWord("dad")
print obj.search("bad")
