def deletion_distance(str1, str2):


  def deletion_distance_dp(index1, index2) : # return recurison is the minimum number of edits
    #base case
    
    #cache[(i,j)] = (i,j)
    if index1 == len(str1) and index2 == len(str2):
      return 0
    
    if index1 == len(str1):
      return len(str2) - index2
    if index2 == len(str2):
      return len(str1) - index1
    
    if str1[index1] == str2[index2]:
      return deletion_distance_dp(index1+1,index2+1) # + 1

    #recursion
    return 1 + min(deletion_distance_dp(index1+1,index2), deletion_distance_dp(index1,index2+1) )

  #start value
  return deletion_distance_dp(0, 0)

print(deletion_distance("dog", "frog"))

print(deletion_distance("", "hit"))

print(deletion_distance("awesome", "awesome"))