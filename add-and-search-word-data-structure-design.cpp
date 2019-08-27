#include <string>
#include <vector>

using namespace std;

// =====================================================================================================================

struct Trie {
    string str;
    vector<Trie*> children;
};

class WordDictionary {
public:
    /** Initialize your data structure here. */
    WordDictionary() :
        root{"", {}} {
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        if (word.empty()) return this->Found;
        if (word[0] == '.') {
            for (WordDictionary* child : this->Child) {
                if (child == nullptr) continue;
                if (child->search(word.substr(1))) return true;
            }
        } else {
            unsigned int index = static_cast<unsigned int>(word[0] - 'a');
            if (this->Child[index] == nullptr) return false;
            return this->Child[index]->search(word.substr(1));
        }
        return false;
    }
private:
    Trie root;
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */