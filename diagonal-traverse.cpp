#include <vector>
#include <exception>

using namespace std;

// =============================================================================

enum class Direct : int {
    RightUp,
    LeftDown
};

struct RightException : exception {};
struct LeftException : exception {};
struct UpException : exception {};
struct DownException : exception {};

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        this->M = matrix.size();
        if (this->M == 0) return result;
        this->N = matrix[0].size();
        if (this->N == 0) return result;
        result.push_back(matrix[0][0]);
        while (this->traverse()) {
            result.push_back(matrix[this->R][this->C]);
        }
        return result;
    }
private:
    size_t R = 0ul; // Row Number, {+: Down, -: Up}
    size_t C = 0ul; // Col Number, {+: Right,  -: Left}
    Direct D = Direct::RightUp; // Direction
    size_t M; // Maximum Row
    size_t N; // Maximum Col
    void goUp() {
        if (this->R == 0) throw UpException();
        this->R--;
    }
    void goDown() {
        if (this->R+1 == M) throw DownException();
        this->R++;
    }
    void goRight() {
        if (this->C+1 == this->N) throw RightException();
        this->C++;
    }
    void goLeft() {
        if (this->C == 0) throw LeftException();
        this->C--;
    }
    void goBack() {
        if (this->D == Direct::RightUp) {
            this->D = Direct::LeftDown;
        } else {
            this->D = Direct::RightUp;
        }
    }
    bool traverse() {
        switch (this->D)
        {
        case Direct::RightUp:
            try {
                this->goRight();
                this->goUp();
                return true;
            } catch (const RightException& e) {
                try {
                    this->goDown();
                    this->goBack();
                    return true;
                } catch (const DownException& e) {
                    return false;
                }
            } catch (const UpException& e) {
                try {
                    this->goBack();
                    return true;
                } catch (const RightException& e) {
                    return false;
                }
            }
            break;
        case Direct::LeftDown:
            try {
                this->goDown();
                this->goLeft();
                return true;
            } catch (const DownException& e) {
                try {
                    this->goRight();
                    this->goBack();
                    return true;
                } catch (const RightException& e) {
                    return false;
                }
            } catch (const LeftException& e) {
                try {
                    this->goBack();
                    return true;
                } catch (const DownException& e) {
                    return false;
                }
            }
            break;
        }
        return false;
    }
};