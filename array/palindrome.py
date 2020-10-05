
def isPalindrome(A):
	length = len(A)
	i=0
	j=length - 1
	A = A.lower()
	arr=""
	A = list(A)
	for ch in A:
		if ch.isalnum() == True:
			arr += ch
	print(arr)

	return 1

A = "s; ; r"
print (isPalindrome(A))
