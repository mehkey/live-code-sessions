from collections import Counter
from collections import defaultdict

def word_count_engine(document):
  
  
  '''
  
  Sort and Count
  
  1_ Find all the words
  
  2_ Cleanup the words
  
  3_ Counting
  
  4_ Create response
  
  5_ Sorting
  
  6_ Create a HM
  
  
  
  N Characters
  
  M words
  
  Runtime: O(M log M + N)
  
  Space: O(N)
  
  '''
  
  #1_ Find all the words
  
  raw_words = document.split(' ')
  
  #stores the first positon of the word
  word_pos = defaultdict(int)
  
  #2_ Cleanup the words 
  #create an empty List of size raw_words
  clean_words = [None]*len((raw_words))
  
  for i,word in enumerate(raw_words):
    clean_words[i] = ''.join([letter.lower() for letter in word if letter.isalnum()])
    if clean_words[i] not in word_pos:
      word_pos[clean_words[i]] = i
      

  #3_ Counting counter
  word_counter = Counter(clean_words)
  
  #print(word_counter)

  
  #4_ Create response and remove space
  
  raw_output = [[key,word_counter[key],word_pos[key]] for key in word_counter if key != '']#[None] * len(word_counter)
  
  
  #sort frist based on Count, Second based on Postion in word
  def compare_words(word):
    return (-word[1],word[2])
  
  #5_ Sorting
  raw_output = sorted(raw_response, key=compare_words)

  # remove the last integer an return it
  return [[word[0],str(word[1])] for word in raw_output]

print(word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!"))
    