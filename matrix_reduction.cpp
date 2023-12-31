#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <set>
#include <algorithm>

using namespace std;
// defining picvot vector of the matrix
vector<int> pivot(const vector<vector<int>>& matrix, int row, int col) {
  std::vector<int> piv(col, 0);
  for (int j=0; j<col; j++) {
    piv[j] = 0;
  }
  for (int j=0; j<col; j++) {
    for (int i=0; i<row; i++) {
      if (matrix[i][j] != 0) {
        piv[j] = i+1;
      }
    }
  }
  return piv;
}

// constructing a vector of unique pivot elements
vector<int> unique_pivot(vector<int> w) {
  std::set<int> s(w.begin(), w.end());
  return vector<int>(s.begin(), s.end());
}

// constructing a vector of nonzero elements of the pivot 
std::vector<int> nonzero_pivot(const vector<int> w) {
  std::vector<int> nonzero_v;
  std::copy_if(w.begin(), w.end(), std::back_inserter(nonzero_v),
                 [](int element) { return element != 0; });
  return nonzero_v;
}

//column operation
std::vector<vector<int>> column_operation(vector<vector<int>> matrix, int row, int col) {
    for (int j=0; j<col; j++) {
      for (int k=0; k<j; k++) {
        if (pivot(matrix,row,col)[j] == pivot(matrix, row, col)[k] and pivot(matrix, row, col)[j] != 0) {
          for (int i=0; i< row; i++) {
            matrix[i][j] = (matrix[i][j] + matrix[i][k]) %2;
          }
        }
      }
    }
    return matrix;
    while (true) {
      column_operation(matrix, row, col);
      vector<int> v = pivot(matrix, row, col);
      if (nonzero_pivot(v).size() != unique_pivot(v).size()) {
        break;
    } 
  }
    return matrix;
  }

//matrix reduction (binary matrix) 
//vector<vector<int>> reduce(vector<vector<int>> matrix, int row, int col) {
  
//}

// main function
int main() {
  //creating matrix
  int row = 5;
  int col = 5;
  //random_device rd;
  unsigned seed = static_cast<unsigned>(chrono::system_clock::now().time_since_epoch().count());
  mt19937 gen(seed);
  uniform_int_distribution<> dist(0,1);
  vector<vector<int>> matrix(row, vector<int>(col));
  for (int i=0; i<row; i++) {
    for (int j=0; j<col; j++) {
      matrix[i][j] = dist(gen);
    }
  }

  //printing the matrix
  for (int i=0; i<row; i++) {
    for (int j=0; j<col; j++) {
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }
  cout << "===========";
  cout << endl;
  for (int j=0; j<col; j++) {
    cout << pivot(matrix, row, col)[j] << " ";
  }
  cout << endl;
 vector<int> w = pivot(matrix, row, col);
 vector<int> u = unique_pivot(w);
 int n = u.size();
 for (int j=0; j<n; j++) {
  cout << u[j] << " ";
 }
cout << endl;
cout << "===============";
cout << endl << "reduced matrix: ";
cout << endl;
 //printing reduced matrix
 for (int i=0; i<row; i++) {
    for (int j=0; j<col; j++) {
      cout << column_operation(matrix, row, col)[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}