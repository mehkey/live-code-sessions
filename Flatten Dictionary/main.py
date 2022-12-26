from collections import defaultdict


def flatten_dictionary_recursive(dictionary, result, stack):

  if not dictionary:
    return

  for key,value in dictionary.items():

    if key != '':
      stack.append(key)

    if isinstance(value,str) or isinstance(value,int): 
      result['.'.join(stack)] =  value

    elif isinstance(value,dict) :
      flatten_dictionary_recursive(value,result,stack)

    if key != '':
      stack.pop()

def flatten_dictionary(dictionary):

  '''
  
  Approach 1:
  
  Use a stack to keep track of the level
  
  Use a recursive approach
  
  If value is number or string, add to the result,
  
  Otherwise, call recursively
  
  Keep a result array and pass around the array
  
  
  LEVEL 1: Key1, Key2
  
  LEVEL 2: a,b,c
  
  LEVEL 3: d,e
  
  
  "Key1" : "1",
  "Key2" : {
      "a" : "2",
      "b" : "3",
      "c" : {
          "d" : "3",
          "e" : {
              "" : "1"
          }
      }
  }
         


  time O(N)
  
  space O(N)

  '''

  if not dictionary:
    return {}

  res ={}

  stack = []

  flatten_dictionary_recursive(dictionary,res, stack)

  return res

'''
stack = ['Key2', 'a']

"Key1" : "1", 
"Key2.a": "2",
...
"Key2.c.d": "3",
...
"Key2.c.e.": "1",

test = { 
            
            "Key2" : { 
                "a" : "2", 
                "b" : "3", 
                "c" : { 
                    "d" : "3", 
                    "e" : { 
                        "" : "1" 
                    }
                }
            },
  "Key1" : "1"
        }
#print(flatten_dictionary(test))

'''