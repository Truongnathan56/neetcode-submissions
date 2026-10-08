class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        for(int i = 0; i < nums.size(); i++) {
            int difference = target - nums[i];
            if(hash.find(difference) != hash.end()) // If the differnce is found before the last term + 1
                return {hash[difference], i};
            hash[nums[i]] = i;
        }

        return {};
    }
};
