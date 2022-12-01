from collections import deque


def shortestWordEditPath(source, target, words):
  """
	@param source: str
	@param target: str
	@param words: str[]
	@return: int
	

	#pass #your code goes here

  #mohamed_sayed codeforces 

  
  #Graph

  #https://codeforces.com/profile/Mohamed_Sayed

  

  
  Graph
  
  Search From source to Target
  
  1. Create the Graph
  2. BFS , DFS (BFS will be faster). When we find the word, we return
  3. return -1 if we finish the BFS
  
  bit
  
  *it -> bit
  
  b*t -> bit
  
  bi* -> bit

  N words N words
  W is the size of the words (e.g. bit has 3 characters)

  time O(N*W)
  space O(N*W)

  
  """

  G = {}

  for word in words:
    
    for i,l in enumerate(word):
      
      new = create_word(word,i)

      if new not in G:
        G[new] = []
      
      G.get(new).append(word)

  counter = 0
  
  #q = deque()
  
  q = []
  
  q.append(source)
  
  visited = set()
 
  index = 0
  
  while q:
    
    for _ in q:
      
      word = q[0]
      #index += 1

      q = q[1:]
      
      if word == target:
        return counter

      visited.add(word)

      for i,l in enumerate(word):
        # 0 1 2 ...
        
        new = create_word(word,i)
        
        if new in G:

          for full_word in G[new]:
            if full_word not in visited:
              q.append(full_word)

    counter += 1

  return -1

def create_word(word,i):
  return word[0:i] + '*' + word[i+1:]

  
  #McGill Canada