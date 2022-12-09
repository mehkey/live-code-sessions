#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<vector<int>> findPairsWithGivenDifference( const vector<int>& arr, int k) 
{
  set<int> unique_numbers;
  
  for (auto &x : arr ){
    unique_numbers.insert(x);
  }

  vector<vector<int>> result;

  for (auto &number : arr){

    if ( unique_numbers.find(number + k)  != unique_numbers.end()){
      vector<int> ans ({ number + k,number});
      result.push_back(ans);
    }
  }
  return result;
}

int main() {
  return 0;
}