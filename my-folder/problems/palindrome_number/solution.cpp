class Solution {
public:
    bool isPalindrome(int x) {
        // std::to_string is used to convert int to string
        // y is the reverse of x
        if (x <0){
            return false;
        }
        long y = 0;
        int x_copy = x;
        int digitNum = 0 ;
        if (x > 0)
            digitNum = log10(x);
        for (;x_copy > 0;){
            y = y*10 + (x_copy % 10);
            x_copy /= 10;
        }
        return y==x;
    }
};