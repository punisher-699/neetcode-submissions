class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        unordered_map<int, char> sht, tht;
        for(int i = 0 ; i < s.length() ; i++){
            sht[s[i]]++;
            tht[t[i]]++;
        }
        return sht == tht;
    }
};
