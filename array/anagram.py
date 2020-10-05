


## ""

def isAnagram_sort(s1,s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)

def isAnagram_hashTable(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = s1.replace(" ","")
    s2 = s2.replace(" ","")

    if len(s1) != len(s2):
        return False

    #key = letter value = count
    dict = {}
    for i in range(len(s1)):
        if s1[i] not in dict:
            dict[s1[i]] = 1
        else:
            dict[s1[i]] +=1

    for i in range(len(s2)):
        if s2[i] not in dict:
            return False
        elif dict[s2[i]] == 0:
            return False
        else:
            dict[s2[i]] -=1
    print dict
    return True

s1 = "aacc"
s2 = "acca"
print isAnagram_hashTable(s1,s2)
print isAnagram_sort(s1,s2)
