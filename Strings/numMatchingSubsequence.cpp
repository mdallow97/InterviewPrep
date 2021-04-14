// numMatchingSubsequence.cpp

class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.size() > t.size())
            return false;
            
        int i = 0;
        while ((i < t.size()) && (s.size() > 0)) {
            if (t[i] == s[0]) {
                s.erase(s.begin());
            }
            i++;
        }
        
        if (s.size() == 0)
            return true;
        else return false;
    }
    
    int numMatchingSubseq(string s, vector<string>& words) {
        int count = 0;
        unordered_map<string, bool> knownSequence;
        
        for (auto word : words) {
            if (knownSequence.find(word) != knownSequence.end()) {
                if (knownSequence[word])
                    count ++;
                continue;
            }
            
            bool isSequence = isSubsequence(word, s);
            pair<string, bool> newSequence (word, isSequence);
            knownSequence.insert(newSequence);
            
            if (knownSequence[word])
                count ++;
        }
        return count;
    }
};