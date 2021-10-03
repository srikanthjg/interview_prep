##Rolling Hash

def get_rolling_hash(sub_string):
    hash=0

    hmap={}
    for i in range(26):
        hmap[chr(97+i)]=i+1
    #print hmap
    i=len(sub_string)
    #print i
    for ch in sub_string:
        hash+= hmap[ch]*(10**(i-1))
        i-=1
        #print ch,hash
    #print hash
    return hash

def is_sub_string(sub_string,string):

    hash_sub=get_rolling_hash(sub_string)
    i=0
    while i < len(string)-len(sub_string)+1:
        string_part=string[i:i+len(sub_string)]
        hash_string=get_rolling_hash(string_part)
        #print string_part,hash_string,i
        if hash_string==hash_sub:
            if sub_string==string_part:
                return i
        i+=1

    return -1

string="abcadfsdfljacabdslkgjfg"
sub_string="cab"
print is_sub_string(sub_string, string)
