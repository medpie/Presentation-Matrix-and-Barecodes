#pragma once

using namespace std;

vector<vector<int>> random_matrix(int row, int col);
vector<int> pivot(const vector<vector<int>>& matrix, int row, int col);
vector<int> unique_pivot(vector<int> w);
vector<int> nonzero_pivot(const vector<int> w);
vector<vector<int>> column_operation(vector<vector<int>> matrix, int row, int col);
vector<std::pair<int, int>> barcode(vector<vector<int>> matrix, int row, int col);
vector<vector<int>> simplices(vector<vector<int>> scomplex);


