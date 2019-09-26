#include <cstddef>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// =============================================================================

class Solution {
public:
    int rob(TreeNode* root) {
        if (root == NULL) return 0;
        int planA, planB;
        this->robPlans(root, planA, planB);
        return planA;
    }
    // planA: Rob root
    // planB: Do not Rob root
    void robPlans(TreeNode* root, int& planA, int& planB) {
        int planLeftA, planLeftB, planRightA, planRightB;
        if (root->left != NULL) {
            robPlans(root->left, planLeftA, planLeftB);
        } else {
            planLeftA = planLeftB = 0;
        }
        if (root->right != NULL) {
            robPlans(root->right, planRightA, planRightB);
        } else {
            planRightA = planRightB = 0;
        }
        planA = planLeftB + planRightB + root->val;
        planB = planLeftA + planRightA;
        if (planA < planB) {
            planA = planB;
        }
    }
};