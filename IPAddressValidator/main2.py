import unittest

def validateIP(ip):
  """

  Validate the IP address

  Approach 1: Split and validate number

  Check if characters are number
  Check if number is between 0 and 255

  Return True

  runtime: O(1) O(12)
  spacetime: O (1)

  @param ip: str
  @return: bool
  """
  # check if the size is greater than 15
  # 255.255.255.255 is the max size
  if len(ip) > 15:
    return False

  #create a list of ips
  # [ '192', '168', '0', '1' ]
  ip_split_dot = ip.split('.')

  # we should have 4 numbers
  # size == 4
  if len(ip_split_dot) != 4:
    return False

  # check if all the ip are numbers
  #1 9 2  1 6 8  0 1
  if not all([  char.isdigit() for ip_raw in ip_split_dot for char in ip_raw  ]):
    return False

  # check if numbers are between 0 and 255
  # used to be a string, make it a integer
  if not all( [ ip and 0 <= int(ip) <= 255 for ip in ip_split_dot ]):
    return False

  return True


class TestValidateIP(unittest.TestCase):
  
  def test_larger(self):
    #Arrage
    ip = '192.168.123.456'
    
    #Act
    result = validateIP(ip)
    
    #Assert
    self.assertEquals(result, False)
  
  def test_ok(self):
    #Arrage
    ip = '192.168.123.255'
    
    #Act
    result = validateIP(ip)
    
    #Assert
    self.assertEquals(result, True)
  
  def test_zero(self):
    #Arrage
    ip = '0.0.0.0'
    
    #Act
    result = validateIP(ip)
    
    #Assert
    self.assertEquals(result, True)
  
  def test_zero(self):
    #Arrage
    ip = '0.0.0.0'

    #Act
    result = validateIP(ip)

    #Assert
    self.assertEquals(result, True)

  def test_bad(self):
    #Arrage
    ip = '0.0.0'

    #Act
    result = validateIP(ip)

    #Assert
    self.assertEquals(result, False)



#unittest.main(verbosity=2)
  
  
	
