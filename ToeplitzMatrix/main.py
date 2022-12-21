def isToeplitz(arr):
 
 hm = {}

 for i in range(len(arr)):
  for j in range(len(arr[0])):

   if i - j not in hm:

    hm[i-j] = arr[i][j]

   elif hm[i-j] != arr[i][j]:
    return False

 return True
