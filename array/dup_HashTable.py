

def dup(a):

    a = list(a)

    #init dict
    dict_char = {}
    for i in a:
        dict_char[i]=0
    # or 
    #dict_char = dict.fromkeys(a,0)
    print "dict=%r"%dict_char
    for i in range(len(a)):
        #if a[i] not in dict_char:
        #    dict_char[a[i]] += 1
        #else:
            dict_char[a[i]] += 1

    print dict_char
    for k,v in dict_char.items():
        if v >1:
            return False
        else:
            return True

def dup_set(a):
    return len(a) == len(set(a))


s = "abjgfrg"
print dup(s)
print dup_set(s)
