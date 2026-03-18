class Solution {
public:
    bool isPalindrome(int x) {
        
    string original = to_string(x);

    string newNum = original;
    reverse(newNum.begin(), newNum.end());

        if(newNum == original){
            return true;
        }

        else{
            return false;
        }
    }
};