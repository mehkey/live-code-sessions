def diffBetweenTwoStrings(source, target):
  """
  @param source: str
  @param target: str
  @return: str[]
  """
  ans = []
  i = 0
  j = 0
  
  memo = [[0]*len(source) for i in range(len(target))]

  def dp(i, j):
        # If one of the strings is empty, we know
        # the answer already.
        if i == len(source) or j == len(target):
            return len(target) - j

        # Otherwise, if we don't have a cached answer,
        # then find one.
        elif memo[i][j] == None:
            if source[i] == target[j]:
                memo[i][j] = dp(i+1, j+1)
            else:
                memo[i][j] = 1 + min(dp(i+1, j), dp(i, j+1))

        return memo[i][j]
  # We are always considering strings source[i:] and target[j:]
  while i < len(source) and j < len(target):
      if source[i] == target[j]:
          # Write the string with no edits
          ans.append(source[i])
          i += 1
          j += 1
      else:
          # We have to decide whether to subtract source[i],
          # or add target[j].
          if dp(i+1, j) <= dp(i, j+1):
              ans.append('-' + source[i])
              i += 1
          else:
              ans.append('+' + target[j])
              j += 1

  while j < len(target):
      ans.append('+' + target[j])
      j += 1

  return " ".join(ans)