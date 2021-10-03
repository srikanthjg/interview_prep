class Solution():
    def __init__(self):
        self.hmap = {}
        for i in range(26):
            self.hmap[chr(ord('a')+i)] = (i+1)

    ##Rolling Hash
    def get_rolling_hash(self,sub_string,prev_hash,prev_char):

        hash=0
        #get hash
        if prev_hash==-1:
            for i in range(len(sub_string)):
                hash += (10**(len(sub_string)-1-i)) * self.hmap[sub_string[i]]

        else:
            tmp = (self.hmap[prev_char]*(10**(len(sub_string)-1)))
            #print prev_char,tmp
            hash = ((prev_hash - tmp)*10) + self.hmap[sub_string[-1]]
            #Cant do the following because of 2digit hash value eg z=26
            #h= str(prev_hash)+str(self.hmap[sub_string[-1]])
            #hash=int(h[1:])

        return hash

    def is_sub_string(self, sub_string, string):

        hash_sub = self.get_rolling_hash(sub_string, -1,'')
        print hash_sub
        i = 0
        hash_string=-1
        prev_char=''
        while i <= len(string)-len(sub_string):
            string_part = string[i:i+len(sub_string)]
            hash_string = self.get_rolling_hash(string_part, hash_string, prev_char)
            prev_char = string_part[0]
            #print string_part, hash_string, i
            if hash_string == hash_sub:
                #hash collision
                if sub_string == string_part:
                    print "found=%s" % sub_string
                    return i
            i += 1

        return -1


string = "acabd"
sub_string = "cab"
s=Solution()
print s.is_sub_string(sub_string, string)
