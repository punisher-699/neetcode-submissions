class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int *start = numbers.data(), *end = numbers.data() + numbers.size() - 1;

        while (start < end){
            int sum = *start + *end;
            
            if (sum == target){
                return {int(start - numbers.data() + 1), int(end - numbers.data() + 1)};
            }

            if (sum > target) end--;
            else start++;
        }
        return {};
    }
};
