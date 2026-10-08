class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> numbers;
        for(int i = 0; i < nums.size(); i++) {
            if (numbers.find(nums[i]) != numbers.end()) {
                return true;
            }

            numbers.insert({nums[i], i});
        }
        return false;
    }
};