def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        symbol = {

'I':            1,
'V':            5,
'X':            10,
'L':            50,
'C':            100,
'D':            500,
'M':            1000,
        }

        output=0
        length = len(s)-1
        i = 0
        #print "length = %d"%(length)
        while(i<=length):
                #print i,length,
                if s[i] == 'I':
            #        print "Icase",
                    #if not the last
                    if(i != length and
                        ( (s[i+1] == 'V') or
                          (s[i+1] == 'X') )):
                        #print "in excpt"
                        output = output + (symbol[s[i+1]] - symbol['I'])
                        i = i + 2
            #            print i,
                    else:
                        #III
            #            print s[i]
                        output = output + symbol[s[i]]
                        i = i + 1


                elif s[i] == 'X':
            #        print "Xcase",
                    if(i != length and
                        ( (s[i+1] == 'L') or
                          (s[i+1] == 'C') )):
                        output = output + (symbol[s[i+1]] - symbol['X'])
                        i = i + 2
                    else:
                        #III
            #            print s[i]
                        output = output + symbol[s[i]]
                        i = i + 1
                elif s[i] == 'C':
            #        print "Ccase",
                    if(i != length and
                        ( (s[i+1] == 'D') or
                          (s[i+1] == 'M') )):
                        output = output + (symbol[s[i+1]] - symbol['C'])
                        i = i + 2
                    else:
                        #III
            #            print s[i]
                        output = output + symbol[s[i]]
                        i = i + 1

                else:
                    #III
            #        print s[i]
                    output = output + symbol[s[i]]
                    i = i + 1
                print ""
                print output
        return output


romanToInt("DCXXI")
