class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        vector<int> ht(26, 0);
        for (int i = 0 ; i < s.length() ; i++){
            ht[s[i] - 'a']++;
            ht[t[i] - 'a']--;
        }

        for (int val : ht)
            if (val != 0)
                return false;
        return true;
    }
};
