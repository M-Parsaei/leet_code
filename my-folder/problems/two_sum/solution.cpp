class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sol(2);
        bool isDone = false;
        int arrSize = nums.size();
        for(int i=0;i<arrSize;i++){
            for(int j=i+1;j<arrSize;j++){
                if((nums[i]+nums[j]) == target){
                    sol[0]=i;
                    sol[1]=j;
                    isDone = true;
                    break;
                }
            }
            if(isDone){
                break;
            }
        }
        return sol;
    }
};