import java.io.*;
import java.util.*;

class Solution {

  static int getNumberOfIslands(int[][] binaryMatrix) {
    
    int total = 0;

    for (int i = 0; i < binaryMatrix.length;i++){
      for (int j =0; j< binaryMatrix[0].length;j++){
        if (binaryMatrix[i][j] == 1){
          dfs(binaryMatrix,i,j);
          total++;
        }
      }
    }
    
    return total;
    
  }
  
  static void dfs(int[][] binaryMatrix,int i, int j) {
    binaryMatrix[i][j] = -1;
    if (valid(binaryMatrix, i+1,j)) {
      dfs(binaryMatrix,i+1,j);
    }
    if (valid(binaryMatrix, i,j+1)){
      dfs(binaryMatrix,i,j+1);
    }
    if (valid(binaryMatrix, i-1,j)){
      dfs(binaryMatrix,i-1,j);
    }
    if (valid(binaryMatrix, i,j-1)){
      dfs(binaryMatrix,i,j-1);
    }
  }

  static boolean valid(int[][] binaryMatrix , int x, int y){
    int rows = binaryMatrix.length;
    int cols = binaryMatrix[0].length;

    if (x >= 0 && x < rows && y >= 0 && y < cols && binaryMatrix[x][y] == 1){
      return true;
    }
    return false;
  }

  public static void main(String[] args) {

  }

}