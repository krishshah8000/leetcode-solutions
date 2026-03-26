class Solution {
public:
    int subarraySum(vector<int>& arr, int k) {
        int n = arr.size();
        int count =0;
        vector<int> ps(n,0);

        ps[0]=arr[0];
        for(int i=1;i<n;i++){
            ps[i]=ps[i-1]+arr[i];
        }
        unordered_map<int , int> m;
        for(int j=0;j<n;j++){
            if(ps[j]==k) count++;

            int val=ps[j]-k;
            if(m.find(val) != m.end()){
                count=count+m[val];
            }

            // if(m.find(val) == m.end()){
            //     m[ps[j]] = 0;
            // }
            m[ps[j]]++;
        }
        return count;
    }
};