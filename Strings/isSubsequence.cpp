// isSubsequence.cpp

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
};