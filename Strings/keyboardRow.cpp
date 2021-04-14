// keyboardRow.cpp

class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        // Use a dict to map keyboard keys to a row for fast access
        unordered_map<int, vector<char>> location = 
        {
            {0, {'q','w','e','r','t','y','u','i','o','p'}},
            {1, {'a','s','d','f','g','h','j','k','l'}},
            {2, {'z','x','c','v','b','n','m'}}
        };
        
        vector<string> output;
        for (auto word : words)
        {
            // Find keyboard row
            int row = -1;
            string valid_word;
            for (auto key : location) {
                for (auto letter : key.second) {
                    if (letter == (char) tolower(word[0])) {
                        row = key.first;
                        break;
                    }
                }
                if (row != -1)
                    break;
            }
            
            // Determine whether all letters in word fall on same keyboard row
            for (auto letter : word) {
                bool found = false;
                for (auto valid_letter : location[row]) {
                    if (valid_letter == (char) tolower(letter)) {
                        found = true;
                        valid_word.push_back(letter);
                    }
                }
                
                if (!found)
                    break;
            }
            
            // Simple way to detect if word is valid, may take up unnecessary memory
            if (valid_word.size() == word.size()) {
                output.push_back(word);
                valid_word = "";
            }
        }
        
        return output;
    }
};