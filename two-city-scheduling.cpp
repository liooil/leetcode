#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// =====================================================================================================================

class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        const int N = costs.size()/2;
        nth_element(costs.begin(), costs.begin()+N, costs.end(), [](vector<int>& lhs, vector<int>& rhs){
            return ((lhs[1]-lhs[0]) < (rhs[1]-rhs[0]));
        });
        int costTotal = 0;
        for (size_t i = 0; i < N; i++) {
            costTotal += costs[i][1] + costs[i+N][0];
        }
        return costTotal;
    }
};

// =====================================================================================================================

int main() {
    Solution s = Solution();
    vector<vector<int>> costs = {
        {259, 700},
        {448,54},
        {926,667},
        {184,139},
        {840,118},
        {577,469}
    };
    cout << s.twoCitySchedCost(costs) << endl;
    return 0;
}

