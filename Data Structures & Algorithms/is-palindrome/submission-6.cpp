class Solution {
public:
    bool isPalindrome(string s) {
        char *st = s.data();
        char *end = s.data() + s.length() - 1;

        while (st < end) {

            while (st < end && !isalnum(*st))
                st++;

            while (st < end && !isalnum(*end))
                end--;

            if (tolower(*st) != tolower(*end))
                return false;

            st++;
            end--;
        }

        return true;
    }
};