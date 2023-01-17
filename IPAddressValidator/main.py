def validateIP(ip):
  """

  Split

  check if the size of the split array is 4

  check if the characters are between 0-9

  convert the string to int

  check if the integer is between 0 and 256

  return true

  time:O(N)
  space:O(1)

  @param ip: str
  @return: bool
  """
  
  #ip_array = ip.split('.')
  
  dots = 0
  
  i = 0
  
  while i <len(ip):
    j = i
    arr =[]
    while j < len(ip) and ip[j] != '.':
      if not (ord('0') <= ord(ip[j]) <= ord('9')):
        return False

      arr.append(ip[j])
      j += 1

    dots += 1
      
    num = ''.join(arr)
    
    if not num:
      return False
    
    if not 0<= int(num) <= 255:
      return False
    
    i = j +1

  if dots != 4:
    return False
  
  
  return True
    
    
  '''
  if len(ip_array) != 4:
    return False

  try:
    if(not all([ 0<= int(i) <= 255 for i in ip_array])):
      return False
  except ValueError:
    return False
  
  
  
  
  
  return True
  '''

print(validateIP('192.168.0.1'))

print(validateIP('192.oops.0.1'))

print(validateIP('192.168.123.456'))

print(validateIP('123.24.59.99'))

print(validateIP('123.24.59.'))




'''
try:
  ip_number_array = [int(i) for i in ip_array]
except ValueError:
  return False


for i in range(4):
  if 0 > ip_number_array > 255:
    return False


'''
  