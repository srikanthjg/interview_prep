class Solution(object):
    def createMap(self,magazine):
        letters={}
        for i in magazine:
            if i not in letters:
                letters[i]=1
            else:
                letters[i]=letters[i]+1
        return letters
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = self.createMap(magazine)
        for letter in ransomNote:
            if letter not in hashmap:
                return False
            if hashmap[letter]==0:
                return False
            hashmap[letter] = hashmap[letter]-1
        return True
