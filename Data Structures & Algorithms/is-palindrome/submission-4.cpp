class Solution {
public:
    bool isPalindrome(string s) {
        char * st = s, *end = s + strlen(s) - 1;

        while (st < end){
            if( tolower(*st) != tolower(*end)){
                return false;
            }
            st++; end--;
        }
        return true;
    }
};
