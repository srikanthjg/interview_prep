
def permutationHelper(chosen,rest):
	print chosen,rest
	if len(rest)==0:
		print "".join(chosen)


	for i in range(len(rest)):
		chosen.append(rest[i])
		tmp = rest.pop(i)
		permutationHelper(chosen,rest)
		chosen.pop()
		rest.insert(i,tmp)

def permutation(num):
	chosen = []
	rest = list(str(num))
	permutationHelper(chosen,rest)



def permutation2Helper(arr,l,r):
	if l==r:
		output.append("".join(arr))
		return

	for i in range(len(arr)):
		#print i,l
		arr[i],arr[l] = arr[l],arr[i]
		permutation2Helper(arr,l+1,r)
		arr[i],arr[l] = arr[l],arr[i]

def permutation2(num):
	permutation2Helper(list(str(num)),0,len(list(str(num))))
	return

num = 123
output = []
permutation(num)
#permutation2(num)
#print len(sorted(output))
#print len(sorted(set(output)))
