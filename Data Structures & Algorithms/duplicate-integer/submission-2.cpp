class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> hset;

        for (auto num : nums){
            if( hset.count(num))
                return !false;
            hset.insert(num);
        }
        return !true;
    }
};