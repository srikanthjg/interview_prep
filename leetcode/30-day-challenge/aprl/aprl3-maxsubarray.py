def maxSubArray(arr):
  cur_max=0
  max_so_far=0
  subarr=[]
  
  for i in range(1,len(arr)):
    cur_max = max(arr[i],cur_max+arr[i])
    max_so_far = max(max_so_far,cur_max)
  return max_so_far

arr = [-1,2,3,4,-10]
print maxSubArray(arr)
