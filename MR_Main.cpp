#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <set>
#include <algorithm>
#include <fstream>
#include <utility>
#include <limits>
#include "mr_functions.cpp"

using namespace std;
//===================================================================================
//=======================================Main========================================
//===================================================================================

int main() {
  //creating matrix
  int row = 10;
  int col = 10;

// the matrix
vector<vector<int>> matrix = random_matrix(row, col);

// an alternate way of giving a matrix of data
/* vector<vector<int>> myList = {{1,0,1}, {1,1,1}, {0,0,1}};
vector<vector<int>> matrix(myList.size(), vector<int>(myList[0].size()));
for (int i=0; i < myList.size(); i++) {
  for (int j=0; j < myList[0].size(); j++) {
    matrix[i][j] = myList[i][j];
  }
}
*/

  std::ofstream outputFile("D://b.txt");

   if (!outputFile.is_open()) {
        return 1; // return an error code
    }

  //printing the matrix
  for (int i=0; i<row; i++) {
    for (int j=0; j<col; j++) {
      cout << matrix[i][j] << " ";
      outputFile << matrix[i][j] << " ";
    }
    cout << endl;
    outputFile << endl;
  }
  cout << "===========" << endl;
  outputFile << "===========" << endl;
  for (int j=0; j<col; j++) {
    cout << pivot(matrix, row, col)[j] << " ";
    outputFile << pivot(matrix, row, col)[j] << " ";
  }
  cout << endl;
  outputFile << endl;
 vector<int> w = pivot(matrix, row, col);
 vector<int> u = unique_pivot(w);
 int n = u.size();
 cout << "pivot without multiplicity: " << endl;
 outputFile << "pivot without multiplicity: " << endl;
 for (int j=0; j<n; j++) {
  cout << u[j] << " ";
  outputFile << u[j] << " ";
 }
cout << endl;
outputFile << endl;
cout << "===============";
outputFile << "===============";
cout << endl << "reduced matrix: ";
outputFile << endl << "reduced matrix: ";
cout << endl;
outputFile << endl;
 //printing reduced matrix
 for (int i=0; i<row; i++) {
    for (int j=0; j<col; j++) {
      cout << column_operation(matrix, row, col)[i][j] << " ";
      outputFile << column_operation(matrix, row, col)[i][j] << " ";
    }
    cout << endl;
    outputFile << endl;
  }

// printing barcodes
cout << endl;
cout << "======  barcodes:" << endl;
outputFile << endl; 
outputFile << "======= barcodes:" << endl;
cout << "{";
outputFile << "{";
std::vector<std::pair<int, int>> results = barcode(matrix, row, col);
for (const auto& pair : results) {
  cout << "[" << pair.first << "," << pair.second << ")";
  if (&pair != &results.back()) {
    cout << ", ";
  }
  outputFile << "[" << pair.first << "," << pair.second << ")";
  if (&pair != &results.back()) {
    outputFile << ", ";
  }
}
cout << "}";
outputFile << "}";
  outputFile.close();
  return 0;
}