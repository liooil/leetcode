#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

// ============================================================================

class Solution {
public:
    // ========================================================================
    // Induction: minCut(s) = min(minCut(s[n])+1 if s[n:] is palindrome)
    int minCut(string s) {
        const int N = s.size();
        // DP[n] means minCut(s[:n])
        vector<int> DP(N+1, -1);
        // pldCache stores starts that can form palidrome s[start:end+1],
        // if s[start] == s[end]
        stack<int> pldCache;
        pldCache.push(0);
        for (int end = 0; end < N; end++) {
            DP[end+1] = DP[end]+1;
            stack<int> pldCacheNew;
            while (!pldCache.empty()) {
                const int start = pldCache.top();
                pldCache.pop();
                if (s[start] == s[end]) {
                    if (DP[start]+1 < DP[end+1]) {
                        DP[end+1] = DP[start]+1;
                    }
                    // If and only if s[start:end+1] is palindrome,
                    // s[start-1:end+2] could be palindrome
                    if (start > 0) {
                        pldCacheNew.push(start-1);
                    }
                }
            }
            pldCache = pldCacheNew;
            // s[end+1:end+1] is always a palindrome (empty)
            pldCache.push(end);
            if (end > 0) {
                // s[end:end+1] is palindrome (single char)
                pldCache.push(end-1);
            }
        }
        return DP[N];
    }
};

// ============================================================================

int main() {
    Solution s;
    cout << s.minCut("aab") << endl;
    return 0;
}
