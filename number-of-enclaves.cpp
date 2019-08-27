#include <iostream>
#include <vector>
#include <stack>
#include <tuple>
#include <set>

using namespace std;

///////////////////////////////////////////////////////////////////////////////

struct Pos {
    const int x;
    const int y;
};

class Solution {
public:
    int numEnclaves(vector<vector<int>>& A) {
        int m = A.size();
        int n = (A.size() > 0) ? A[0].size() : 0;
        stack<Pos> boundaryStack;
        for (int x=0; x<m; ++x) {
            if (A[x][0] == 1) {
                A[x][0] = 0;
                boundaryStack.emplace(Pos{x, 0});
            }
            if (A[x][n-1] == 1) {
                A[x][n-1] = 0;
                boundaryStack.emplace(Pos{x, n-1});
            }
        }
        for (int y=0; y<n; ++y) {
            if (A[0][y] == 1) {
                A[0][y] = 0;
                boundaryStack.emplace(Pos{0, y});
            }
            if (A[m-1][y] == 1) {
                A[m-1][y] = 0;
                boundaryStack.emplace(Pos{m-1, y});
            }
        }

        while (!boundaryStack.empty()) {
            Pos pos = boundaryStack.top();
            boundaryStack.pop();
            vector<Pos> neighbours = {};
            if ((pos.x-1>=0) && (A[pos.x-1][pos.y] == 1)) {
                A[pos.x-1][pos.y] = 0;
                boundaryStack.emplace(Pos{pos.x-1,pos.y});
            }
            if ((pos.x+1<m) && (A[pos.x+1][pos.y] == 1)) {
                A[pos.x+1][pos.y] = 0;
                boundaryStack.emplace(Pos{pos.x+1,pos.y});
            }
            if ((pos.y-1>=0) && (A[pos.x][pos.y-1] == 1)) {
                A[pos.x][pos.y-1] = 0;
                boundaryStack.emplace(Pos{pos.x,pos.y-1});
            }
            if ((pos.y+1<n) && (A[pos.x][pos.y+1] == 1)) {
                A[pos.x][pos.y+1] = 0;
                boundaryStack.emplace(Pos{pos.x,pos.y+1});
            }
        }
        int result = 0;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                result += A[i][j];
            }
        }
        return result;
    }
};