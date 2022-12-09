def bracket_match(text):
  
  stack = []
  
  
  '''
  for c in text:
    
    if c == '(':
      
      stack.append(c)
      
    if c== ')':
      
      if len(stack) >0 and stack[-1] == '(':
        
        stack.pop()
      else:
        stack.append(c)

  return len(stack)
  
  '''
  
  open = 0
  closings = 0
  
  for c in text:
    
    if c == '(':

      open+= 1
      
    if c == ')':

      if open > 0:
        open -= 1
      else:
        closings += 1

  return open + closings





function bracketMatch(text):
    diffCounter = 0
    ans = 0
    n = text.length

    for i from 0 to n-1:
        if ( text[i] == '(' ):
            diffCounter += 1
        else if ( text[i] == ')' ):
            diffCounter -= 1
        if ( diffCounter < 0 ):
            diffCounter += 1
            ans += 1

    return ans + diffCounter