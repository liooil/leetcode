#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// =============================================================================

class Solution {
public:
    int smallestRangeII(vector<int>& A, int K) {
        std::sort(A.begin(), A.end());
        int range = A[A.size()-1] - A[0];
        for (int i = 0; i < A.size(); i++) {
            // Add 2*K to A[:i]
            int A_High = A[A.size()-1];
            if (A[i] + 2*K > A[A.size()-1]) {
                A_High = A[i] + 2*K;
            }
            int A_Low = A[0] + 2*K;
            if ((i+1 < A.size()) && (A[i+1] < A_Low)) {
                A_Low = A[i+1];
            }
            if (A_High - A_Low < range) {
                range = A_High - A_Low;
            }
        }
        return range;
    }
};

// =============================================================================

int main() {
    vector<int> A = {0, 10};
    int K = 2;
    Solution s;
    printf("Result: %d\n", s.smallestRangeII(A, K));
}