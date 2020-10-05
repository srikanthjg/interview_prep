

def sentence_reversal(sentence):
    a = sentence.split(" ")
    print a
    for i in range(len(a)//2):
        a[i], a[len(a)-1-i] =  a[len(a)-1-i], a[i]
    return " ".join(a)

#sentence = "this is srikanth govindarajan !"
#print sentence_reversal(sentence)


def string_compress(a):
    output=[]
    a = list(a)

    cur = a[0]
    count = 1

    if len(a) == 1:
        output.append(cur)
        output.append('1')

## WRITE AGAIN!!!!!!!!
    for i in range(1,len(a)):
        if a[i] == a[i-1]:
            count += 1
        if i+1 == len(a):
            if a[i] == a[i-1]:
                output.append(a[i])
                output.append(str(count))
                #print a[i],count
                break
            else:
                output.append(a[i])
                output.append('1')
                #print a[i],count
        if a[i] != a[i+1]:
            output.append(a[i])
            output.append(str(count))
            #print a[i],count
            count = 1
    output = "".join(output)

    return output

print string_compress("AAAaaaa")
