def decodeVariations(S):
  """
	@param S: str
	@return: int
	"""

  '''
  DP problem
  
  -> memorization DP
  -> linear DP
  
  1262
  
  1 262    ->.  1  2. 62.    or 1. 26. 2
  
  
  
  12 62    ->   12  62.      or  12  6. 2
  
  DP 
  
  def dp(index): 
  
      if we reach index == len(S):
         result += 1
         return
      
      first_char = ind
      
      
  '''

  #result = 0

  def dp(index): 

    result = 0
    
    length = len(S)

    if index == length:
      result += 1
      return result

    

    if index+1 <= length:
      first_char = S[index:index+1]
      if int(first_char) == 0:
        return 0
      if 1 <= int(first_char) <= 9:
        result += dp(index+1)

    if index+2 <= length:
      first_two = S[index:index+2]
      if 1 <= int(first_two) <= 26:
        result += dp(index+2)

    return result

  result = dp(0)

  return result

  '''
function decodeVariations(S):
    N = S.length
    dp = new Array(N)
    dp[N] = 1
    for i from N-1 to 0:
        if S[i] == '0':
            dp[i] = 0
        else if S[i] == '1':
            dp[i] = dp[i+1] + dp[i+2]
        else if S[i] == '2':
            dp[i] = dp[i+1]
            if i+1 < S.length && S[i+1] <= '6':
                dp[i] += dp[i+2]
        else:
            dp[i] = dp[i+1]

    return dp[0]

  
  Hi Can you hear me?

  no i cant 
  can you ?
  oah ok 
  then read the question 

  ok

  Usually, after 1 minute it will refresh


  '''

