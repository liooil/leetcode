#include <cstddef>
#include <stack>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode * left;
    TreeNode * right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// =============================================================================

class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        if (root != NULL) {
            this->bstToGst(root->right);
            root->val = sum += root->val;
            this->bstToGst(root->left);
        }
        return root;
    }
private:
    int sum = 0;
};