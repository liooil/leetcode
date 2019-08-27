#include <string>
#include <vector>

using namespace std;

// =============================================================================

class Solution {
public:
    int minScoreTriangulation(vector<int>& A) {
        const int N = A.size();
        // DP[dp_size][i] is answer for minScoreTriangulation(A[i:i+dp_size]) (i+dp_size=<N)
        // DP[dp_size][i] = min(
        //  A[i]*A[i+1]*A[k] + DP[][i+1]+DP[dp_size-k][k]
        //  for k in range(i+2, i+dp_size))
        vector<vector<int>> DP;
        for (int dp_size=3; dp_size<N; ++dp_size) {
            for (int k=2; k<N; ++k) {
                int dp = A[
            }
        }
    }
};