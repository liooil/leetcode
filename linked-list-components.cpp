#include <vector>
#include <set>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// =============================================================================

class Solution {
public:
    int numComponents(ListNode* head, vector<int>& G) {
        set<int> S;
        for (int d : G) {
            S.insert(d);
        }
        bool PrevInside = false;
        int num = 0;
        while (head != nullptr) {
            if (S.find(head->val) == S.end()) {
                PrevInside = false;
            } else {
                if (!PrevInside) {
                    num++;
                }
                PrevInside = true;
            }
            head = head->next;
        }
        return num;
    }
};