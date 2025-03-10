# Recursive Python program to check if a string is subsequence
# of another string

# Returns true if str1[] is a subsequence of str2[].
def isSubSequence(string1, string2,m,n):

    # Base Cases
    if m == 0:    return True
    if n == 0:    return False

    # If last characters of two strings are matching
    if string1[m-1] == string2[n-1]:
        return isSubSequence(string1, string2, m-1, n-1)

    # If last characters are not matching
    return isSubSequence(string1, string2, m, n-1)

# Driver program to test the above function
string1 = "gksrek"
string2 = "geeksforgeeks"
m = len(string1)
n = len(string2)
if isSubSequence(string1, string2,m,n):
    print "Yes"
else:
    print "No"

for i in range(4,-1,-1):
    print i
