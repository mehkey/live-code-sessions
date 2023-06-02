import unittest

def diffBetweenTwoStrings(source, target):
  """
  @param source: str
  @param target: str
  @return: str[]
  
        source = "ABCDEFG"
      target = "ABDFFGH"
      answer = ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"]
      
      We want the minimum answer
      
      
      Approach DP: Dynamic programming
      
      Step 1: Find the DP minimum starting at index sourcePointer and targetPointer
      
      Step 2: Reconstruct the minimum string starting at 0,0
      
      source = "ABCDEFG"
      target = "ABDFFGH"
      
      
      dp(0,0) = 9
      
      sourcePointer = 2
      targetPointer = 2
      
      if same letter
      answer = ['A', 'B', '-C', ...]
      
      answer = ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"]
      
      
  """
  
  diff = DiffBetweenTwoStrings()
  
  return diff.diff_between_two_strings(source,target)


class DiffBetweenTwoStrings:
  
  def diff_between_two_strings(self,source,target):
    self.source = source
    self.target = target
    self.len_source = len(source)
    self.len_target = len(target)
    self.dp_memo = {}
    
    source_pointer = 0
    target_pointer = 0
    
    result = []
    
    #print(self.len_source, self.len_target)
    
    while source_pointer < self.len_source and target_pointer < self.len_target:
      
      if self.source[source_pointer] == self.target[target_pointer]:
        result.append(self.source[source_pointer])
        source_pointer += 1
        target_pointer += 1
      elif self.dp_min_difference(source_pointer+1, target_pointer) <= self.dp_min_difference(source_pointer, target_pointer+1):

        result.append("".join(['-',self.source[source_pointer]]))
        source_pointer += 1
      else:
        result.append("".join(['+',self.target[target_pointer]]))
        target_pointer += 1
    
    while source_pointer < self.len_source:
      result.append("".join(['-',self.source[source_pointer]]))
      source_pointer += 1
    
    while target_pointer < self.len_target:
      result.append("".join(['+',self.target[target_pointer]]))
      target_pointer += 1
    
    
    return result
      
      
  
  def dp_min_difference(self,source_pointer,target_pointer):

    if (source_pointer,target_pointer) in self.dp_memo:
      return self.dp_memo[(source_pointer,target_pointer)]
    #print(source_pointer, target_pointer)
    #base case
    if source_pointer == self.len_source:
      return self.len_target - target_pointer
    
    if target_pointer == self.len_target:
      return self.len_source - source_pointer

    # A == A
    if self.source[source_pointer] == self.target[target_pointer]:
      result = self.dp_min_difference(source_pointer+1,target_pointer+1) + 1
      
      self.dp_memo[(source_pointer,target_pointer)] = result 
      return result

    # A != B
    result = min( self.dp_min_difference(source_pointer,target_pointer + 1) + 1, self.dp_min_difference(source_pointer+1,target_pointer) + 1)
    self.dp_memo[(source_pointer,target_pointer)] = result 
    
    return result


class TestDiffBetweenTwoStrings(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.diff = DiffBetweenTwoStrings()
    
  def test_Standard_Case(self):
    source = "ABCDEFG"
    target = "ABDFFGH"
    self.assertEquals( self.diff.diff_between_two_strings(source,target),["A","B","-C","D","-E","F","+F","G","+H"]) 
  
  def test_Standard_Case2(self):
    source = "ABCDEFG"
    target = "ABDFFGH"
    self.assertEqual( self.diff.diff_between_two_strings(source,target),["A","B","-C","D","-E","F","+F","G","+H"]) 

unittest.main(verbosity=2)
