class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();
        int st = 0 , end = n-1;
        if(n == 1) return nums[st];
        if(nums[st] != nums[st+1]) return nums[st];
        if(nums[end] != nums[end-1]) return nums[end];

        
        while(st<=end){
            int mid = st + (end-st)/2;

            if(nums[mid-1] != nums[mid] && nums[mid] != nums[mid+1]){
                return nums[mid];
            }

            if(mid%2==1){//even
                if(nums[mid-1] == nums[mid]){
                    st = mid+1;
                }

                else{
                    end = mid-1;
                }
            }

            else{//odd
                if(nums[mid-1] == nums[mid]){
                    end = mid - 1;
                }

                else{
                    st = mid+1;
                }
            }
        }
        return -1;
    }
};