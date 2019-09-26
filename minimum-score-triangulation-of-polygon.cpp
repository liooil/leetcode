#include <string>
#include <vector>

using namespace std;

// =============================================================================

class Solution {
public:
    int minScoreTriangulation(vector<int>& A) {
        const int N = A.size();
        // DP[0:N-1] = min(
        //    A[0]*A[N-1]*A[k] + DP[0:k] + DP[k:N-1]
        //    for k in range(1, N-1))
        vector<vector<int>> DP(N, vector<int>(N, -1));

        for (int end=2; end<N; end++) {
            for (int start=end-1; start>=0; start--) {
                for (int k = start+1; k<end; k++) {
                    const int dp_local = A[start] * A[end] * A[k] + DP[start][k] + DP[k][end];
                    if ((DP[start][end] == -1) || (dp_local < DP[start][end])) {
                        DP[start][end] = dp_local;
                    }
                }
            }
        }
        return DP[0][N-1];
    }
};

// =============================================================================

#include <iostream>

int main() {
    Solution s;
    vector<int> A{1, 2, 3};
    cout << s.minScoreTriangulation(A) << endl;
    return 0;
}
