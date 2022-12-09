#include <iostream>
#include <string>
#include <stack>
using namespace std;

int bracketMatch( const string& text ) 
{
  if(text.size() == 0)
    return 0;
  
  int openBracketCount = 0;
  int closingBracket = 0;
  
  for(auto each : text)
  {
    if(each == '(')
    {
      ++openBracketCount;
    }
    else if(each == ')')
    {
      if(openBracketCount > 0)
      {

        --openBracketCount;        
      }
      else 
      {
        closingBracket++;
      }
    }
  }
  return openBracketCount + closingBracket;
}

int main() {
  
  
  return 0;
}

/*
1. As I come across openiing - push into stack - increment count

2. come across closing - pop from stack - decrement count

3. end of string - stack size - 
 

O(N)

O(N)



*/