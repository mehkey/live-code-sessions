


def regex_match(text, pattern):



def is_match(text, pattern):
  
  
  '''
  
  Regex (pattern) and a String (text)
  
  Does the Text match the regex?


  Approach 1:
  
  Use a Regex Library

  Approach 2:
  
  Double Pointer Loop
  
  1st pointer poins to the text
  2snd pointer points to the regex
    if the pointer is on a dot
      increment both pointers
      
    if the pointer is on wildcard
      increment the pointer while string pointer is on the previous letter

    otherwise if pointers point to the same character
      increment both pointers

    if both pointer reach the end, return true

  M = size of regex
  N = size of string
  
  O(N + M)
  
  O(1)

  '''
  
  reg_pointer = 0
  
  text_pointer = 0
  
  
  while reg_pointer < len(pattern) and text_pointer< len(text):
    
    if pattern[reg_pointer] == '.':
      reg_pointer+=1
      text_pointer+=1
    elif pattern[reg_pointer] == '*':

      # .*    **

      previous = pattern[reg_pointer-1]  
      if reg_pointer > 0 and previous != '.' and previous != '*':
        
        while text_pointer< len(text) and text[text_pointer] == previous:
          text_pointer += 1

        reg_pointer += 1

      else:
        raise Exception("This is not valid")
    
    if ( reg_pointer+2 < len(pattern) and  pattern[reg_pointer+1] == '*') and pattern[reg_pointer] != text[text_pointer]:
      reg_pointer += 2
      
    elif check_valid_char(pattern[reg_pointer])  and  check_valid_char(text[text_pointer]) and pattern[reg_pointer] == text[text_pointer] :

      reg_pointer += 1
      text_pointer += 1
      
    else:
      return False

  return reg_pointer == len(pattern) and text_pointer == len(text)
      
      
def check_valid_char(char):
  return ord('a') <=  ord(char) <=  ord('z') or ord('A') <=  ord(char) <=  ord('Z')
  

print(is_match("acd","ab*c."))



#pattern = ab*bb

#abbbbbbbb 



def regex_match(text, pattern ):
 return regex_match(text,pattern,0,0)

def regex_match(text, pattern, reg_pointer, text_pointer ):

 if reg_pointer == len(pattern) and text_pointer == len(text):
  return True

 if pattern[reg_pointer] == '.':
  return regex_match(text, pattern, reg_pointer+1, text_pointer+1 )

 elif reg_pointer+1 < len(pattern) and pattern[reg_pointer] == '*':
  
  for i in range(text_pointer, len(text)):
   if text[text_pointer] == pattern[reg_pointer+1]:
    if regex_match(text, pattern, reg_pointer+2, i ):
     return True
 elif text[text_pointer] == pattern[reg_pointer]:
  regex_match(text, pattern, reg_pointer+1, text_pointer+1 )

 return False

    if pattern[reg_pointer] == '.':
      reg_pointer+=1
      text_pointer+=1
    elif pattern[reg_pointer] == '*':

      # .*    **

      previous = pattern[reg_pointer-1]  
      if reg_pointer > 0 and previous != '.' and previous != '*':
        
        while text_pointer< len(text) and text[text_pointer] == previous:
          text_pointer += 1

        reg_pointer += 1

      else:
        raise Exception("This is not valid")
    
    if ( reg_pointer+2 < len(pattern) and  pattern[reg_pointer+1] == '*') and pattern[reg_pointer] != text[text_pointer]:
      reg_pointer += 2
      
    elif check_valid_char(pattern[reg_pointer])  and  check_valid_char(text[text_pointer]) and pattern[reg_pointer] == text[text_pointer] :

      reg_pointer += 1
      text_pointer += 1
      
    else:
      return False




def is_match(text, pattern):
  
  
  '''
  
  Regex (pattern) and a String (text)
  
  Does the Text match the regex?


  Approach 1:
  
  Use a Regex Library

  Approach 2:
  
  Double Pointer Loop
  
  1st pointer poins to the text
  2snd pointer points to the regex
    if the pointer is on a dot
      increment both pointers
      
    if the pointer is on wildcard
      increment the pointer while string pointer is on the previous letter

    otherwise if pointers point to the same character
      increment both pointers

    if both pointer reach the end, return true

  M = size of regex
  N = size of string
  
  O(N + M)
  
  O(1)

  '''

  #def regex_match(text, pattern ):
  return regex_match(text,pattern,0,0)

def regex_match(text, pattern, reg_pointer, text_pointer ):

  if reg_pointer == len(pattern) and text_pointer == len(text):
    return True
  
  if reg_pointer == len(pattern) or text_pointer == len(text):
    
    return False

  if pattern[reg_pointer] == '.':
    
    return regex_match(text, pattern, reg_pointer+1, text_pointer+1 )

  elif reg_pointer+1 < len(pattern) and pattern[reg_pointer+1] == '*':
    
    if regex_match(text, pattern, reg_pointer+2, text_pointer ):
      return True

    for i in range(text_pointer, len(text)):
      
      if text[i] == pattern[reg_pointer]:
      
        if regex_match(text, pattern, reg_pointer+2, i +1 ):
          return True
      else:
        break

  elif text[text_pointer] == pattern[reg_pointer]:
    return regex_match(text, pattern, reg_pointer+1, text_pointer+1 )

  return False

  '''
  reg_pointer = 0
  
  text_pointer = 0
  
  
  while reg_pointer < len(pattern) and text_pointer< len(text):
    
    if pattern[reg_pointer] == '.':
      reg_pointer+=1
      text_pointer+=1
    elif pattern[reg_pointer] == '*':

      # .*    **

      previous = pattern[reg_pointer-1]  
      if reg_pointer > 0 and previous != '.' and previous != '*':
        
        while text_pointer< len(text) and text[text_pointer] == previous:
          text_pointer += 1

        reg_pointer += 1

      else:
        raise Exception("This is not valid")
    
    if ( reg_pointer+2 < len(pattern) and  pattern[reg_pointer+1] == '*') and pattern[reg_pointer] != text[text_pointer]:
      reg_pointer += 2
      
    elif check_valid_char(pattern[reg_pointer])  and  check_valid_char(text[text_pointer]) and pattern[reg_pointer] == text[text_pointer] :

      reg_pointer += 1
      text_pointer += 1
      
    else:
      return False

  return reg_pointer == len(pattern) and text_pointer == len(text)
      
      
def check_valid_char(char):
  return ord('a') <=  ord(char) <=  ord('z') or ord('A') <=  ord(char) <=  ord('Z')
  

print(is_match("acd","ab*c."))



#pattern = ab*bb

#abbbbbbbb 

'''



def is_match(text, pattern):

  '''

  Regex (pattern) and a String (text)

  Does the Text match the regex?

  Approach 1:

  Use a Regex Library

  Approach 2:

  Double Pointer Loop

  1st pointer poins to the text
  2snd pointer points to the regex
    if the pointer is on a dot
      increment both pointers

    if the pointer is on wildcard
      increment the pointer while string pointer is on the previous letter

    otherwise if pointers point to the same character
      increment both pointers

    if both pointer reach the end, return true

  M = size of regex
  N = size of string

  O(N + M)

  O(1)

  '''

  return regex_match(text,pattern,0,0)

def regex_match(text, pattern, reg_pointer, text_pointer ):

  if reg_pointer == len(pattern) :
    if len(pattern) == 0 or text_pointer >= len(text):
      return True
    else:
      return False



  if reg_pointer+1 < len(pattern) and pattern[reg_pointer+1] == '*':

    if regex_match(text, pattern, reg_pointer+2, text_pointer ):
      return True

    for i in range(text_pointer, len(text)):

      if text[i] == pattern[reg_pointer] or '.' == pattern[reg_pointer] :

        if regex_match(text, pattern, reg_pointer+2, i +1 ):
          return True
      else:
        break

  elif pattern[reg_pointer] == '.':
    return regex_match(text, pattern, reg_pointer+1, text_pointer+1 )

  elif text[text_pointer] == pattern[reg_pointer]:
    return regex_match(text, pattern, reg_pointer+1, text_pointer+1 )

  return False

  '''
  reg_pointer = 0

  text_pointer = 0

  
  while reg_pointer < len(pattern) and text_pointer< len(text):
    
    if pattern[reg_pointer] == '.':
      reg_pointer+=1
      text_pointer+=1
    elif pattern[reg_pointer] == '*':

      # .*    **

      previous = pattern[reg_pointer-1]  
      if reg_pointer > 0 and previous != '.' and previous != '*':
        
        while text_pointer< len(text) and text[text_pointer] == previous:
          text_pointer += 1

        reg_pointer += 1

      else:
        raise Exception("This is not valid")
    
    if ( reg_pointer+2 < len(pattern) and  pattern[reg_pointer+1] == '*') and pattern[reg_pointer] != text[text_pointer]:
      reg_pointer += 2
      
    elif check_valid_char(pattern[reg_pointer])  and  check_valid_char(text[text_pointer]) and pattern[reg_pointer] == text[text_pointer] :

      reg_pointer += 1
      text_pointer += 1
      
    else:
      return False

  return reg_pointer == len(pattern) and text_pointer == len(text)
      
      
def check_valid_char(char):
  return ord('a') <=  ord(char) <=  ord('z') or ord('A') <=  ord(char) <=  ord('Z')



print(is_match("acd","ab*c."))



#pattern = ab*bb

#abbbbbbbb 

'''

