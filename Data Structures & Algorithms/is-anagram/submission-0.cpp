class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> count;
        if(s.length() != t.length())
            return false;
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            count[c] = count[c] + 1;
        }

        for (int j = 0; j < t.length(); j++) {
            char c = t[j];
            count[c] = count[c] - 1;

            if (count[c] < 0) {
                return false;
            }
        }

        return true;        

    }
};
