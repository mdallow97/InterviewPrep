// assignCookies.cpp

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int count = 0;
        bool flag = false;
        
        sort(s.begin(), s.end());
        sort(g.begin(), g.end());
        
        for (auto child : g) {
            flag = true;
            for (int i = 0; i < s.size(); i++) {
                if (s[i] >= child) {
                    count++;
                    s.erase(s.begin() + i);
                    flag = false;
                    break;
                }
            }
            
            if (flag)
                break;
        }
        
        return count;
    }
};