import string


##Remove punctuation
p= string.punctuation
print p
dmap= dict.fromkeys(p)
print dmap

s="Hello,  WOrld!"
s1=""
i=0
for i in range(len(s)):
    if s[i] not in dmap:
        s1=s1+s[i]
print s1
